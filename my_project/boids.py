from manimlib.imports import *
import functools

class Boid(object):
	CONFIG = {
		# allowing a different radius for each force
		"radius_of_separation": 1,
		"radius_of_alignment": 1,
		"radius_of_cohesion": 1,
		# TODO: use this angle for figuring out the fov
		"angle_of_separation": PI, # currently not used
		"angle_of_alignment": PI, # currently not used
		"angle_of_cohesion": PI, # currently not used

		# allowing different weights for each force
		"factor_separation": 1,
		"factor_separation_object": 1,
		"factor_alignment": 1,
		"factor_cohesion": 1,

		# allowing different powers for each force
		"separation_object_power": -1,
		"separation_power": -1,
		"alignment_power": 1,
		"cohesion_power": 1,

		"speed_mean": 1,
		"speed_std": 0, # if set to 0, then the speed will stay constant

		"mass": 1, # resistance to forces : F=ma
	}
	def __init__(self, position, velocity, **kwargs):
		# there's no need to call digest config, since this class is a meta class
		# Thus, Boid2D / Boid3D will inherit from a Mobject, and will call digest_config on their own

		self.move_to(position)

		self.set_speed(kwargs.get("speed", self.speed_mean))
		self.set_velocity(velocity)

		# requires `set_direction` method from Cone/Triangle/Boid2D
		self.set_direction(self.velocity)

	#
	# Getting nearby boids
	#
	def set_other_boids(self, boids):
		if self in boids:
			# create a copy of the list, so that we won't change it
			boids = boids[::]
			boids.remove(self)

		self._other_boids = boids
	def get_other_boids(self):
		return getattr(self, "_other_boids", [])
	#
	# Getting nearby objects
	#
	def set_other_objects(self, objects):
		self._other_objects = objects
	def get_other_objects(self):
		return getattr(self, "_other_objects", [])

	#
	# Field Of View & Distance utils
	#
	def is_boid_in_fov(self, other_boid, radius, angle):
		if radius == 0:
			return False

		distance = self.get_boid_distance(other_boid)
		if get_norm(distance) < radius:
			if angle == PI: # full circle
				return True

			# TODO: test this code
			# following https://math.stackexchange.com/questions/878785/how-to-find-an-angle-in-range0-360-between-2-vectors
			vec_1 = distance
			vec_2 = self.velocity
			dot = vec_1.dot(vec_2)
			size_1 = get_norm(vec_1)
			size_2 = get_norm(vec_2)
			other_boid_angle = np.arccos(dot / (size_1 * size_2))
			return other_boid_angle <= angle

		return False
	def get_boid_distance(self, b):
		return b.get_center() - self.get_center()

	def is_object_in_fov(self, obj):
		distance = self.get_object_distance(obj)
		return get_norm(distance) <= self.radius_of_separation
	def get_object_distance(self, obj):
		if type(obj) is LineX:
			distance = Y_AXIS * (obj.y - self.get_center()[1])

			# check if self is in the X range of the line
			x_min = min(obj.x_start, obj.x_end)
			x_max = max(obj.x_start, obj.x_end)

			if self.get_center()[0] > x_max:
				distance += X_AXIS * (self.get_center()[0] - x_max)
			elif self.get_center()[0] < x_min:
				distance += X_AXIS * (x_max - self.get_center()[0])

		elif type(obj) is LineY:
			distance = X_AXIS * (obj.x - self.get_center()[0])

			# check if self is in the X range of the line
			y_min = min(obj.y_start, obj.y_end)
			y_max = max(obj.y_start, obj.y_end)

			if self.get_center()[1] > y_max:
				distance += Y_AXIS * (self.get_center()[1] - y_max)
			elif self.get_center()[1] < y_min:
				distance += Y_AXIS * (y_min - self.get_center()[1])
		elif type(obj) is Circle:
			raise NotImplemented
			# Circle has get_center() & radius
			# size of distance is get_norm(self.get_center() - Circle.get_center()) - radius
			# direction is self.get_center() - Circle.get_center()
			# not sure about that
			distance = np.array([np.inf]*3)
		else:
			distance = np.array([np.inf]*3)

		return distance

	#
	# Getting Field Of View
	#
	def set_fov(self):
		self.fov_separation = list(filter(
			lambda b: self.is_boid_in_fov(b, self.radius_of_separation, self.angle_of_separation),
			self.get_other_boids()
		))
		self.fov_alignment  = list(filter(
			lambda b: self.is_boid_in_fov(b, self.radius_of_alignment , self.angle_of_alignment ),
			self.get_other_boids()
		))
		self.fov_cohesion   = list(filter(
			lambda b: self.is_boid_in_fov(b, self.radius_of_cohesion  , self.angle_of_cohesion  ),
			self.get_other_boids()
		))

		self.fov_separation_objects = list(filter(
			self.is_object_in_fov,
			self.get_other_objects()
		))
	def get_fov_separation(self):
		return getattr(self, "fov_separation", [])
	def get_fov_alignment(self):
		return getattr(self, "fov_alignment", [])
	def get_fov_cohesion(self):
		return getattr(self, "fov_cohesion", [])
	def get_fov_separation_objects(self):
		return getattr(self, "fov_separation_objects", [])

	#
	# calculating the different forces
	#
	def calculate_force(self, factor, vector, power, repel=False):
		sign = (-1) ** repel
		direction = sign * normalize(vector)
		strength = factor * get_norm(vector)**power
		return strength * direction
	def get_force_separation_boids(self):
		return sum(
			(self.calculate_force(
				factor = self.factor_separation,
				vector = self.get_boid_distance(b),
				power  = self.separation_power,
				repel  = True,
			) for b in self.get_fov_separation()),
			np.zeros(3)
		)
	def get_force_separation_objects(self):
		return sum(
			(self.calculate_force(
				factor = self.factor_separation,
				vector = self.get_object_distance(obj),
				power  = self.separation_object_power,
				repel  = True,
			) for obj in self.get_fov_separation_objects()),
			np.zeros(3)
		)
	def get_force_alignment(self):
		if self.radius_of_alignment == 0 or not self.get_fov_alignment():
			return np.zeros(3)

		velocity_direction = np.mean([b.velocity for b in self.get_fov_alignment()], axis=0)

		return self.calculate_force(self.factor_alignment, velocity_direction, self.alignment_power, repel=False)
	def get_force_cohesion(self):
		if self.radius_of_cohesion == 0 or not self.get_fov_cohesion():
			return np.zeros(3)

		# calculate Center Of Mass
		com_direction = np.mean([self.get_boid_distance(b) for b in self.get_fov_cohesion()], axis=0)

		return self.calculate_force(self.factor_cohesion, com_direction, self.cohesion_power, repel=False)

	def get_force_separation(self):
		return self.get_force_separation_boids() + self.get_force_separation_objects()
	def get_force(self):
		return self.get_force_cohesion() + self.get_force_alignment() + self.get_force_separation()
	@property
	def acceleration(self):
		return self.get_force() / self.mass
	

	#
	# updating
	#
	def updater(self, dt):
		# update fov
		self.set_fov()
		# move according to the old velocity
		self.update_position(dt)
		# update the velocity according to the current acceleration
		self.update_velocity(dt)
		# re-align to the current (updated) velocity
		self.update_direction()
	def update_position(self, dt):
		self.shift(self.velocity * dt)
	def update_velocity(self, dt):
		# this will be the new velocity direction
		increased_velocity = self.velocity + self.acceleration * dt
		# however, we allow for a specific range of speeds
		self.set_speed(get_norm(increased_velocity), normalize=True)
		self.set_velocity(increased_velocity)
	def update_direction(self):
		self.set_direction(self.velocity)

	#
	# Setting Velocity (vector) and Speed (magnitude)
	#
	def set_velocity(self, velocity):
		self.velocity = normalize(velocity) * self.speed
	def set_speed(self, new_speed, normalize=False):
		if normalize:
			# we take the difference between the new speed & the current one
			diff = new_speed - self.speed
			# Then we normalize it to a number between -1 to 1, using the sigmoid function
			# 	(for no particular reason. It simply has a nice behavior)
			normalized_diff = 2 * ((np.exp(diff) / (np.exp(diff) + 1)) - 0.5)
			# Next, convert normalized_diff to a percentage, based on the distance from the min/max allowed speed
			if normalized_diff < 0:
				allowed_change = self.speed - self.min_allowed_speed
			elif normalized_diff > 0:
				allowed_change = self.max_allowed_speed - self.speed
			else:
				allowed_change = 0

			if normalized_diff != normalized_diff: # check if NaN
				# probably diff is too big, so np.exp(diff) gives infinity
				# So we'll convert it to a number between -1 to 1 using a strange rule: 1/diff
				# for no good reason. This is merely a workaround the bug.
				print(f"[!] NaN speed encountered: {diff}")
				normalized_diff = 1/diff
			# the new speed is the current one plus or minus (depending on the sign of normalized_diff)
			# some fraction of the allowed changed (the fraction is expressed in normalized diff)
			self.speed += normalized_diff * allowed_change
		else:
			self.speed = new_speed

	#
	# Speed getter, setter, and other utils
	#
	@property
	def speed(self):
		return getattr(self, "_speed", self.speed_mean)
	@speed.setter
	def speed(self, value):
		# verifying speed range
		if value < self.min_allowed_speed:
			print("[!] a speed lower than the minimum:", value)
			value = self.min_allowed_speed
		if value > self.max_allowed_speed:
			print("[!] a speed higher than the maximum:", value)
			value = self.max_allowed_speed

		self._speed = value

		## Setting a color to represent the velocity
		# normalize to a number between 0 and 1
		try:
			normalized_speed = (value - self.speed_mean + self.speed_std) / (2 * self.speed_std)
			# then use it to get one of the colors (multipliying by color_gradient length minus 1)
			self.set_color(self.speed_color_gradient[int(normalized_speed * 19)])
		except:
			import pdb; pdb.set_trace()
	@property
	def min_allowed_speed(self):
		return self.speed_mean - self.speed_std
	@property
	def max_allowed_speed(self):
		return self.speed_mean + self.speed_std
	@property
	@functools.lru_cache()
	def speed_color_gradient(self):
		return color_gradient([BLUE_A, BLUE_E, RED_E, RED_A], 20)


