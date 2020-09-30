from manimlib.imports import *

OUTPUT_DIRECTORY = "double_pendulum"

class SingleDoublePendulumScene(Scene):
	CONFIG = {
		"run_time": 10,
	}
	def construct(self):
		print_config(self.pendulum_config)
		pendulum = self.pendulum = DoublePendulum(**self.pendulum_config)
		self.add(pendulum)
		self.wait()
		pendulum.start_swinging()
		self.wait(self.run_time)

class MultipleDoublePendulumScene(Scene):
	CONFIG = {
		"pendulums_config": [],
		"run_time": 25,
	}
	def construct(self):
		self.pendulums = []
		for index, config in enumerate(self.pendulums_config):
			print_config(config)
			self.pendulums.append(DoublePendulum(**config))
		# self.pendulums = [DoublePendulum(**config) for config in self.pendulums_config]

		self.add(*self.pendulums)
		self.wait()
		for p in self.pendulums:
			p.start_swinging()
		self.wait(self.run_time)

def print_config(c):
	print(f"""
Red Rod Length       : {c['L1']}
Red Mass             : {c['m1']}
Red Initial Degrees  : {c['initial_theta1'] / DEGREES}
Blue Rod Length      : {c['L2']}
Blue Mass            : {c['m2']}
Blue Initial Degrees : {c['initial_theta2'] / DEGREES}
Gravity              : {c['gravity']}
""")


# intro - small angles
class Intro(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 1,
			"m2": 1,
			"initial_theta1": 10*DEGREES,
			"initial_theta2": -5*DEGREES,
			"initial_omega1": 0,
			"initial_omega2": 0,
			"gravity": 20,
			"weight_diameter": 0.5,
			"n_steps_per_frame": 100,
		},
		"run_time": 15,
	}

# chaos
class Example1(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 1.5,
			"m2": 1,
			"initial_theta1": 10*DEGREES,
			"initial_theta2": 160*DEGREES,
			"initial_omega1": 0,
			"initial_omega2": 0,
			"gravity": 20,
			"weight_diameter": 0.5,
			"n_steps_per_frame": 100,
		},
		"run_time": 15,
	}

# wanted chaos ; got a pattern
class Example2(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 1,
			"m2": 3,
			"initial_theta1": 10*DEGREES,
			"initial_theta2": 90*DEGREES,
			"initial_omega1": 0,
			"initial_omega2": 0,
			"gravity": 20,
			"weight_diameter": 0.5,
			"n_steps_per_frame": 100,
		},
		"run_time": 15,
	}

# loop de loop
class Example3(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 1,
			"m2": 1,
			"initial_theta1": -90*DEGREES,
			"initial_theta2": 90*DEGREES,
			"initial_omega1": 0,
			"initial_omega2": 0,
			"gravity": 20,
			"weight_diameter": 0.5,
			"n_steps_per_frame": 100,
		},
		"run_time": 15,
	}

# energy transfer
class Example4(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 10,
			"m2": 1,
			"initial_theta1": 0*DEGREES,
			"initial_theta2": 90*DEGREES,
			"initial_omega1": 0,
			"initial_omega2": 0,
			"gravity": 20,
			"weight_diameter": 0.5,
			"n_steps_per_frame": 100,
		},
		"run_time": 25,
	}

# the heart
class Example5(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 10,
			"m2": 1,
			"initial_theta1": 90*DEGREES,
			"initial_theta2": 0*DEGREES,
			"initial_omega1": 0,
			"initial_omega2": 0,
			"gravity": 20,
			"weight_diameter": 0.5,
			"n_steps_per_frame": 100,
		},
		"run_time": 25,
	}

# squished sin wave
class Example6(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 1,
			"m2": 1,
			"initial_theta1": 45*DEGREES,
			"initial_theta2": -45*DEGREES,
			"initial_omega1": 0,
			"initial_omega2": 0,
			"gravity": 9.81,
			"weight_diameter": 0.5,
			"n_steps_per_frame": 100,
		},
		"run_time": 25,
	}

# resonance squishing of a sin wave
class Example6_2(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 1,
			"m2": 1.5,
			"initial_theta1": 45*DEGREES,
			"initial_theta2": -45*DEGREES,
			"initial_omega1": 0,
			"initial_omega2": 0,
			"gravity": 9.81,
			"weight_diameter": 0.5,
			"n_steps_per_frame": 100,
		},
		"run_time": 25,
	}

# lets give it a little push
class Example7(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 10,
			"m2": 1,
			"initial_theta1": 0*DEGREES,
			"initial_theta2": 0*DEGREES,
			"initial_omega1": 0,
			"initial_omega2": 2,
			"gravity": 20,
			"weight_diameter": 0.5,
			"n_steps_per_frame": 100,
		},
		"run_time": 25,
	}

