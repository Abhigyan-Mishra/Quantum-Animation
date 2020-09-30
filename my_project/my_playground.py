from manimlib.imports import *

Hadamard_1d = ""
# Hadamard_2d = "\\begin{bmatrix} 1 & 1 & 1 & 1 \\\\ 1 & -1 & 1 & -1 \\\\ 1 & 1 & -1 & -1 \\\\ 1 & -1 & -1 & 1\\end{bmatrix}"
Hadamard_2d = "\\frac{1}{2}\\begin{bmatrix} 1 & 1 & 1 & 1 \\\\ 1 & -1 & 1 & -1 \\\\ 1 & 1 & -1 & -1 \\\\ 1 & -1 & -1 & 1\\end{bmatrix}"
C_10        = "\\begin{bmatrix} 1 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 0 & 0 & 1 & 0\\end{bmatrix}"
C_01        = "\\begin{bmatrix} 1 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 1 & 0 & 0\\end{bmatrix}"

class DisplayTex(Scene):
	CONFIG = {
		# 's': "\\ket{0}\\qquad\\ket{1}",
		# 's': "\\ket{1}\\ket{1}\\ket{0}\\ket{1}",
		# 's': "\\ket{1101}",
		# 's': "\\ket{13}_4",
		# 's': "\\ket{0}=\\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}",
		# 's': "\\ket{1}=\\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}",
		# 's': "\\ket{10} = \\ket{1}\\otimes\\ket{0} = \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix} \\otimes \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 0 \\end{bmatrix}",
		# 's': "\\begin{bmatrix} a_1 \\\\ a_2 \\end{bmatrix} \\otimes \\begin{bmatrix} b_1 \\\\ b_2 \\end{bmatrix} = \\begin{bmatrix} a_1 b_1 \\\\ a_1 b_2 \\\\ a_2 b_1 \\\\ a_2 b_2 \\end{bmatrix}",
		# 's': "NOT\\ket{0}=\\ket{1} \\\\ NOT\\ket{1}=\\ket{0}",
		# 's': "X\\ket{0}=\\ket{1} \\\\ X\\ket{1}=\\ket{0}",
		# 's': "ERASE\\ket{0}=\\ket{0} \\\\ ERASE\\ket{1}=\\ket{0}",
		's': "NOT \\  ERASE\\ket{0}=\\ket{1} \\\\ NOT \\  ERASE\\ket{1}=\\ket{1}",
		# 's': "50\\% \\ket{0}+ 50\\% \\ket{1}",
		# 's': "\\ket{\\Psi}=\\alpha_0\\ket{0}+\\alpha_1\\ket{1}",
		# 's': "\\ket{\\Psi}=\\alpha\\ket{0}+\\beta\\ket{1}",
		# 's': "\\ket{\\Psi}=\\frac{1+i}{2}\\ket{0}+\\frac{1-i}{2}\\ket{1}",
		# 's': "\\abs{\\alpha_0}^2 + \\abs{\\alpha_1}^2 = 1",
		# 's': "\\sum_{i=0}^{2^N}\\abs{\\alpha_i}^2=1",
		# 's': "i=\\sqrt{-1}\\Rightarrow i^2=-1",
		# 's': "\\abs{x+iy}^2=x^2+y^2",
		# 's': "\\abs{\\alpha}^2\\equiv\\alpha^2",
		# 's': "\\ket{\\Psi}=\\begin{bmatrix} \\alpha_0 \\\\ \\vdots \\\\ \\alpha_{n-1} \\end{bmatrix}",
		# 's': "\\bra{\\Psi}=\\begin{bmatrix} \\alpha_0^* & \\hdots & \\alpha_{n-1}^* \\end{bmatrix}",
		# 's': "\\bra{\\Phi}\\ket{\\Psi}=\\sum_{i=0}^{n-1} \\beta_i^*\\alpha_i",
		# 's': "X\\ket{0}=\\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}=\\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}=\\ket{1}",
		# 's': "X\\ket{1}=\\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}=\\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}=\\ket{0}",
		# 's': "C_{10}\\ket{xy}",
		# 's': "(A \\otimes B) \\otimes C = A \\otimes (B \\otimes C)",
		# 's': "I_5 \\otimes X_4 \\otimes I_3 \\otimes I_2 \\otimes X_1 \\otimes I_0",
		# 's': "X_4 X_1=X_1 X_4",
		# 's': "V U \\ket{x}",
		# 's': "\\ket{101}=\\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix} \\otimes \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix} \\otimes \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}=\\begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \\\\ 0 \\\\ 0 \\end{bmatrix}",
		# 's': "\\ket{x_2 x_1 x_0}=\\begin{bmatrix} \\gamma_0 \\\\ \\gamma_1 \\end{bmatrix} \\otimes \\begin{bmatrix} \\beta_0 \\\\ \\beta_1 \\end{bmatrix} \\otimes \\begin{bmatrix} \\alpha_0 \\\\ \\alpha_1 \\end{bmatrix}=\\begin{bmatrix} \\gamma_0 \\beta_0 \\alpha_0 \\\\ \\gamma_0 \\beta_0 \\alpha_1 \\\\ \\gamma_0 \\beta_1 \\alpha_0 \\\\ \\gamma_0 \\beta_1 \\alpha_1 \\\\ \\gamma_1 \\beta_0 \\alpha_0 \\\\ \\gamma_1 \\beta_0 \\alpha_1 \\\\ \\gamma_1 \\beta_1 \\alpha_0 \\\\ \\gamma_1 \\beta_1 \\alpha_1 \\end{bmatrix}",
		# 's': "H\\ket{0}= \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 & 1 \\\\ 1 & -1 \\end{bmatrix} \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}= \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix} = \\frac{\\ket{0} + \\ket{1}}{\\sqrt{2}} \\equiv \\ket{+}",
		# 's': "H\\ket{1}= \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 & 1 \\\\ 1 & -1 \\end{bmatrix} \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}= \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ -1 \\end{bmatrix} = \\frac{\\ket{0} - \\ket{1}}{\\sqrt{2}} \\equiv \\ket{-}",
		# 's': "H = \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 1 & 1 \\\\ 1 & -1 \\end{bmatrix} = \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} + \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix} = \\frac{\\sigma_{x} + \\sigma_{z}}{\\sqrt{2}}",
		# 's': "P(k)=\\frac{\\lambda^k e^{-\\lambda}}{k!}",
		# 's': "\\frac{1}{2}\\cdot\\ket{0}=\\frac{1}{2}\\cdot\\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}=\\begin{bmatrix} \\frac{1}{2} \\\\ 0 \\end{bmatrix}",
		# 's': "5\\cdot\\ket{0}+7\\cdot\\ket{1}=5\\cdot\\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}+7\\cdot\\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}=\\begin{bmatrix} 5 \\\\ 7 \\end{bmatrix}",
		# 's': "H(H\\ket{0})=H\\frac{\\ket{0}+\\ket{1}}{\\sqrt{2}}=\\frac{\\ket{0}+\\ket{1}}{2}+\\frac{\\ket{0}-\\ket{1}}{2}=\\ket{0}",
		# 's': "H(H\\ket{1})=H\\frac{\\ket{0}-\\ket{1}}{\\sqrt{2}}=\\frac{\\ket{0}+\\ket{1}}{2}-\\frac{\\ket{0}-\\ket{1}}{2}=\\ket{1}",
		# 's': "H^{(2)}\\ket{00}=(H\\ket{0})(H\\ket{0})=(\\frac{\\ket{0}+\\ket{1}}{\\sqrt{2}})(\\frac{\\ket{0}+\\ket{1}}{\\sqrt{2}})=\\frac{\\ket{00}+\\ket{01}+\\ket{10}+\\ket{11}}{2}",
		# 's': "C_{10}H_1\\ket{00}=C_{10}\\frac{\\ket{0}+\\ket{1}}{\\sqrt{2}}\\ket{0}=\\frac{\\ket{00}+\\ket{11}}{\\sqrt{2}}\\equiv\\ket{\\Phi^+}",
		# 's': "H^{(2)}C_{10}H^{(2)}=%s%s%s" % (Hadamard_2d, C_10, Hadamard_2d),
		# 's': "O_x=%s=C_{01}" % C_01,
	}

	def construct(self):
		self.camera.background_color = WHITE
		self.camera.init_background()

		a = TexMobject(self.s)
		# a.scale(1.5)
		a.scale(0.6)
		a.set_color(BLACK)
		self.add(a)