class Boid2D(Boid, ArrowTip): # ArrowTip is Triangle++
	CONFIG = {
		"dimensions": 2,

		"triangle_config": {},
	}
	def __init__(self, position, velocity, **kwargs):
		# parse CONFIG
		digest_config(self, kwargs)
		# ArrowTip constructor first
		super(Boid, self).__init__(**self.triangle_config, **kwargs)
		# Then Boid constructor
		super().__init__(position, velocity, **kwargs)

	# in the 2d case, `direction` is identical to `angle`. Yet, `direction` is used for generality and compatability with 3D
	def set_direction(self, direction):
		new_angle = angle_of_vector(direction)
		old_angle = self.get_angle()
		self.rotate(new_angle - old_angle)
	def get_direction(self):
		return self.get_angle()


class Boid3D(Boid, Cone):
	CONFIG = {
		"dimensions": 3,

		"cone_config": {
			"base_radius": 0.2,
			"height": 0.5,
		},
		"boid_config": {},
	}
	def __init__(self, position, velocity, **kwargs):
		# parse CONFIG
		digest_config(self, kwargs)
		# Cone constructor first
		super(Boid, self).__init__(**self.cone_config, **kwargs)
		# Then Boid constructor
		super().__init__(position, velocity, **self.boid_config, **kwargs)