# lets give the other one a small push
class Example7_2(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 20,
			"m2": 1,
			"initial_theta1": 0*DEGREES,
			"initial_theta2": 0*DEGREES,
			"initial_omega1": 2,
			"initial_omega2": 0,
			"gravity": 10,
			"weight_diameter": 0.5,
			"n_steps_per_frame": 100,
			# "traj_max_length": 100,
		},
		"run_time": 25,
	}


class Test(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 20,
			"m2": 1,
			"initial_theta1": 0*DEGREES,
			"initial_theta2": 0*DEGREES,
			"initial_omega1": 2,
			"initial_omega2": 0,
			"gravity": 10,
			"weight_diameter": 0.5,
			"n_steps_per_frame": 100,
			# "traj_max_length": 100,
		},
		"run_time": 25,
	}



class OldExample(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 1,
			"m2": 1,
			"initial_theta1": 45*DEGREES,
			"initial_theta2": 90*DEGREES,
			"initial_omega1": 0,
			"initial_omega2": 0,
			"gravity": 9.8,
			"weight_diameter": 0.5,
			"n_steps_per_frame": 100,
		},
		"run_time": 10,
	}
	
class OldExample1(SingleDoublePendulumScene):
	CONFIG = {
		"pendulum_config": {
			"top_point": 2*UP,
			"L1": 2,
			"L2": 2,
			"m1": 1,
			"m2": 1,
			"initial_theta1": 17*DEGREES,
			"initial_theta2": 100*DEGREES,
			"initial_omega1": 0,
			"initial_omega2": 0,
			"weight_diameter": 0.35,
			"gravity": 20,
			"n_steps_per_frame": 100,

			"weight1_color": RED,
			"weight2_color": BLUE,
		},
		"run_time": 25,
	}

class OldExampleDouble(MultipleDoublePendulumScene):
	CONFIG = {
		"pendulums_config": [
			{
				"top_point": 2*UP,
				"L1": 2,
				"L2": 2,
				"m1": 1,
				"m2": 1,
				"initial_theta1": 17*DEGREES,
				"initial_theta2": 100*DEGREES,
				"initial_omega1": 0,
				"initial_omega2": 0,
				"weight_diameter": 0.35,
				"gravity": 20,
				"n_steps_per_frame": 100,

				"weight1_color": RED,
				"weight2_color": BLUE,
			}, {
				"top_point": 2*UP,
				"L1": 2,
				"L2": 2,
				"m1": 1,
				"m2": 1,
				"initial_theta1": -80*DEGREES,
				"initial_theta2": 25*DEGREES,
				"initial_omega1": 0,
				"initial_omega2": 0,
				"weight_diameter": 0.35,
				"gravity": 20,
				"n_steps_per_frame": 100,

				"weight1_color": ORANGE,
				"weight2_color": GREEN,
			},
		],
		"run_time": 25,
	}

class OldExampleDouble1(MultipleDoublePendulumScene):
	CONFIG = {
		"pendulums_config": [
			{
				"top_point": 2*UP,
				"L1": 2,
				"L2": 2,
				"m1": 1,
				"m2": 1,
				"initial_theta1": 17*DEGREES,
				"initial_theta2": 100*DEGREES,
				"initial_omega1": 0,
				"initial_omega2": 0,
				"weight_diameter": 0.35,
				"gravity": 20,
				"n_steps_per_frame": 3,

				"weight1_color": RED,
				"weight2_color": BLUE,
			}, {
				"top_point": 2*UP,
				"L1": 2,
				"L2": 2,
				"m1": 1,
				"m2": 1,
				"initial_theta1": 17*DEGREES,
				"initial_theta2": 110*DEGREES,
				"initial_omega1": 0,
				"initial_omega2": 0,
				"weight_diameter": 0.35,
				"gravity": 20,
				"n_steps_per_frame": 3,

				"weight1_color": RED,
				"weight2_color": GREEN,
			}, {
				"top_point": 2*UP,
				"L1": 2,
				"L2": 2,
				"m1": 1,
				"m2": 1,
				"initial_theta1": 17*DEGREES,
				"initial_theta2": 120*DEGREES,
				"initial_omega1": 0,
				"initial_omega2": 0,
				"weight_diameter": 0.35,
				"gravity": 20,
				"n_steps_per_frame": 3,

				"weight1_color": RED,
				"weight2_color": ORANGE,
			}, {
				"top_point": 2*UP,
				"L1": 2,
				"L2": 2,
				"m1": 1,
				"m2": 1,
				"initial_theta1": 17*DEGREES,
				"initial_theta2": 130*DEGREES,
				"initial_omega1": 0,
				"initial_omega2": 0,
				"weight_diameter": 0.35,
				"gravity": 20,
				"n_steps_per_frame": 3,

				"weight1_color": RED,
				"weight2_color": PINK,
			},
		],
		"run_time": 25,
	}
