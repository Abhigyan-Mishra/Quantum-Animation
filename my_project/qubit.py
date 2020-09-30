from manimlib.imports import *
from my_project.qubit_utils import *

OUTPUT_DIRECTORY = "qubit"


class State(Mobject):
	def __init__(self, zero_amplitude, one_amplitude, r=SPHERE_RADIUS, **kwargs):
		Mobject.__init__(self, **kwargs)

		self.zero_amplitude = complex(zero_amplitude)
		self.one_amplitude = complex(one_amplitude)

		self.r = r
		self.theta, self.phi = vector_to_angles(self.get_vector())

		self.line = self.create_line()
		self.add(self.line)

	def _get_cartesian(self):
		return np.array( spherical_to_cartesian(self.r, self.theta, self.phi) )

	def create_line(self):
		return Line(
			start=ORIGIN,
			end=self._get_cartesian(),
		)

	def get_vector(self):
		return np.array([self.zero_amplitude, self.one_amplitude])

	def apply_operator(self, operator, verbose=True):
		if verbose:
			print("from: ", self.get_vector())
		vector_result = operator.dot(self.get_vector())
		if verbose:
			print("to  : ", vector_result)
		new_state = State(*vector_result)
		new_state.set_color(self.color)
		return new_state

state_zero  = State(1,             0,            r=SPHERE_RADIUS)
state_one   = State(0,             1,            r=SPHERE_RADIUS)
state_plus  = State(1/np.sqrt(2),  1/np.sqrt(2), r=SPHERE_RADIUS)
state_minus = State(1/np.sqrt(2), -1/np.sqrt(2), r=SPHERE_RADIUS)