class Boids(VMobject):
	CONFIG = {
		"x_min": -7,
		"x_max":  7,
		"y_min": -3.5,
		"y_max":  3.5,
		"z_min": -3,
		"z_max":  3,

		"boid_config": {
			"speed_mean": 1.5,
			"speed_std": 0.5,
		},

		"apply_updaters": [
			# "debug",
			# "stay_in_the_box",
		],

		"dimensions": 2, # either 2 or 3
	}
	def __init__(self, n=5, **kwargs):
		super().__init__(**kwargs)
		self.init_boids(n)

		if "debug" in self.apply_updaters:
			self.for_each(self._boid_class.add_updater, self.debug)
		if "stay_in_the_box" in self.apply_updaters:
			self.for_each(self._boid_class.add_updater, self.stay_in_the_box)

	@property
	@functools.lru_cache()
	def _boid_class(self):
		if self.dimensions == 2:
			return Boid2D
		elif self.dimensions == 3:
			return Boid3D
		else:
			raise ValueError("invalid dimensions value. Please enter either 2 or 3.")

	def _generate_random_positions(self, n):
		# each vector has to be 3d
		random_position = np.array([
			np.random.uniform(self.x_min, self.x_max, n),
			np.random.uniform(self.y_min, self.y_max, n),
			np.random.uniform(self.z_min, self.z_max, n),
		]).T

		# then, we truncate the unwanted dimensions
		random_position[:,self.dimensions:] = np.zeros((n,3-self.dimensions))

		return random_position
	def _generate_random_velocities(self, n):
		# first, choose direction
		random_velocity = np.random.uniform(-1, 1, (n, 3))
		random_velocity[:,self.dimensions:] = np.zeros((n,3-self.dimensions))

		# Then, generate random velocity size (the length of the vector, i.e. the speed)
		mean = self.boid_config["speed_mean"]
		std  = self.boid_config["speed_std"]
		random_speed = np.random.uniform(mean - std, mean + std, n)

		return random_velocity, random_speed

	def init_boids(self, n):
		random_position = self._generate_random_positions(n)
		random_velocity, random_speed = self._generate_random_velocities(n)
		
		self.boids = []

		for i in range(n):
			b = self._boid_class(
				random_position[i],
				random_velocity[i],
				speed=random_speed[i],
				**self.boid_config,
			)
			b.add_updater(b.__class__.updater)
			self.boids.append(b)
		
		self.for_each(Boid.set_other_boids, self.boids)

		self.add(*self.boids)

	# updaters
	def debug(self, boid_self, dt):
		print(boid_self.get_center(), boid_self.velocity)

	def stay_in_the_box(self, boid_self, dt):
		# just keep moving - when reaching one end - go to the other end
		x_size = self.x_max - self.x_min
		y_size = self.y_max - self.y_min
		z_size = self.z_max - self.z_min
		# very manual check
		if boid_self.get_center()[0] > self.x_max:
			boid_self.shift(-x_size*X_AXIS)
		if boid_self.get_center()[0] < self.x_min:
			boid_self.shift( x_size*X_AXIS)

		if boid_self.get_center()[1] > self.y_max:
			boid_self.shift(-y_size*Y_AXIS)
		if boid_self.get_center()[1] < self.y_min:
			boid_self.shift( y_size*Y_AXIS)

		if boid_self.get_center()[2] > self.z_max:
			boid_self.shift(-z_size*Z_AXIS)
		if boid_self.get_center()[2] < self.z_min:
			boid_self.shift( z_size*Z_AXIS)

	def for_each(self, method, *args, **kwargs):
		# the lazy version of a for loop
		for b in self.boids:
			method(b, *args, **kwargs)


