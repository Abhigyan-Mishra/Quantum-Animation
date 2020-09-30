from manimlib.imports import *

OUTPUT_DIRECTORY = "qubit"


SPHERE_RADIUS = 2


#
# quantum gates
#
Hadamard = 1/np.sqrt(2) * np.array([[1,1],[1,-1]])
Pauli_x = np.array([[0,1],
					[1,0]])
Pauli_y = np.array([[0 ,-1j],
					[1j,0  ]])
Pauli_z = np.array([[1,0 ],
					[0,-1]])
Sqrt_x = 1/2 * np.array([[1+1j,1-1j],
						 [1-1j,1+1j]])
Sqrt_y = 1/2 * np.array([[-1+1j,-1+1j],
						 [1-1j ,-1+1j]])

s2 = np.sqrt(2)
# the sqrt(i) is the phase, so that it will come out as H
Sqrt_H = np.sqrt(1j) / s2 * np.array([[ 1 - 1j/s2 ,   - 1j/s2 ],
									  [   - 1j/s2 , 1 + 1j/s2 ]])
del s2

Hadamard_Y_Z = 1/np.sqrt(2) * np.array([[1 ,-1j], [1j,-1 ]])
# when decomposing this matrix, it resolves into a pi/2 rotation about the X axis. great.

def Phase(phi):
	return np.array([[1,0               ],
					 [0,np.exp(1j * phi)]]) # e^(i phi)
Rz = Phase
def Rx(phi):
	return Hadamard.dot(Phase(phi)).dot(Hadamard)
def Ry(phi):
	return Hadamard_Y_Z.dot(Phase(phi)).dot(Hadamard_Y_Z)


# 
# create a TexMobject which is properly aligned to 3d
# 
def tex(*s):
	tex = TexMobject(*s)
	tex.rotate(90 * DEGREES, RIGHT)
	tex.rotate(90 * DEGREES, OUT)
	tex.scale(0.5)
	return tex
def transform(source, dest):
	t = tex(dest)
	t.move_to(source.get_center())
	t.set_color(source.get_color())
	return Transform(source, t)


# 
# numpy utils
# 
def almost_zero(d):
	return np.around(d, 5) == 0
def complex_to_str(c):
	if almost_zero(c.imag):
		return str(np.around(c.real, 3))
	if almost_zero(c.real):
		return str(np.around(c.imag, 3)) + 'j'
	return str(np.around(c, 3))
def angle_to_str(c):
	return str(np.around(c / DEGREES, 3))


# 
# a quantum state class
#
def angles_to_vector(theta, phi):
	# cos(theta/2) |0> + e^(i theta)*sin(theta/2) |1>
	zero = complex( np.cos(theta/2) )
	one = np.exp(1j * phi) * np.sin(theta/2)
	return np.array([zero, one])
def vector_to_angles(v, verbose=False):
	# alpha = v[0]
	# abs(alpha)^2 = cos^2(theta/2)
	# cos(x)=2 cos(x/2)-1
	# ==> theta = cos^-1(2*abs(alpha)^2 - 1)
	theta = np.arccos(2 * abs(v[0])**2 - 1)
	if verbose:
		print("theta: ", theta)

	# check if it is one of the poles
	if v[0] == 0 or v[1] == 0 or abs(v[0]) == 1:
		if verbose:
			print("    reseting phi")
		phi = 0
	else:
		try:
			phi = -1j * np.log(
				( abs(v[0]) * v[1] )
				 /
				(v[0] * np.sqrt(
					1 - abs(v[0])**2
				))
			)
		except:
			print("    reseting phi (error)")
			phi = 0

	t = theta.real
	p = phi.real
	if p < 0:
		p += 2*PI
	return t, p


# 
# decomposing a generic 2x2 matrix into its rotation axis
# 
class RotationMatrix(object):
	def __init__(self, matrix, automatic_decomposition=True):
		if matrix.shape != (2,2):
			raise ValueError("the input has to be a 2x2 np.ndarray")

		self.matrix = matrix

		# I don't really like operating on objects inside __init__
		# however, since the whole purpose of this object is to expose properties of the matrix
		# And since I've tested the common cases
		# I decided that it would be better (for syntactic reasons) to decompose the matrix inside __init__
		if automatic_decomposition:
			self.decompose()
			self.axis = self._get_rotation_axis()
			self.theta = self._get_rotation_amount()
			self.theta_deg = self.theta * DEGREES

	def decompose(self):
		"""
		assuming a matrix of the form: [ a , b ]
									   [ c , d ]
		we decompose into
		alpha*I + beta*X + gamma*Y + delta*Z
		"""
		a,b,c,d = self.matrix.flatten()
		self.alpha = (a + d)/2
		self.delta = (a - d)/2
		self.beta  = (b + c)/2
		self.gamma = (c - b)/2j

	def _get_rotation_axis(self):
		n = np.linalg.norm([
			self.beta,
			self.gamma,
			self.delta
		])

		return np.array([
			abs(self.beta ) / n,
			abs(self.gamma) / n,
			abs(self.delta) / n,
		])

	def _get_rotation_amount(self):
		"""
		a general rotation matrix, rotation theta radians, in the direction of n_hat, can be written as:
		cos(theta/2) I - i sin(theta/2) n_hat dot sigma_vector
		Thus, we take alpha (the coefficient for I).
		Then we take its absolute value, to remove any absolute phase
		And then we take inverse-cosine, and multiply by 2
		"""
		theta = np.arccos(abs(self.alpha))*2
		if self.alpha.imag < 0:
			theta = TAU - theta
		return theta

	_long_doc = """
	The purpose of this class is to take any 2x2 matrix, and decompose it into the rotation it describes
	This is done using 3 steps:
	1) decompose the matrix into the 3 pauli matrices
	2) find the axis of rotation
	3) find the amount of rotation (in degrees)

	some examples:
	H = 1/sqrt(2) * [[1,1],[1,-1]]
		it breaks into
			(X+Z)/sqrt(2)
		and it is a rotation by 180 degrees

	Sqrt_x = 1/2 * np.array([[1+1j,1-1j],[1-1j,1+1j]])
		it breaks into
			(1+i)/2 I + (1-i)/2 X
			it is a rotation about the X axis
			by 90 degrees

	Phase (pi/4)
		it breaks into
			(0.853+0.35 i)I + (0.146-0.353 i)Z
				(the numbers above are rounded)
			it is a rotation about the Z axis
			by 45 degrees

	Step 1:
		using the "decompose" function, the matrix is written as a linear combination of
			I, X, Y, Z

		There is an alternative decomposition function, which uses Hilbert-Schmidt-Product

	Step 2:
		taking only the coefficients of (X,Y,Z), A unit matrix is created
		by normalizing them into a 3-vector

	Step 3:
		Taking only the coefficient of (I), the amount of rotation is extracted based on:
			http://www.vcpc.univie.ac.at/~ian/hotlist/qc/talks/bloch-sphere-rotations.pdf
			slide number 24, first line
	"""