# who goes where
class DisplayTex2(Scene):
	def construct(self):
		# NOT        = TexMobject("\\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}")
		ERASE      = TexMobject("\\begin{bmatrix} 1 & 1 \\\\ 0 & 0 \\end{bmatrix}")
		ZERO_WHO   = TexMobject("\\ket{0}").move_to(1*UP     + 0.35*LEFT)
		ZERO_WHERE = TexMobject("\\ket{0}").move_to(0.3*UP   + 1  *LEFT)
		ONE_WHO    = TexMobject("\\ket{1}").move_to(1*UP     + 0.4*RIGHT)
		ONE_WHERE  = TexMobject("\\ket{1}").move_to(0.3*DOWN + 1  *LEFT)
		WHO       = TextMobject("Who").move_to(1.7*UP)
		WHERE     = TextMobject("Where").move_to(2.3*LEFT)
		self.add(ERASE, ZERO_WHO, ZERO_WHERE, ONE_WHO, ONE_WHERE, WHO, WHERE)

# 2 bits basis
class DisplayTex3(Scene):
	def construct(self):
		t0 = TexMobject("\\ket{0}_2=\\ket{00}=\\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \\end{bmatrix}").move_to(1.4*UP   + 2.5*LEFT )
		t1 = TexMobject("\\ket{1}_2=\\ket{01}=\\begin{bmatrix} 0 \\\\ 1 \\\\ 0 \\\\ 0 \\end{bmatrix}").move_to(1.4*UP   + 2.5*RIGHT)
		t2 = TexMobject("\\ket{2}_2=\\ket{10}=\\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 0 \\end{bmatrix}").move_to(1.4*DOWN + 2.5*LEFT )
		t3 = TexMobject("\\ket{3}_2=\\ket{11}=\\begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 1 \\end{bmatrix}").move_to(1.4*DOWN + 2.5*RIGHT)

		self.add(t0, t1, t2, t3)