###################
#### Obstacles ####
###################

# a line parallel to the x axis, i.e. y doesn't change
class LineX(Line):
	def __init__(self, y, x_start, x_end, **kwargs):
		start = x_start*X_AXIS + y*Y_AXIS
		end   = x_end  *X_AXIS + y*Y_AXIS
		super().__init__(start, end, **kwargs)
		self.y       = y
		self.x_start = x_start
		self.x_end   = x_end
# a line parallel to the y axis, i.e. x doesn't change
class LineY(Line):
	def __init__(self, x, y_start, y_end, **kwargs):
		start = x*X_AXIS + y_start*Y_AXIS
		end   = x*X_AXIS + y_end  *Y_AXIS
		super().__init__(start, end, **kwargs)
		self.x       = x
		self.y_start = y_start
		self.y_end   = y_end


################
#### Scenes ####
################

class Boids2DScene(Scene):
	CONFIG = {
		"objstacles": [
			LineY(3, -1, 1),
			LineX(1, -5, -4),
		],

		"boids_config": {
			"boid_config": {},
		},

		"n": 15, # amount of boids
		"duration": 15, # animation duration in seconds
	}
	def construct(self):
		# create boids
		self.boids = Boids(n=self.n, dimensions=2, **self.boids_config)
		self.add(self.boids)

		# create objects / obstacles
		self.add_boundary()
		self.add(*self.objstacles)

		# inform the boids about the objects
		self.boids.for_each(Boid.set_other_objects, self.borders + self.objstacles)

		# add axes for debug purpose
		self.add_axes()

		self.wait(self.duration)

		self.youtube_description()

	def add_boundary(self):
		l1 = LineY(self.boids.x_min, self.boids.y_min, self.boids.y_max)
		l2 = LineY(self.boids.x_max, self.boids.y_min, self.boids.y_max)
		l3 = LineX(self.boids.y_min, self.boids.x_min, self.boids.x_max)
		l4 = LineX(self.boids.y_max, self.boids.x_min, self.boids.x_max)
		self.borders = [l1, l2, l3, l4]
		self.add(*self.borders)

	def add_axes(self):
		axes = self.axes = Axes()
		# axes.set_stroke(width=2)
		axes.add_coordinates()

		self.add(axes)

	def youtube_description(self):
		try:
			print(f"Boids 2D animation")
			print(f"Title: {self.__class__.__name__[13:]}")
			print(f"Parameters:")
			print(f"  Amount of boids: {self.n}")

			if "boid_config" not in self.boids_config:
				return

			if "speed_mean" in self.boids_config["boid_config"] and "speed_std" in self.boids_config["boid_config"]:
				print(f"  Allowed_speed: {  self.boids_config['boid_config']['speed_mean']} \u00B1 {self.boids_config['boid_config']['speed_std']}")

			print(f"")

			print(f"  Separation (from boids):")
			if "radius_of_separation" in self.boids_config["boid_config"]:
				print(f"    Radius: {       self.boids_config['boid_config']['radius_of_separation']     }")
			if "factor_separation" in self.boids_config["boid_config"]:
				print(f"    Force Factor: { self.boids_config['boid_config']['factor_separation']        }")
			if "separation_power" in self.boids_config["boid_config"]:
				print(f"    Force Power: {  self.boids_config['boid_config']['separation_power']         }")

			print(f"  Separation (from objects):")
			if "radius_of_separation" in self.boids_config["boid_config"]:
				print(f"    Radius: {       self.boids_config['boid_config']['radius_of_separation']     }")
			if "factor_separation_object" in self.boids_config["boid_config"]:
				print(f"    Force Factor: { self.boids_config['boid_config']['factor_separation_object'] }")
			if "separation_object_power" in self.boids_config["boid_config"]:
				print(f"    Force Power: {  self.boids_config['boid_config']['separation_object_power']  }")

			print(f"  Alignment:")
			if "radius_of_alignment" in self.boids_config["boid_config"]:
				print(f"    Radius: {       self.boids_config['boid_config']['radius_of_alignment']      }")
			if "factor_alignment" in self.boids_config["boid_config"]:
				print(f"    Force Factor: { self.boids_config['boid_config']['factor_alignment']         }")
			if "alignment_power" in self.boids_config["boid_config"]:
				print(f"    Force Power: {  self.boids_config['boid_config']['alignment_power']          }")

			print(f"  Cohesion:")
			if "radius_of_cohesion" in self.boids_config["boid_config"]:
				print(f"    Radius: {       self.boids_config['boid_config']['radius_of_cohesion']       }")
			if "factor_cohesion" in self.boids_config["boid_config"]:
				print(f"    Force Factor: { self.boids_config['boid_config']['factor_cohesion']          }")
			if "cohesion_power" in self.boids_config["boid_config"]:
				print(f"    Force Power: {  self.boids_config['boid_config']['cohesion_power']           }")
		except:
			pass

