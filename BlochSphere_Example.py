from manimlib.imports import *
from my_project.qubit import *
import numpy as np

OUTPUT_DIRECTORY = "qubit"


# 
# hadamard rotation
# 

class BlochSphereHadamardRotate_once_with_sphere_fast(BlochSphereHadamardRotate):
	CONFIG = {
		"rotate_sphere": True,
		"rotate_time": 5,
		"rotate_amount": 1,
	}
class BlochSphereHadamardRotate_once_with_sphere_slow(BlochSphereHadamardRotate):
	CONFIG = {
		"rotate_sphere": True,
		"rotate_time": 8,
		"rotate_amount": 1,
	}
class BlochSphereHadamardRotate_once_without_sphere_fast(BlochSphereHadamardRotate):
	CONFIG = {
		"rotate_sphere": False,
		"rotate_time": 5,
		"rotate_amount": 1,
	}

# 
# regular examples
# 
class BlochSphere_example_X(BlochSphere):
	CONFIG = {
		"operators": [
			Pauli_x,
		],
		"operator_names": [
			"Pauli X",
		],
	}
class BlochSphere_example_Y(BlochSphere):
	CONFIG = {
		"circle_xz_show": True,
		"operators": [
			Pauli_y,
		],
		"operator_names": [
			"Pauli Y",
		],
	}
class BlochSphere_example_Z(BlochSphere):
	CONFIG = {
		"operators": [
			Pauli_z,
		],
		"operator_names": [
			"Pauli Z",
		],
	}

class BlochSphere_example_X_X(BlochSphere):
	CONFIG = {
		"operators": [
			Pauli_x,
			Pauli_x,
		],
		"operator_names": [
			"Pauli X",
			"Pauli X",
		],
	}
class BlochSphere_example_Y_Y(BlochSphere):
	CONFIG = {
		"circle_xz_show": True,
		"operators": [
			Pauli_y,
			Pauli_y,
		],
		"operator_names": [
			"Pauli Y",
			"Pauli Y",
		],
	}
class BlochSphere_example_Z_Z(BlochSphere):
	CONFIG = {
		"operators": [
			Pauli_z,
			Pauli_z,
		],
		"operator_names": [
			"Pauli Z",
			"Pauli Z",
		],
	}

class BlochSphere_example_H_H(BlochSphere):
	CONFIG = {
		"operators": [
			Hadamard,
			Hadamard,
		],
		"operator_names": [
			"Hadamard",
			"Hadamard",
		],
	}