# different colors for different letters
class DisplayTex4(Scene):
	def construct(self):
		# s = TexMobject("C_{", "i", "j", "}\\ket{x_{n-1} \\hdots x_1 x_0}")
		s = TexMobject("\\frac{\\alpha}{2}(\\ket{", '0', '0', '0', "}+\\ket{", '0', '1', '1', "}) + \\frac{\\beta}{2}(\\ket{", '1', '0', '0', "}+\\ket{", '1', '1', '1', "})")
		
		s[1].set_color(GREEN)
		s[2].set_color(BLUE)
		s[3].set_color(RED)

		s[5].set_color(GREEN)
		s[6].set_color(BLUE)
		s[7].set_color(RED)

		s[9].set_color(GREEN)
		s[10].set_color(BLUE)
		s[11].set_color(RED)

		s[13].set_color(GREEN)
		s[14].set_color(BLUE)
		s[15].set_color(RED)

		self.add(s)

class DisplayMatrix(Scene):
	CONFIG = {
		# "name": "X",
		# "values": [
		# 	[0,1],
		# 	[1,0]
		# ],
		# "name": "ERASE",
		# "values": [
		# 	[1,1],
		# 	[0,0]
		# ],
		# "name": "NOT \\  ERASE",
		# "values": [
		# 	[0,0],
		# 	[1,1]
		# ],
		# "name": "SWAP",
		# "values": [
		# 	[1,0,0,0],
		# 	[0,0,1,0],
		# 	[0,1,0,0],
		# 	[0,0,0,1],
		# ],
		# "name": "C_{01}",
		# "values": [
		# 	[1,0,0,0],
		# 	[0,0,0,1],
		# 	[0,0,1,0],
		# 	[0,1,0,0],
		# ],
		# "name": "C_{10}",
		# "values": [
		# 	[1,0,0,0],
		# 	[0,1,0,0],
		# 	[0,0,0,1],
		# 	[0,0,1,0],
		# ],
		# "name": "H",
		# "values": [
		# 	[1,1],
		# 	[1,-1]
		# ],
		# "name": "H^{(2)}",
		# "values": [
		# 	[1, 1, 1, 1],
		# 	[1,-1, 1,-1],
		# 	[1, 1,-1,-1],
		# 	[1,-1,-1, 1],
		# ],
		# "name": "AND",
		# "values": [
		# 	[1,0,0,0,0,0,0,0],
		# 	[0,1,0,0,0,0,0,0],
		# 	[0,0,1,0,0,0,0,0],
		# 	[0,0,0,1,0,0,0,0],
		# 	[0,0,0,0,1,0,0,0],
		# 	[0,0,0,0,0,1,0,0],
		# 	[0,0,0,0,0,0,0,1],
		# 	[0,0,0,0,0,0,1,0],
		# ],
		# "name": "OR",
		# "values": [
			# [1,0,0,0,0,0,0,0], # 000
			# [0,1,0,0,0,0,0,0], # 001
			# [0,0,0,1,0,0,0,0], # 010
			# [0,0,1,0,0,0,0,0], # 011
			# [0,0,0,0,0,1,0,0], # 100
			# [0,0,0,0,1,0,0,0], # 101
			# [0,0,0,0,0,0,0,1], # 110
			# [0,0,0,0,0,0,1,0], # 111
		# ],
		# "name": "XOR",
		# "values": [
		# 	[1,0,0,0,0,0,0,0], # 000
		# 	[0,1,0,0,0,0,0,0], # 001
		# 	[0,0,0,1,0,0,0,0], # 010
		# 	[0,0,1,0,0,0,0,0], # 011
		# 	[0,0,0,0,0,1,0,0], # 100
		# 	[0,0,0,0,1,0,0,0], # 101
		# 	[0,0,0,0,0,0,1,0], # 110
		# 	[0,0,0,0,0,0,0,1], # 111
		# ],
		"name": "M",
		"values": [
			["m_{00}","m_{01}"],
			["m_{10}","m_{11}"]
		],

		"factor": "",
		# "factor": "\\frac{1}{\\sqrt{2}}",
		# "factor": "\\frac{1}{2}",
	}

	def construct(self):
		m = ' \\\\ '.join(
			' & '.join(str(i) for i in row)
			for row in self.values
		)

		# "\\begin{bmatrix} a_1 \\\\ a_2 \\end{bmatrix} \\otimes \\begin{bmatrix} b_1 \\\\ b_2 \\end{bmatrix} = \\begin{bmatrix} a_1 b_1 \\\\ a_1 b_2 \\\\ a_2 b_1 \\\\ a_2 b_2 \\end{bmatrix}",

		s = f"{self.name} = {self.factor} \\begin{{bmatrix}} {m} \\end{{bmatrix}}"
		print(s)
		a = TexMobject(s)
		# a.scale(1.5)

		self.add(a)