# 3D is still a Work In Progress
class Boids3DScene(SpecialThreeDScene):
	CONFIG = {
		"objstacles": [],

		"n": 5, # amount of boids
		"duration": 5, # animation duration in seconds
	}
	def construct(self):
		self.boids = Boids(n=self.n, dimensions=3)
		self.add(self.boids)

		# inform the boids about the objects
		# self.boids.for_each(Boid.set_other_objects, self.borders + self.objstacles)

		self.wait(self.duration)

	def add_boundary(self):
		p_xy_top    = PlaneXY(self.boids.z_max, self.boids.x_min, self.boids.x_max, self.boids.y_min, self.boids.y_max)
		p_xy_bottom = PlaneXY(self.boids.z_min, self.boids.x_min, self.boids.x_max, self.boids.y_min, self.boids.y_max)
		p_xz_top    = PlaneXZ(self.boids.y_max, self.boids.x_min, self.boids.x_max, self.boids.z_min, self.boids.z_max)
		p_xz_bottom = PlaneXZ(self.boids.y_min, self.boids.x_min, self.boids.x_max, self.boids.z_min, self.boids.z_max)
		p_yz_top    = PlaneYZ(self.boids.x_max, self.boids.y_min, self.boids.y_max, self.boids.z_min, self.boids.z_max)
		p_yz_bottom = PlaneYZ(self.boids.x_min, self.boids.y_min, self.boids.y_max, self.boids.z_min, self.boids.z_max)
		self.borders = [p_xy_top, p_xy_bottom, p_xz_top, p_xz_bottom, p_yz_top, p_yz_bottom]
		self.add(*self.borders)

