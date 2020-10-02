from manimlib.imports import *
from my_project.qubit import *
import numpy as np

OUTPUT_DIRECTORY = "qubit"


# 
# hadamard rotation
# 

class BlochSphere_example_Z_Z(BlochSphere):
	CONFIG = {
		"operators": [
            Pauli_x,
			Hadamard,
			Pauli_y,
            Hadamard
		],
		"operator_names": [
			"Pauli X",
            "Hadamard",
			"Pauli Y",
            "Hadamard",
		],
	}