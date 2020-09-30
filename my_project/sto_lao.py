from manimlib.imports import *
from my_project.qubit_utils import *

OUTPUT_DIRECTORY = "STO_LAO"

"""
TODO

[ ] create a background grid
		similar to coordinate_systems.py
		another useful file: three_d_scene.py

[ ] Create a little axis to be displayed at the top-right
		to help keep track of the orientation

[ ] create 3d vec - with a cone as its tip

[V] change perovskite to be a VGroup
		so that the animation details will be kept here

[ ] fill perovskite
		maybe set x_min, x_max, y_min, y_max, z_min, z_max?
		maybe set `amount`, and create 2n+1 A atoms to each direction
"""



class SinglePerovskiteTest(SpecialThreeDScene):
	CONFIG = {
		"three_d_axes_config": {
			"num_axis_pieces": 1,
			"number_line_config": {
				"unit_size": 2,
				"tick_frequency": 1,
				"numbers_with_elongated_ticks": [0, 1, 2],
				"stroke_width": 2,
			}
		},
		"init_camera_orientation": {
			"phi": 80 * DEGREES,
			# "theta": -135 * DEGREES,
			"theta": 15 * DEGREES,
		},
	}

	def construct(self):
		self.init_camera()
		self.init_axes()

		# Sr = Atom_Sr()

		# Ti = VGroup(*[
		# 	Atom_Ti(point=self.d*i)
		# 	for i in all_edges()
		# ])

		# O = VGroup(*[
		# 	Atom_O(point=self.d*i)
		# 	for i in all_sides()
		# ])

		# self.add(Sr, Ti, O)
		p = SinglePerovskite(**Perovskite_SrTiO3)
		self.add(p)

		self.wait(1)

		self.rotate_to_surface(surface=[1,0,0])
		self.wait(1)
		self.rotate_to_surface(surface=[1,1,0])
		self.wait(1)
		self.rotate_to_surface(surface=[1,1,1])
		self.wait(1)

		return

		rate = 0.05 # 0.02

		print(f"theta={self.camera.get_theta()} ; phi={self.camera.get_phi()} ; gamma={self.camera.get_gamma()}")

		# rotate about theta
		self.begin_ambient_camera_rotation(rate=rate)
		self.wait(10)
		self.stop_ambient_camera_rotation()
		self.wait(1)
		print(f"theta={self.camera.get_theta()} ; phi={self.camera.get_phi()} ; gamma={self.camera.get_gamma()}")

		# rotate about phi
		self.camera.phi_tracker.add_updater(
			lambda m, dt: m.increment_value(rate * dt)
		)
		self.add(self.camera.phi_tracker)
		self.wait(10)
		self.camera.phi_tracker.clear_updaters()
		self.remove(self.camera.phi_tracker)
		self.wait(1)
		print(f"theta={self.camera.get_theta()} ; phi={self.camera.get_phi()} ; gamma={self.camera.get_gamma()}")

		# rotate about gamma
		self.camera.gamma_tracker.add_updater(
			lambda m, dt: m.increment_value(rate * dt)
		)
		self.add(self.camera.gamma_tracker)
		self.wait(10)
		self.camera.gamma_tracker.clear_updaters()
		self.remove(self.camera.gamma_tracker)
		self.wait(1)
		print(f"theta={self.camera.get_theta()} ; phi={self.camera.get_phi()} ; gamma={self.camera.get_gamma()}")

	def init_camera(self):
		self.set_camera_orientation(**self.init_camera_orientation)

	def init_axes(self):
		self.axes = self.get_axes()
		self.add(self.axes)


	def rotate_to_surface(self, surface=[1,0,0], display_vec=True):
		if type(surface) is str:
			assert(len(surface) == 3)
			for c in surface:
				assert(c in ['0', '1'])

			surface = [int(c) for c in surface]
		print(f"surface={surface}")

		if display_vec:
			vec = surface
			# plot vec as a line, not a vector, because of the tip, which is aligned with the xy plane

			# self.play( grow( vec ) )

		# rotate camera
		r, theta, phi = cartesian_to_spherical(*surface)
		self.move_camera(theta=theta, phi=phi)



class SingleSrTiO3(SinglePerovskite):
	pass		