class Boids2DScene_1(Boids2DScene):
	# doesn't converge
	CONFIG = {
		"objstacles": [
			LineY(3, -1, 1),
			LineX(1, -5, -4),
		],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 1,
				"radius_of_alignment": 2,
				"radius_of_cohesion": 2.5,

				# allowing different weights for each force
				"factor_separation": 2.5,
				"factor_separation_object": 1,
				"factor_alignment": 1.5,
				"factor_cohesion": 1.5,

				# allowing different powers for each force
				"separation_object_power": -1,
				"separation_power": -1,
				"alignment_power": 1,
				"cohesion_power": 1.3,

				"speed_mean": 1,
				"speed_std": 0.5, # if set to 0, then the speed will stay constant
			},
		},
		"n": 15,
		"duration": 20,
	}

class Boids2DScene_small_fov(Boids2DScene):
	# doesn't converge ; very small group radius
	CONFIG = {
		"objstacles": [],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": .5,
				"radius_of_alignment": 1,
				"radius_of_cohesion": 1,

				# allowing different weights for each force
				"factor_separation": 1,
				"factor_separation_object": 1.75,
				"factor_alignment": 2.25,
				"factor_cohesion": 1.75,

				# allowing different powers for each force
				"separation_object_power": -1,
				"separation_power": -1.25,
				"alignment_power": 1.3,
				"cohesion_power": 1.7,

				"speed_mean": 1,
				"speed_std": 0.5, # if set to 0, then the speed will stay constant
			},
			"apply_updaters": [
				"stay_in_the_box",
			],
		},
		"n": 15,
		"duration": 30,
	}
class Boids2DScene_medium_fov(Boids2DScene):
	# quickly group ; normal group behavior
	CONFIG = {
		"objstacles": [],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 1.5,
				"radius_of_alignment": 2.5,
				"radius_of_cohesion": 3,

				# allowing different weights for each force
				"factor_separation": 1,
				"factor_separation_object": 1,
				"factor_alignment": 2.25,
				"factor_cohesion": 1.75,

				# allowing different powers for each force
				"separation_object_power": -1,
				"separation_power": -1.25,
				"alignment_power": 1.3,
				"cohesion_power": 1.7,

				"speed_mean": 1,
				"speed_std": 0.5, # if set to 0, then the speed will stay constant
			},
			"apply_updaters": [
				"stay_in_the_box",
			],
		},
		"n": 15,
		"duration": 30,
	}
class Boids2DScene_large_fov(Boids2DScene):
	# quickly group ; normal group behavior ; big group radius
	CONFIG = {
		"objstacles": [],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 3,
				"radius_of_alignment": 5,
				"radius_of_cohesion": 5,

				# allowing different weights for each force
				"factor_separation": 1,
				"factor_separation_object": 2,
				"factor_alignment": 2.25,
				"factor_cohesion": 1.75,

				# allowing different powers for each force
				"separation_object_power": -1,
				"separation_power": -1.25,
				"alignment_power": 1.3,
				"cohesion_power": 1.7,

				"speed_mean": 1,
				"speed_std": 0.5, # if set to 0, then the speed will stay constant
			},
			"apply_updaters": [
				"stay_in_the_box",
			],
		},
		"n": 15,
		"duration": 20,
	}
class Boids2DScene_uniform_large_fov(Boids2DScene):
	# bad ; buggy ; they group, very widely
	CONFIG = {
		"objstacles": [],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 2.5,
				"radius_of_alignment": 2.5,
				"radius_of_cohesion": 2.5,

				# allowing different weights for each force
				"factor_separation": 1.5,
				"factor_separation_object": 1,
				"factor_alignment": 2,
				"factor_cohesion": 1.5,

				# allowing different powers for each force
				"separation_object_power": -1,
				"separation_power": -1,
				"alignment_power": 1.5,
				"cohesion_power": 1.2,

				"speed_mean": 2,
				"speed_std": 1, # if set to 0, then the speed will stay constant
			},
			"apply_updaters": [
				"stay_in_the_box",
			],
		},
		"n": 15,
		"duration": 60*4,
	}

class Boids2DScene_strong_separation(Boids2DScene):
	# quickly group ; large group radius ; wiggles
	CONFIG = {
		"objstacles": [],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 1.5,
				"radius_of_alignment": 2.5,
				"radius_of_cohesion": 3,

				# allowing different weights for each force
				"factor_separation": 3,
				"factor_separation_object": 1,
				"factor_alignment": 2.25,
				"factor_cohesion": 1.75,

				# allowing different powers for each force
				"separation_object_power": -1.75,
				"separation_power": -1.25,
				"alignment_power": 1.3,
				"cohesion_power": 1.7,

				"speed_mean": 1,
				"speed_std": 0.5, # if set to 0, then the speed will stay constant
			},
			"apply_updaters": [
				"stay_in_the_box",
			],
		},
		"n": 15,
		"duration": 30,
	}