# dashed lines seperating a matrix
class DisplayMatrix2(Scene):
	def construct(self):
		a = TexMobject("C_{10} = \\begin{bmatrix} 1 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 0 & 0 & 1 & 0 \\end{bmatrix} = \\begin{bmatrix} I & 0 \\\\ 0 & X \\end{bmatrix}")
		a.scale(1.3)

		l1 = DashedLine(
			start=1.7*DOWN + 0.6*LEFT,
			end=1.7*UP + 0.6*LEFT,
		).set_color(RED)

		l2 = DashedLine(
			start=1.3*RIGHT,
			end=2.5*LEFT,
		).set_color(RED)
		

		self.add(a, l1, l2)
		# self.add(a, b, TWO_WHO, c, ONE_WHERE)

# dashed lines seperating a matrix
class DisplayMatrix3(Scene):
	def construct(self):
		a = TexMobject("I_1 \\otimes X_0 = \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix} \\otimes X_0 = \\begin{bmatrix} 1 \\cdot X_0 & 0 \\cdot X_0 \\\\ 0 \\cdot X_0 & 1 \\cdot X_0 \\end{bmatrix} = \\begin{bmatrix} 0 & 1 & 0 & 0 \\\\ 1 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 0 & 0 & 1 & 0 \\end{bmatrix} = \\begin{bmatrix} X & 0 \\\\ 0 & X \\end{bmatrix}")
		# a = TexMobject("I_1 \\otimes X_0 = \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix} \\otimes \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} = \\begin{bmatrix} 0 & 1 & 0 & 0 \\\\ 1 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 0 & 0 & 1 & 0 \\end{bmatrix} = \\begin{bmatrix} X & 0 \\\\ 0 & X \\end{bmatrix}")
		# a = TexMobject("X_1 \\otimes I_0 = \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} \\otimes \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix} = \\begin{bmatrix} 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 1 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\end{bmatrix} = \\begin{bmatrix} 0 & I \\\\ I & 0 \\end{bmatrix}")
		a.scale(0.6)

		l1 = DashedLine(
			start=1*DOWN + 1.7*RIGHT + 0.4*RIGHT,
			end=1*UP + 1.7*RIGHT + 0.4*RIGHT,
		).set_color(RED)

		l2 = DashedLine(
			start=2.7*RIGHT + 0.4*RIGHT,
			end=0.6*RIGHT + 0.4*RIGHT,
		).set_color(RED)

		l1.scale(0.8)
		l2.scale(0.8)


		l1.shift(0.15*RIGHT)
		l2.shift(0.15*RIGHT)
		

		self.add(a, l1, l2)
		# self.add(a, b, TWO_WHO, c, ONE_WHERE)