class BlochSphere(SpecialThreeDScene):
	CONFIG = {
		"three_d_axes_config": {
			"num_axis_pieces": 2,
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

		"circle_xz_show": False,
		"circle_xz_color": PINK,

		"circle_xy_show": False,
		"circle_xy_color": GREEN,

		"circle_yz_show": False,
		"circle_yz_color": ORANGE,

		
		"sphere_config": {
			"radius": SPHERE_RADIUS,
			"resolution": (60, 60),
		},
		
		"rotate_sphere": True,
		"rotate_circles": False,
		"rotate_time": 5,
		"operators": [
		],
		"operator_names": [
		],
		"show_intro": True,

		"wait_time": 2,
		"pre_operators_wait_time": 1.5,
		"final_wait_time": 3,
		"intro_wait_time": 3,
		"intro_fadeout_wait_time": 1,
	}

	def construct(self):
		if self.show_intro:
			self.present_introduction()
		self.init_camera()
		self.init_axes()
		self.init_sphere()
		self.init_states()
		self.init_text()
		self.wait(self.pre_operators_wait_time)

		for o in self.operators:
			self.apply_operator(o)
			self.wait(self.wait_time)
		self.wait(self.final_wait_time)

	def present_introduction(self):
		self.intro_tex_1 = TextMobject(
			"\\begin{flushleft}\n"
			"The State of the Qbit"
			"\\\\"
			"as represented in the Bloch Sphere."
			"\n\\end{flushleft}",
			alignment="",
		)
		# self.intro_tex_1 = TextMobject(
		# 	# "\\begin{align*}\n" + "The state of the Qbit" + "\n\\end{align*}",
		# 	"\\begin{flalign}\n" + "The state of the Qbit" + "\n\\end{flalign}",
		# 	# "The state of the Qbit",
		# 	# "\\begin{flushleft}"
		# 	# "The state of the Qbit"
		# 	# "\\\\"
		# 	# "as represented in the Bloch Sphere."
		# 	# "\\end{flushleft}",
		# 	alignment="",
		# 	# template_tex_file_body=TEMPLATE_TEXT_FILE_BODY,
	 #        # arg_separator="",
		# )
		self.intro_tex_1.move_to(2*UP)
		self.add(self.intro_tex_1)
		self.play(
			Write(self.intro_tex_1),
			run_time=1.5
		)

		if self.operator_names:
			self.intro_tex_2 = TextMobject(
				"\\begin{flushleft}"
				"The following gates will be applied:"
				"\\\\"
				+
				"\\\\".join(f"{i+1}) {n}" for i,n in enumerate(self.operator_names))
				+
				"\n\\end{flushleft}",
				alignment="",
			)
			self.intro_tex_2.move_to(0.8*DOWN)
			self.add(self.intro_tex_2)
			self.play(
				Write(self.intro_tex_2),
				run_time=2.5
			)

		self.wait(self.intro_wait_time)

		if self.operator_names:
			self.play(
				FadeOut(self.intro_tex_1),
				FadeOut(self.intro_tex_2)
			)
		else:
			self.play(
				FadeOut(self.intro_tex_1)
			)

		self.wait(self.intro_fadeout_wait_time)

	def init_camera(self):
		self.set_camera_orientation(**self.init_camera_orientation)

	def init_axes(self):
		self.axes = self.get_axes()
		self.set_axes_labels()
		self.add(self.axes)

	def _tex(self, *s):
		tex = TexMobject(*s)
		tex.rotate(90 * DEGREES, RIGHT)
		tex.rotate(90 * DEGREES, OUT)
		tex.scale(0.5)
		return tex

	def set_axes_labels(self):
		labels = VGroup()

		zero = tex("\\ket{0}")
		zero.next_to(
			self.axes.z_axis.number_to_point(1),
			Y_AXIS + Z_AXIS,
			MED_SMALL_BUFF
		)

		one = tex("\\ket{1}")
		one.next_to(
			self.axes.z_axis.number_to_point(-1),
			Y_AXIS - Z_AXIS,
			MED_SMALL_BUFF
		)

		labels.add(zero, one)
		self.axes.z_axis.add(labels)

		x = tex("x")
		x.next_to(
			self.axes.x_axis.number_to_point(1),
			-Y_AXIS,
			MED_SMALL_BUFF
		)
		self.axes.x_axis.add(x)

		y = tex("y")
		y.next_to(
			self.axes.y_axis.number_to_point(1),
			Y_AXIS + Z_AXIS,
			MED_SMALL_BUFF
		)
		self.axes.y_axis.add(y)

	def init_sphere(self):
		sphere = self.get_sphere(**self.sphere_config)
		sphere.set_fill(BLUE_E)
		sphere.set_opacity(0.1)
		self.add(sphere)
		self.sphere = sphere

		if self.circle_xy_show:
			self.circle_xy = Circle(
				radius=SPHERE_RADIUS,
				color=self.circle_xy_color,
			)
			self.circle_xy.set_fill(self.circle_xy_color)
			self.circle_xy.set_opacity(0.1)
			self.add(self.circle_xy)

		if self.circle_xz_show:
			self.circle_xz = Circle(
				radius=SPHERE_RADIUS,
				color=self.circle_xz_color,
			)
			self.circle_xz.rotate(90 * DEGREES, RIGHT)
			self.circle_xz.set_fill(self.circle_xz_color)
			self.circle_xz.set_opacity(0.1)
			self.add(self.circle_xz)

		if self.circle_yz_show:
			self.circle_yz = Circle(
				radius=SPHERE_RADIUS,
				color=self.circle_yz_color,
			)
			self.circle_yz.rotate(90 * DEGREES, UP)
			self.circle_yz.set_fill(self.circle_yz_color)
			self.circle_yz.set_opacity(0.1)
			self.add(self.circle_yz)

	def init_text(self):
		"""
		for each state, write (with its own color):
			the probabilities
			theta & phi
		"""
		# the qquad is used as a placeholder, since the value changes, and the length of the value changes.
		self.tex_zero_vec   = tex("\\ket{BLUE} = ", "\\qquad \\qquad 1", " \\\\ ", "\\qquad 0")
		self.tex_zero_vec.set_color(BLUE)
		self.tex_zero_vec.move_to(Z_AXIS * 2 - Y_AXIS * 4)

		self.tex_zero_theta = tex("\\theta = ", "0.000")
		self.tex_zero_theta.set_color(BLUE)
		self.tex_zero_theta.move_to(Z_AXIS * 1 - Y_AXIS * 4)

		self.tex_zero_phi   = tex("\\phi = ", "0.000")
		self.tex_zero_phi.set_color(BLUE)
		self.tex_zero_phi.move_to(Z_AXIS * 0.5 - Y_AXIS * 4)


		self.tex_one_vec    = tex("\\ket{RED} = ", "\\qquad \\qquad 0", " \\\\ ", "\\qquad 1")
		self.tex_one_vec.set_color(RED)
		self.tex_one_vec.move_to(Z_AXIS * 2 + Y_AXIS * 3.5)

		self.tex_one_theta  = tex("\\theta = ", "180.0")
		self.tex_one_theta.set_color(RED)
		self.tex_one_theta.move_to(Z_AXIS * 1 + Y_AXIS * 4)

		self.tex_one_phi    = tex("\\phi = ", "0.000")
		self.tex_one_phi.set_color(RED)
		self.tex_one_phi.move_to(Z_AXIS * 0.5 + Y_AXIS * 4)

		self.tex_dot_product= tex("\\bra{0}\\ket{1} = ", "\\qquad \\quad 0.000")
		self.tex_dot_product.set_color(WHITE)
		self.tex_dot_product.move_to(- Z_AXIS * 2 + Y_AXIS * 3)

		self.add(
			self.tex_zero_vec,
			self.tex_zero_theta,
			self.tex_zero_phi,

			self.tex_one_vec,
			self.tex_one_theta,
			self.tex_one_phi,

			self.tex_dot_product,
		)

		# the initial values are only used to make enough space for later values
		self.play(
			*self.update_tex_transforms(self.zero, self.one),
			run_time=0.1
		)

	def update_tex_transforms(self, new_zero, new_one):
		zero_state = new_zero.get_vector()
		zero_angles = vector_to_angles(zero_state)
		one_state = new_one.get_vector()
		one_angles = vector_to_angles(one_state)

		dot_product = np.vdot( new_one.get_vector(), new_zero.get_vector())

		return(
			transform(self.tex_zero_vec[1],   complex_to_str(zero_state[0])),
			transform(self.tex_zero_vec[3],   complex_to_str(zero_state[1])),
			transform(self.tex_zero_theta[1], angle_to_str(zero_angles[0]) ),
			transform(self.tex_zero_phi[1],   angle_to_str(zero_angles[1]) ),

			transform(self.tex_one_vec[1],    complex_to_str(one_state[0]) ),
			transform(self.tex_one_vec[3],    complex_to_str(one_state[1]) ),
			transform(self.tex_one_theta[1],  angle_to_str(one_angles[0])  ),
			transform(self.tex_one_phi[1],    angle_to_str(one_angles[1])  ),

			transform(self.tex_dot_product[1],   complex_to_str(dot_product)),
		)

	def init_states(self):
		self.old_zero = self.zero = State(1, 0, r=2)
		self.old_one  = self.one  = State(0, 1, r=2)

		self.zero.set_color(BLUE)
		self.one.set_color(RED)

		self.add(self.zero, self.one)

	def apply_operator(self, operator, verbose=True):
		# preparing the rotation animation
		vg = VGroup(self.old_zero.line, self.old_one.line)
		if self.rotate_sphere:
			vg.add(self.sphere)

		if self.rotate_circles:
			if self.circle_xy_show:
				vg.add(self.circle_xy)
			if self.circle_xz_show:
				vg.add(self.circle_xz)
			if self.circle_yz_show:
				vg.add(self.circle_yz)


		rm = RotationMatrix(operator)

		if verbose:
			print(f"rotating around axis: {rm.axis} by {rm.theta / DEGREES} degrees")

		# preparing the tex update
		new_zero = self.zero.apply_operator(operator)
		new_one = self.one.apply_operator(operator)


		self.play(
			Rotate(
				vg,
				angle=rm.theta,
				axis=rm.axis
			),
			*self.update_tex_transforms(new_zero, new_one),
			run_time=self.rotate_time
		)

		self.zero = new_zero
		self.one  = new_one

	def apply_operator_old(self, operator, verbose=True):
		if verbose:
			print()
			print("00000")
		new_zero = self.zero.apply_operator(operator)
		if verbose:
			print("11111")
		new_one = self.one.apply_operator(operator)

		self.play(
			Transform(self.old_zero, new_zero),
			Transform(self.old_one,  new_one),
			*self.update_tex_transforms(new_zero, new_one),
		)

		self.zero = new_zero
		self.one  = new_one


class BlochSphereHadamardRotate(BlochSphere):
	CONFIG = {
		"show_intro": False,
		"rotate_sphere": True,
		"rotate_time": 5,
		"rotate_amount": 1,
	}

	def construct(self):
		if self.show_intro:
			self.present_introduction()
		self.init_camera()
		self.init_axes()
		self.init_sphere()
		self.init_states()
		self.init_text()
		self.wait(self.pre_operators_wait_time)

		self.init_rotation_axis()

		for _ in range(self.rotate_amount):
			self.haramard_rotate()
			self.wait()
		self.wait(self.final_wait_time)

	def init_rotation_axis(self):
		self.direction = 1/np.sqrt(2) * (X_AXIS + Z_AXIS)

	

		x_arc = Arc(
			arc_center=ORIGIN,
			start_angle=0 * DEGREES,
			angle=45 * DEGREES,
			**{
				"radius": 1,
				"stroke_color": GREEN,
				"stroke_width": 2,
			},
		)

		z_arc = Arc(
			arc_center=ORIGIN,
			start_angle=90 * DEGREES,
			angle=-45 * DEGREES,
			**{
				"radius": 0.8,
				"stroke_color": PINK,
				"stroke_width": 2,
			},
		)
		x_arc.rotate_about_origin(90 * DEGREES, X_AXIS)
		z_arc.rotate_about_origin(90 * DEGREES, X_AXIS)


	def haramard_rotate(self):
		a = VGroup(self.old_zero.line, self.old_one.line)
		if self.rotate_sphere:
			a.add(self.sphere)

		self.play(
			Rotate(
				a,
				angle=PI,
				axis=self.direction
			),
			run_time=self.rotate_time
		)