class Boids2DScene_strong_alignment(Boids2DScene):
	# quickly group ; converges
	CONFIG = {
		"objstacles": [],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 1.5,
				"radius_of_alignment": 2.5,
				"radius_of_cohesion": 3,

				# allowing different weights for each force
				"factor_separation": 1,
				"factor_separation_object": 1,
				"factor_alignment": 4.25,
				"factor_cohesion": 1.75,

				# allowing different powers for each force
				"separation_object_power": -1,
				"separation_power": -1.25,
				"alignment_power": 2,
				"cohesion_power": 1.7,

				"speed_mean": 1,
				"speed_std": 0.5, # if set to 0, then the speed will stay constant
			},
			"apply_updaters": [
				"stay_in_the_box",
			],
		},
		"n": 15,
		"duration": 25,
	}
class Boids2DScene_strong_cohesion(Boids2DScene):
	# quickly group ; small group radius ; wiggles
	CONFIG = {
		"objstacles": [],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 1.5,
				"radius_of_alignment": 2.5,
				"radius_of_cohesion": 3,

				# allowing different weights for each force
				"factor_separation": 1,
				"factor_separation_object": 1,
				"factor_alignment": 2.25,
				"factor_cohesion": 4.75,

				# allowing different powers for each force
				"separation_object_power": -1,
				"separation_power": -1.25,
				"alignment_power": 1.3,
				"cohesion_power": 2.5,

				"speed_mean": 1,
				"speed_std": 0.5, # if set to 0, then the speed will stay constant
			},
			"apply_updaters": [
				"stay_in_the_box",
			],
		},
		"n": 15,
		"duration": 25,
	}

class Boids2DScene_weak_separation(Boids2DScene):
	# group ; small group radius ; interesting (doesn't converge)
	CONFIG = {
		"objstacles": [
			LineY(3, -1, 1),
			LineX(1, -5, -4),
		],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 1,
				"radius_of_alignment": 2,
				"radius_of_cohesion": 2.5,

				# allowing different weights for each force
				"factor_separation": 1,
				"factor_separation_object": 1,
				"factor_alignment": 1.5,
				"factor_cohesion": 1.5,

				# allowing different powers for each force
				"separation_object_power": -1,
				"separation_power": -1.25,
				"alignment_power": 1,
				"cohesion_power": 1.5,

				"speed_mean": 1,
				"speed_std": 0.5, # if set to 0, then the speed will stay constant
			},
		},
		"n": 15,
		"duration": 60*4,
	}

class Boids2DScene_Separation_only(Boids2DScene):
	# as expected ; converges (i.e., boring)
	CONFIG = {
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 1,
				"radius_of_alignment": 0,
				"radius_of_cohesion": 0,

				# allowing different weights for each force
				"factor_separation": 1,
				"factor_separation_object": 1,

				# allowing different powers for each force
				"separation_object_power": -1,
				"separation_power": -1,

				"speed_mean": 1,
				"speed_std": 0.25, # if set to 0, then the speed will stay constant
			},
		},
		"n": 15,
		"duration": 40,
	}
class Boids2DScene_Alignment_only(Boids2DScene):
	# converges
	CONFIG = {
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 0,
				"radius_of_alignment": 1,
				"radius_of_cohesion": 0,

				# allowing different weights for each force
				"factor_alignment": 1,

				# allowing different powers for each force
				"alignment_power": 1,

				"speed_mean": 1,
				"speed_std": 0.25, # if set to 0, then the speed will stay constant
			},
			"apply_updaters": [
				"stay_in_the_box",
			],
		},
		"n": 15,
		"duration": 60,
	}
# want more of this
class Boids2DScene_Cohesion_only(Boids2DScene):
	# stable equilibrium (in low quiality)
	CONFIG = {
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 0,
				"radius_of_alignment": 0,
				"radius_of_cohesion": 3,

				# allowing different weights for each force
				"factor_cohesion": 4,

				# allowing different powers for each force
				"cohesion_power": 2,

				"speed_mean": 1,
				"speed_std": 0.25, # if set to 0, then the speed will stay constant
			},
			"apply_updaters": [
				"stay_in_the_box",
			],
		},
		"n": 15,
		"duration": 60*2.5,
	}
