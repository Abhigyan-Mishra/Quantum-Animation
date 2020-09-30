import itertools

import numpy as np

from manimlib.constants import *
from manimlib.mobject.three_dimensions import Sphere
from manimlib.mobject.svg.tex_mobject import TexMobject
from manimlib.mobject.types.vectorized_mobject import VGroup, VMobject
from manimlib.scene.three_d_scene import SpecialThreeDScene


#
# utils
#

# converting from the atomic radius to plotting radius
PEROVSKITE_SIZE_FACTOR = 1e9

# returns the 6 faces of a cube
ALL_SIDES = [UP, DOWN, RIGHT, LEFT, IN, OUT]
def all_sides():
	for sign, direction in itertools.product([1,-1], [X_AXIS, Y_AXIS, Z_AXIS]):
		yield sign*direction

# returns the 8 edges of a cube
def all_edges():
	for x_sign, y_sign, z_sign in itertools.product([1,-1], [1,-1], [1,-1]):
		yield X_AXIS*x_sign + Y_AXIS*y_sign + Z_AXIS*z_sign



#
# Particle3D is a Sphere, with physical properties
#
class Particle3D(Sphere):
	CONFIG = {
		# velocity can be either a vector or a scalar
		"velocity": np.array((0., 0., 0.)), # m/s
		"mass": 1, # unified atomic mass units

		"radius": 1, # this is the plotting radius for the sphere
	}

	def __init__(self, point=ORIGIN, **kwargs):
		super().__init__(**kwargs)
		# Sphere.__init__(self, **kwargs)
		self._point = point
		self.move_to(point)

#
# Atom is a Particle3D mobject, together with data from the periodic table
#
class Atom(Particle3D):
	# by convention, full word (such as velocity, force) is for the vector, while single letter (v, F) is for the scalar
	CONFIG = {
		# this is the real radius of the atom
		"R": 1, # m
		"density": 1, # Kg/m^3

		"protons": 1,
		"neutrons": 1,
		"charge": 0,
	}

	@property
	def radius(self):
		return self.R * PEROVSKITE_SIZE_FACTOR

	@property
	def electrons(self):
		return self.protons - self.charge


#
# Perovskites follow the chemical formula ABX3
# thus, there are 3 classes, each having a different color. that's all.
#
class Perovskite_A(object):
	CONFIG = {
		"fill_color": BLUE_D,
		"fill_opacity": 1.0,
		"checkerboard_colors": [BLUE_D, BLUE_E],
	}
class Perovskite_B(object):
	CONFIG = {
		"fill_color": GREEN_D,
		"fill_opacity": 1.0,
		"checkerboard_colors": [GREEN_D, GREEN_E],
	}
class Perovskite_X(object):
	CONFIG = {
		"fill_color": RED_D,
		"fill_opacity": 1.0,
		"checkerboard_colors": [RED_D, RED_E],
	}


class Perovskite(VGroup):
	CONFIG = {
		"unit_cell_length": 1, # m
		"A": Atom,
		"B": Atom,
		"X": Atom,
		"center": ORIGIN,
	}

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

	@property
	def d(self):
		return PEROVSKITE_SIZE_FACTOR * self.unit_cell_length / 2	



class SinglePerovskite(VGroup):
	CONFIG = {
		"unit_cell_length": 1, # m
		"A": Atom,
		"B": Atom,
		"X": Atom,
		"center": ORIGIN,
	}

	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		A = self.A(self.center)

		B = VGroup(*[
			self.B(self.center + self.d*i)
			for i in all_edges()
		])

		X = VGroup(*[
			self.X(self.center + self.d*i)
			for i in all_sides()
		])

		self.add(A, B, X)

		# print(f"unit cell length: {self.d}")
		# print(f"A radius = {A.radius}")
		# print(f"B radius = {B[0].radius}")
		# print(f"X radius = {X[0].radius}")

	@property
	def d(self):
		return PEROVSKITE_SIZE_FACTOR * self.unit_cell_length / 2	


#
# specific atoms
# pm = 10^-12m
#
class Atom_Sr(Atom, Perovskite_A):
	CONFIG = {
		"R": 219e-12, # m
		"density": 2630, # Kg/m^3
		"mass": 57.905612124,
		"protons": 38,
		"neutrons": 88 - 38, # the stable isotope is 88, with 38 protons
	}
class Atom_Ti(Atom, Perovskite_B):
	CONFIG = {
		"R": 176e-12,
		"density": 4507, # Kg/m^3
		"mass": 47.947946281,
		"protons": 22,
		"neutrons": 48 - 22, # the stable isotope is 48, with 73.72% abundance
	}
class Atom_O(Atom, Perovskite_X):
	CONFIG = {
		"R": 48e-12,
		"density": 1.429, # Kg/m^3
		"mass": 15.99491461956,
		"protons": 8,
		"neutrons": 16 - 8, # the stable isotope is 48, with 73.72% abundance
	}

#
# specific perovskites
#
Perovskite_SrTiO3 = {
	"unit_cell_length": 3.905e-10,
	"A": Atom_Sr,
	"B": Atom_Ti,
	"X": Atom_O,
}
		