# trying to automate the who-goes-where
class DisplayMatrix4(Scene):
	CONFIG = {
		"name": "SWAP",
		"values": [
			[1,0,0,0],
			[0,0,1,0],
			[0,1,0,0],
			[0,0,0,1],
		],
		
	}

	def construct(self):
		m = ' \\\\ '.join(
			' & '.join(str(i) for i in row)
			for row in self.values
		)

		s = f"{self.name} = \\begin{{bmatrix}} {m} \\end{{bmatrix}}"
		print(s)
		a = TexMobject(s)
		a.scale(1.5)

		# self.add_col_rectangle(0, "\\ket{00}")
		# self.add_row_rectangle(0, "\\ket{00}")

		# self.add_col_rectangle(1, "\\ket{01}")
		# self.add_row_rectangle(2, "\\ket{10}")

		self.add_col_rectangle(2)
		self.add_row_rectangle(1, "\\ket{01}")

		# self.add_col_rectangle(3)
		# self.add_row_rectangle(3)


		self.add(a)

	def add_row_rectangle(self, rownum, name=True):
		r = Rectangle(
			width=len(self.values)+0.7,
			height=0.8,
		)
		r.set_color(BLUE)

		# center the rectangle around the midpoint
		center = (len(self.values)-1)/2
		r.shift(center*UP)

		# shift according to the row
		r.shift(rownum*DOWN)

		# correction
		r.shift(0.1*UP*(rownum-1))

		r.shift(1.8*RIGHT)

		self.add(r)

		if name is True:
			name = self._generate_name(rownum)
		if name:
			n = TexMobject(name)
			n.set_color(BLUE)

			n.shift(LEFT)
			n.shift(center*UP)
			n.shift(rownum*DOWN)
			n.shift(0.1*UP*(rownum-1))

			self.add(n)

		return r

	def add_col_rectangle(self, colnum, name=True):
		r = Rectangle(
			width=0.7,
			height=len(self.values)+0.1,
		)
		r.set_color(RED)

		# center the rectangle around the left-most column
		r.shift(0.15*RIGHT)

		# shift according to the column
		r.shift(colnum*1.1*RIGHT)

		self.add(r)

		if name is True:
			name = self._generate_name(colnum)
		if name:
			n = TexMobject(name)
			n.set_color(RED)

			n.shift(2.4*UP)
			n.shift(0.15*RIGHT)
			n.shift(colnum*1.1*RIGHT)
			
			self.add(n)

		return r

	def _generate_name(self, value):
		return "\\ket{%s}" % bin(value)[2:]

# showing a matrix with multiple names
class DisplayMatrix5(Scene):
	def construct(self):
		# a = TexMobject("C^{Z}_{10} = \\begin{bmatrix} I & 0 \\\\ 0 & Z \\end{bmatrix} = \\begin{bmatrix} 1 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & -1 \\end{bmatrix} = C^{Z}_{01}")
		# a = TexMobject("\\sigma_{Z} = Z = \\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix}")
		a = TexMobject("\\sigma_{Y} = Y = \\begin{bmatrix} 0 & -i \\\\ i & 0 \\end{bmatrix}")
		a.scale(1.3)

		self.add(a)