class Boids2DScene_no_separation(Boids2DScene):
	# slowly group ; converges
	CONFIG = {
		"objstacles": [
			LineY(3, -1, 1),
			LineX(1, -5, -4),
		],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 0,
				"radius_of_alignment": 2,
				"radius_of_cohesion": 2.5,

				# allowing different weights for each force
				"factor_alignment": 1.5,
				"factor_cohesion": 1.5,

				# allowing different powers for each force
				"alignment_power": 1,
				"cohesion_power": 1.5,

				"speed_mean": 1,
				"speed_std": 0.5, # if set to 0, then the speed will stay constant
			},
			"apply_updaters": [
				"stay_in_the_box",
			],
		},
		"n": 15,
		"duration": 15,
	}
# want more of this
class Boids2DScene_no_alignment(Boids2DScene):
	# like bugs ; somewhat stable equilibrium
	CONFIG = {
		"objstacles": [
			LineY(3, -1, 1),
			LineX(1, -5, -4),
		],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 1,
				"radius_of_alignment": 0,
				"radius_of_cohesion": 2.5,

				# allowing different weights for each force
				"factor_separation": 1,
				"factor_separation_object": 1,
				"factor_alignment": 0,
				"factor_cohesion": 1.5,

				# allowing different powers for each force
				"separation_object_power": -1,
				"separation_power": -1.25,
				"alignment_power": 1,
				"cohesion_power": 1.5,

				"speed_mean": 1,
				"speed_std": 0.5, # if set to 0, then the speed will stay constant
			},
		},
		"n": 15,
		"duration": 40,
	}
class Boids2DScene_no_cohesion(Boids2DScene):
	# they group somewhat quickly ; easily seperate ; wide group radius
	CONFIG = {
		"objstacles": [
			LineY(3, -1, 1),
			LineX(1, -5, -4),
		],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 1,
				"radius_of_alignment": 2,
				"radius_of_cohesion": 0,

				# allowing different weights for each force
				"factor_separation": 1,
				"factor_separation_object": 1.75,
				"factor_alignment": 1.5,
				"factor_cohesion": 0,

				# allowing different powers for each force
				"separation_object_power": -1,
				"separation_power": -1.5,
				"alignment_power": 1,
				"cohesion_power": 1.5,

				"speed_mean": 1,
				"speed_std": 0.5, # if set to 0, then the speed will stay constant
			},
			"apply_updaters": [
				"stay_in_the_box",
			],
		},
		"n": 15,
		"duration": 40,
	}

class Boids2DScene_unique_separation(Boids2DScene):
	# quickly group ; solid group radius
	CONFIG = {
		"objstacles": [],
		"boids_config": {
			"boid_config": {
				# allowing a different radius for each force
				"radius_of_separation": 1.5,
				"radius_of_alignment": 2.5,
				"radius_of_cohesion": 3,

				# allowing different weights for each force
				"factor_separation": 0.5,
				# "factor_separation": 1.5,
				"factor_separation_object": 1,
				"factor_alignment": 2.25,
				"factor_cohesion": 3,

				# allowing different powers for each force
				"separation_object_power": -1.75,
				"separation_power": -2.,
				"alignment_power": 1.3,
				"cohesion_power": 1.5,

				"speed_mean": 1,
				"speed_std": 0.5, # if set to 0, then the speed will stay constant
			},
			"apply_updaters": [
				"stay_in_the_box",
			],
		},
		"n": 15,
		"duration": 25,
	}

class Boids2DScene_more_boids_3(Boids2DScene_1):
	CONFIG = {
		"n": 3,
		"duration": 25,
	}
class Boids2DScene_more_boids_8(Boids2DScene_1):
	CONFIG = {
		"n": 8,
		"duration": 25,
	}
class Boids2DScene_more_boids_12(Boids2DScene_1):
	CONFIG = {
		"n": 12,
		"duration": 25,
	}
class Boids2DScene_more_boids_20(Boids2DScene_1):
	CONFIG = {
		"n": 20,
		"duration": 25,
	}
class Boids2DScene_more_boids_28(Boids2DScene_1):
	CONFIG = {
		"n": 28,
		"duration": 40,
	}

class Boids2DScene_more_boids_28_full(Boids2DScene_more_boids_28):
	CONFIG = {
		"duration": 60*4,
	}

"""
TODO:
- add wind (as a force)

try:
	separation: factor 1.5 ; power -0.5

"""