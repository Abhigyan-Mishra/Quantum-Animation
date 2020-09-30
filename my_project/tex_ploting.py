from manimlib.imports import *

Hadamard_1d = ""
# Hadamard_2d = "\\begin{bmatrix} 1 & 1 & 1 & 1 \\\\ 1 & -1 & 1 & -1 \\\\ 1 & 1 & -1 & -1 \\\\ 1 & -1 & -1 & 1\\end{bmatrix}"
Hadamard_2d = "\\frac{1}{2}\\begin{bmatrix} 1 & 1 & 1 & 1 \\\\ 1 & -1 & 1 & -1 \\\\ 1 & 1 & -1 & -1 \\\\ 1 & -1 & -1 & 1\\end{bmatrix}"
C_10        = "\\begin{bmatrix} 1 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 0 & 0 & 1 & 0\\end{bmatrix}"
C_01        = "\\begin{bmatrix} 1 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 1 & 0 & 0\\end{bmatrix}"

class WhiteScene(Scene):
	CONFIG = {
        "camera_config": {
	        "background_color": WHITE,
        },
	}

	def _tex(self, string=None, *args, **kwargs):
		if string is None:
			t = TexMobject(self.s, *args, **kwargs)
		else:
			t = TexMobject(string, *args, **kwargs)

		t.set_color(BLACK)
		return t

	def _text(self, string=None, *args, **kwargs):
		if string is None:
			t = TextMobject(self.s, *args, **kwargs)
		else:
			t = TextMobject(string, *args, **kwargs)

		t.set_color(BLACK)
		return t

	def add_tex(self, string=None, scale=None):
		t = self._tex(string=string)

		if scale is not None:
			t.scale(scale)

		self.add(t)
		

class DisplayTex(WhiteScene):
	CONFIG = {
		# 's': "\\ket{0}\\qquad\\ket{1}",

		### chapter 1
		# 's': "\\ket{0}=\\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}",
		# 's': "\\ket{1}=\\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}",
		# 's': "\\frac{1}{2} \\cdot \\ket{0} = \\frac{1}{2} \\cdot \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix} = \\begin{bmatrix} \\frac{1}{2} \\\\ 0 \\end{bmatrix}",
		# 's': "5 \\cdot \\ket{0} + 7 \\cdot \\ket{1} = 5 \\cdot \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix} + 7 \\cdot \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix} = \\begin{bmatrix} 5 \\\\ 7 \\end{bmatrix}",
		# 's': "\\ket{1}\\ket{1}\\ket{0}\\ket{1}",
		# 's': "\\ket{1101}",
		# 's': "\\ket{13}_4",
		## kronecker product
		# 's': "\\begin{bmatrix} a_1 \\\\ a_2 \\end{bmatrix} \\otimes \\begin{bmatrix} b_1 \\\\ b_2 \\end{bmatrix} = \\begin{bmatrix} a_1 b_1 \\\\ a_1 b_2 \\\\ a_2 b_1 \\\\ a_2 b_2 \\end{bmatrix}",
		# 's': "\\ket{10} = \\ket{1}\\otimes\\ket{0} = \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix} \\otimes \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix} = \\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 0 \\end{bmatrix}",
		# 's': "\\ket{101}=\\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix} \\otimes \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix} \\otimes \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}=\\begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \\\\ 0 \\\\ 0 \\end{bmatrix}",
		# 's': "\\ket{x_2 x_1 x_0}=\\begin{bmatrix} \\gamma_0 \\\\ \\gamma_1 \\end{bmatrix} \\otimes \\begin{bmatrix} \\beta_0 \\\\ \\beta_1 \\end{bmatrix} \\otimes \\begin{bmatrix} \\alpha_0 \\\\ \\alpha_1 \\end{bmatrix}=\\begin{bmatrix} \\gamma_0 \\beta_0 \\alpha_0 \\\\ \\gamma_0 \\beta_0 \\alpha_1 \\\\ \\gamma_0 \\beta_1 \\alpha_0 \\\\ \\gamma_0 \\beta_1 \\alpha_1 \\\\ \\gamma_1 \\beta_0 \\alpha_0 \\\\ \\gamma_1 \\beta_0 \\alpha_1 \\\\ \\gamma_1 \\beta_1 \\alpha_0 \\\\ \\gamma_1 \\beta_1 \\alpha_1 \\end{bmatrix}",
		# 's': "\\ket{101}=\\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix} \\otimes \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix} \\otimes \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}=\\begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 0 \\\\ 1 \\\\ 0 \\\\ 0 \\end{bmatrix}",

		### chapter 2
		## NOT
		# 's': "NOT\\ket{0}=\\ket{1} \\\\ NOT\\ket{1}=\\ket{0}",
		# 's': "X\\ket{0}=\\ket{1} \\\\ X\\ket{1}=\\ket{0}",
		# 's': "X\\ket{0}=\\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}=\\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}=\\ket{1}",
		# 's': "X\\ket{1}=\\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}=\\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}=\\ket{0}",
		## ERASE
		# 's': "ERASE\\ket{0}=\\ket{0} \\\\ ERASE\\ket{1}=\\ket{0}",
		# 's': "NOT \\  ERASE\\ket{0}=\\ket{1} \\\\ NOT \\  ERASE\\ket{1}=\\ket{1}",
		## ASSOCIATIVITY
		# 's': "(A \\otimes B) \\otimes C = A \\otimes (B \\otimes C)",
		# 's': "I_5 \\otimes X_4 \\otimes I_3 \\otimes I_2 \\otimes X_1 \\otimes I_0",
		# 's': "X_4 X_1=X_1 X_4",

		### Chapter 3
		## Generic State
		# 's': "\\ket{\\Psi}=\\alpha_0\\ket{0}+\\alpha_1\\ket{1}",
		# 's': "\\ket{\\Psi}=\\alpha\\ket{0}+\\beta\\ket{1}",
		## Example States
		# 's': "\\ket{\\Psi}=\\frac{1+i}{2}\\ket{0}+\\frac{1-i}{2}\\ket{1}",
		## Probability
		# 's': "\\abs{\\alpha_0}^2 + \\abs{\\alpha_1}^2 = 1",
		# 's': "\\sum_{i=0}^{2^N}\\abs{\\alpha_i}^2=1",
		# 's': "P_0=\\abs{\\alpha_0}^2 = \\alpha_0^* \\alpha_0",
		## Hadamard
		# 's': "H\\ket{0} = \\frac{\\ket{0} + \\ket{1}}{\\sqrt{2}} \\\\ H\\ket{1} = \\frac{\\ket{0} - \\ket{1}}{\\sqrt{2}}",
		# 's': "H\\ket{0}= \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 & 1 \\\\ 1 & -1 \\end{bmatrix} \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}= \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix} = \\frac{\\ket{0} + \\ket{1}}{\\sqrt{2}} \\equiv \\ket{+}",
		# 's': "H\\ket{1}= \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 & 1 \\\\ 1 & -1 \\end{bmatrix} \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}= \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ -1 \\end{bmatrix} = \\frac{\\ket{0} - \\ket{1}}{\\sqrt{2}} \\equiv \\ket{-}",
		# 's': "H(H\\ket{0})=H\\frac{\\ket{0}+\\ket{1}}{\\sqrt{2}}=\\frac{\\ket{0}+\\ket{1}}{2}+\\frac{\\ket{0}-\\ket{1}}{2}=\\ket{0}",
		# 's': "H(H\\ket{1})=H\\frac{\\ket{0}-\\ket{1}}{\\sqrt{2}}=\\frac{\\ket{0}+\\ket{1}}{2}-\\frac{\\ket{0}-\\ket{1}}{2}=\\ket{1}",
		# 's': "H = \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 1 & 1 \\\\ 1 & -1 \\end{bmatrix} = \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} + \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix} = \\frac{\\sigma_{x} + \\sigma_{z}}{\\sqrt{2}}",
			# 'scale': 1.1,
		# 's': "H^{(2)}\\ket{00}=(H\\ket{0})(H\\ket{0})=(\\frac{\\ket{0}+\\ket{1}}{\\sqrt{2}})(\\frac{\\ket{0}+\\ket{1}}{\\sqrt{2}})=\\frac{\\ket{00}+\\ket{01}+\\ket{10}+\\ket{11}}{2}",
			# 'scale': .8,
		

		### Chapter 4
		# 's': "H = \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 1 & 1 \\\\ 1 & -1 \\end{bmatrix} = \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} + \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix} = \\frac{\\sigma_{x} + \\sigma_{z}}{\\sqrt{2}}",
			# 'scale': 1,

		### Chapter 5
		# 's': "C_{10}H_1\\ket{00}=C_{10}\\frac{\\ket{0}+\\ket{1}}{\\sqrt{2}}\\ket{0}=\\frac{\\ket{00}+\\ket{11}}{\\sqrt{2}}\\equiv\\ket{\\Phi^+}",
			# 'scale': 1.2,

		### Chapter 7
		# 's': "H^{(2)}C_{10}H^{(2)}=%s%s%s" % (Hadamard_2d, C_10, Hadamard_2d),
			# 'scale': .8,
		# 's': "O_x=%s=C_{01}" % C_01,
			# 'scale': 1.2,

		### Chapter 8
			# 'scale': 1,
		# 's': "Y = \\begin{bmatrix} 0 & -i \\\\ i & 0 \\end{bmatrix} = \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix} \\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix} \\frac{1}{ad-bc} \\begin{bmatrix} d & -b \\\\ -c & a \\end{bmatrix} = PZP^{-1}",
		# 's': "\\frac{1}{ad-bc} \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix} \\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix} \\begin{bmatrix} d & -b \\\\ -c & a \\end{bmatrix}",
		# 's': "\\frac{1}{ad-bc} \\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix} \\begin{bmatrix} d & -b \\\\ c & -a \\end{bmatrix}",
		# 's': "\\frac{1}{ad-bc} \\begin{bmatrix} ad+bc & -ab-ba \\\\ cd+dc & -bc-ad \\end{bmatrix}",
		# 's': "\\frac{1}{ad-bc} \\begin{bmatrix} ad+bc & -2ab \\\\ 2cd & -(ad+bc) \\end{bmatrix}",
		# 's': "(1) \\qquad ad+bc=0",
		# 's': "(2) \\qquad \\frac{2ab}{ad-bc}=i",
		# 's': "(3) \\qquad \\frac{2cd}{ad-bc}=i",
		# 's': "\\begin{bmatrix} a & b \\\\ c & d \\end{bmatrix} = \\begin{bmatrix} a^* & c^* \\\\ b^* & d^* \\end{bmatrix}",
		# 's': "(4) \\qquad a,d\\in \\mathbb{R}",
		# 's': "(5) \\qquad b=c^*",
		# 's': "(I) \\qquad ab=cd",
		# 's': "P\\ket{0} = \\begin{bmatrix} x & -ix \\\\ ix & -x \\end{bmatrix} \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix} = \\begin{bmatrix} x \\\\ ix \\end{bmatrix}",
		# 's': "P = \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 1 & -i \\\\ i & -1 \\end{bmatrix} = \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 0 & -i \\\\ i & 0 \\end{bmatrix} + \\frac{1}{\\sqrt{2}}\\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix} = \\frac{\\sigma_{y} + \\sigma_{z}}{\\sqrt{2}}",


		## Complex Numbers
		# 's': "i=\\sqrt{-1}\\Rightarrow i^2=-1",
		# 's': "\\abs{x+iy}^2=x^2+y^2",
		## Notation
		# 's': "\\abs{\\alpha}^2\\equiv\\alpha^2",
		# 's': "\\ket{\\Psi}=\\begin{bmatrix} \\alpha_0 \\\\ \\vdots \\\\ \\alpha_{n-1} \\end{bmatrix}",
		# 's': "\\bra{\\Psi}=\\begin{bmatrix} \\alpha_0^* & \\hdots & \\alpha_{n-1}^* \\end{bmatrix}",
		# 's': "\\bra{\\Phi}\\ket{\\Psi}=\\sum_{i=0}^{n-1} \\beta_i^*\\alpha_i",
		## Other
		# 's': "C_{10}\\ket{xy}",
		# 's': "50\\% \\ket{0}+ 50\\% \\ket{1}",

		# 's': "V U \\ket{x}",
		# 's': "P(k)=\\frac{\\lambda^k e^{-\\lambda}}{k!}",
		# 's': "\\frac{1}{2}\\cdot\\ket{0}=\\frac{1}{2}\\cdot\\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}=\\begin{bmatrix} \\frac{1}{2} \\\\ 0 \\end{bmatrix}",
		# 's': "5\\cdot\\ket{0}+7\\cdot\\ket{1}=5\\cdot\\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}+7\\cdot\\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}=\\begin{bmatrix} 5 \\\\ 7 \\end{bmatrix}",
		
		# 's': "\\begin{bmatrix} -1 & 0 \\\\ 0 & -1 \\end{bmatrix} = (-1) \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix} = -I",
		# 's': "X\\ket{+} = X \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix} = (1) \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix}",

		# eigenvalues appendix
		# Z
		# 's': "\\ket{0}\\bra{0} = \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix} \\begin{bmatrix} 1 & 0 \\end{bmatrix} = \\begin{bmatrix} 1 & 0 \\\\ 0 & 0 \\end{bmatrix}",
		# 's': "\\ket{1}\\bra{1} = \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix} \\begin{bmatrix} 0 & 1 \\end{bmatrix} = \\begin{bmatrix} 0 & 0 \\\\ 0 & 1 \\end{bmatrix}",
		# 's': "Z = (1)\\ket{0}\\bra{0} + (-1)\\ket{1}\\bra{1} = \\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix}",
		# X
		# 's': "\\ket{+}\\bra{+} = \\frac{1}{2}\\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix} \\begin{bmatrix} 1 & 1 \\end{bmatrix} = \\frac{1}{2}\\begin{bmatrix} 1 & 1 \\\\ 1 & 1 \\end{bmatrix}",
		# 's': "\\ket{-}\\bra{-} = \\frac{1}{2}\\begin{bmatrix} 1 \\\\ -1 \\end{bmatrix} \\begin{bmatrix} 1 & -1 \\end{bmatrix} = \\frac{1}{2}\\begin{bmatrix} 1 & -1 \\\\ -1 & 1 \\end{bmatrix}",
		# 's': "X = (1)\\ket{+}\\bra{+} + (-1)\\ket{-}\\bra{-} = \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}",
		# 's': "\\sqrt{X} = (1)\\ket{+}\\bra{+} + (i)\\ket{-}\\bra{-} = \\frac{1}{2}\\begin{bmatrix} 1+i & 1-i \\\\ 1-i & 1+i \\end{bmatrix}",

		# 's': "\\frac{1}{2^{\\frac{3}{2}}} ( \\ket{000} + \\ket{001} + \\ket{010} + \\ket{011} + \\ket{100} + \\ket{101} + \\ket{110} + \\ket{111})",
		# 's': "input = x = \\ket{x_{n-1} x_{n-2} \\hdots x_2 x_1 x_0}",
		# 's': "key = k = \\ket{k_{n-1} k_{n-2} \\hdots k_2 k_1 k_0}",
		# 's': "output = (k_{n-1} \\& x_{n-1}) \\oplus (k_{n-2} \\& x_{n-2}) \\oplus \\hdots \\oplus (k_{1} \\& x_{1}) \\oplus (k_{0} \\& x_{0})",
		# 's': "P(\\ket{0})=\\abs{\\frac{1}{\\sqrt{2}}}^2 = \\frac{1}{2}",
		# 's': "P(\\ket{1})=\\abs{\\frac{1}{\\sqrt{2}}}^2 = \\frac{1}{2}",
		# 's': "P(\\ket{1})=\\abs{- \\frac{1}{\\sqrt{2}}}^2 = \\frac{1}{2}",
		# 's': "X\\ket{0} = \\ket{1} \\\\ X\\ket{1} = \\ket{0}",
		# 's': "Z\\ket{0} = \\ket{0} \\\\ Z\\ket{1} = - \\ket{1}",
		# 's': "C\\ket{00} = \\ket{00} \\\\ C\\ket{01} = \\ket{01} \\\\ C\\ket{10} = \\ket{11} \\\\ C\\ket{11} = \\ket{10}",
		# 's': "\\begin{bmatrix} \\bra{0}\\ket{1} & \\bra{0}\\ket{0} \\\\ \\bra{1}\\ket{1} & \\bra{1}\\ket{0} \\end{bmatrix}",
		# 's': "\\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}",
		# 's': "C H \\ket{0} \\ket{0} = C \\frac{\\ket{0} + \\ket{1}}{\\sqrt{2}} \\ket{0} = \\frac{C \\ket{0} \\ket{0} + C \\ket{1} \\ket{0}}{\\sqrt{2}} = \\frac{\\ket{00} + \\ket{11}}{\\sqrt{2}}",

		# 's': "F=ma \\qquad ; \\qquad  a=\\frac{dv}{dt}",
		# 's': "F=-\\frac{dU}{dx}",
		# 's': "F=-kx \\qquad ; \\qquad U=\\frac{1}{2}k x^2",
		# 's': "F_x=-kx \\quad ; \\quad F_y=-ky \\quad ; \\quad U=\\frac{1}{2}k (x^2+y^2)",
		# "scale": 1,

		# 's': "Separation \\  boid-boid & \\frac{2.5}{x} \\\\ Separation \\  boid-object & \\frac{1}{x} \\\\ Alignment & 1.5 \\cdot x \\\\ Cohesion & 1.5 \\cdot x^{1.3}",
		# 's': "\\begin{bmatrix} Separation \\  boid-boid & \\frac{2.5}{x} \\\\ Separation \\  boid-object & \\frac{1}{x} \\\\ Alignment & 1.5 \\cdot x \\\\ Cohesion & 1.5 \\cdot x^{1.3} \\end{bmatrix}",
		# "scale": 1,
	}

	def construct(self):
		# self.add_tex()
		# self.add_tex(scale=1.5)
		# self.add_tex(scale=0.6)
		scale = getattr(self, "scale", 1.5)
		self.add_tex(scale=scale)

# who goes where
class DisplayTex2(WhiteScene):
	def construct(self):
		NOT        = self._tex("\\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix}")
		ERASE      = self._tex("\\begin{bmatrix} 1 & 1 \\\\ 0 & 0 \\end{bmatrix}")
		ZERO_WHO   = self._tex("\\ket{0}").move_to(1*UP     + 0.35*LEFT)
		ZERO_WHERE = self._tex("\\ket{0}").move_to(0.3*UP   + 1  *LEFT)
		ONE_WHO    = self._tex("\\ket{1}").move_to(1*UP     + 0.4*RIGHT)
		ONE_WHERE  = self._tex("\\ket{1}").move_to(0.3*DOWN + 1  *LEFT)
		WHO       = self._text("Who").move_to(1.7*UP)
		WHO.set_color(BLUE)
		# WHO       = self._tex("Who", alignment="").move_to(1.7*UP)
		WHERE     = self._text("Where").move_to(2.3*LEFT)
		WHERE.set_color(RED)

		col_rec = Rectangle(
			width=2.1,
			height=0.5,
		)
		col_rec.set_color(RED)
		col_rec.shift(0.3*LEFT + 0.275*DOWN)
		col_rec.shift(0.575*UP)

		row_rec = Rectangle(
			width=0.55,
			height=1.9,
		)
		row_rec.set_color(BLUE)
		row_rec.shift(0.35*LEFT + 0.4*UP)
		# row_rec.shift(0.75*RIGHT)

		# self.add(NOT, ZERO_WHO, ZERO_WHERE, ONE_WHO, ONE_WHERE, WHO, WHERE, col_rec, row_rec)
		self.add(ERASE, ZERO_WHO, ZERO_WHERE, ONE_WHO, ONE_WHERE, WHO, WHERE, col_rec)

# 2 bits basis
class DisplayTex3(WhiteScene):
	def construct(self):
		t0 = self._tex("\\ket{0}_2=\\ket{00}=\\begin{bmatrix} 1 \\\\ 0 \\\\ 0 \\\\ 0 \\end{bmatrix}").move_to(1.4*UP   + 2.5*LEFT )
		t1 = self._tex("\\ket{1}_2=\\ket{01}=\\begin{bmatrix} 0 \\\\ 1 \\\\ 0 \\\\ 0 \\end{bmatrix}").move_to(1.4*UP   + 2.5*RIGHT)
		t2 = self._tex("\\ket{2}_2=\\ket{10}=\\begin{bmatrix} 0 \\\\ 0 \\\\ 1 \\\\ 0 \\end{bmatrix}").move_to(1.4*DOWN + 2.5*LEFT )
		t3 = self._tex("\\ket{3}_2=\\ket{11}=\\begin{bmatrix} 0 \\\\ 0 \\\\ 0 \\\\ 1 \\end{bmatrix}").move_to(1.4*DOWN + 2.5*RIGHT)

		self.add(t0, t1, t2, t3)

# different colors for different letters
class DisplayTex4(WhiteScene):
	def construct(self):
		s = self._tex("C_{", "i", "j", "}\\ket{x_{n-1} \\hdots x_1 x_0}")
		s[1].set_color(RED)
		s[2].set_color(BLUE)

		# s = self._tex("X", "\\ket{+}", " = X \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix} = (", "1", ") ", "\\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix}")
		# s = self._tex("X", "\\ket{-}", " = X \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ -1 \\end{bmatrix} = (", "-1", ") ", "\\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ -1 \\end{bmatrix}")
		# s = self._tex("Z", "\\ket{0}", " = Z \\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix} = (", "1", ") ", "\\begin{bmatrix} 1 \\\\ 0 \\end{bmatrix}")
		# s = self._tex("Z", "\\ket{1}", " = Z \\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix} = (", "-1", ") ", "\\begin{bmatrix} 0 \\\\ 1 \\end{bmatrix}")
		# s = self._tex("\\sqrt{X}", "\\ket{+}", " = \\sqrt{X} \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix} = (", "1", ") ", "\\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ 1 \\end{bmatrix}")
		# s = self._tex("\\sqrt{X}", "\\ket{-}", " = \\sqrt{X} \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ -1 \\end{bmatrix} = (", "i", ") ", "\\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ -1 \\end{bmatrix}")
		# s = self._tex("Y", "\\ket{y_{+}}", " = Y \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ i \\end{bmatrix} = (", "1", ") ", "\\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ i \\end{bmatrix}")
		# s = self._tex("Y", "\\ket{y_{-}}", " = Y \\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ -i \\end{bmatrix} = (", "-1", ") ", "\\frac{1}{\\sqrt{2}} \\begin{bmatrix} 1 \\\\ -i \\end{bmatrix}")
		# s[1].set_color(RED)
		# s[3].set_color(BLUE)
		# s[5].set_color(RED)

		### Appendix A
		# s = self._tex("C_{1,0}\\ket{00} = \\ket{00} \\\\ C_{1,0}\\ket{01} = \\ket{01} \\\\ C_{1,0}\\ket{10} = \\ket{11} \\\\ C_{1,0}\\ket{11} = \\ket{10}")
		# # for i in (2, 7, 12, 17, 22, 27, 32, 37):
		# for i in (5, 10, 18, 23, 31, 36, 44, 49):
		# 	s[0][i  :i+1].set_color(BLUE)
		# 	s[0][i+1:i+2].set_color(RED)
		s.scale(1.5)


		# s = self._tex("\\frac{\\alpha}{2}(", "\\ket{000}", "+", "\\ket{011}", ") + \\frac{\\beta}{2}(", "\\ket{100}", "+", "\\ket{111}", ")")
		
		# for i in (1,3,5,7): # indexes to sub-tex-mobjects which are kets
		# 	s[i][1:2].set_color(BLUE)
		# 	s[i][2:3].set_color(RED)
		# 	s[i][3:4].set_color(GREEN)


		self.add(s)

class DisplayMatrix(WhiteScene):
	CONFIG = {
		## basics
		# "name": "I",
		# "values": [
		# 	[1,0],
		# 	[0,1]
		# ],
		# "name": "X",
		# "values": [
		# 	[0,1],
		# 	[1,0]
		# ],
		# "name": "Z",
		# "values": [
		# 	[1,0],
		# 	[0,-1]
		# ],

		## Chapter 1
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

		## Chapter 2
		# "name": "SWAP",
		# "values": [
		# 	[1,0,0,0],
		# 	[0,0,1,0],
		# 	[0,1,0,0],
		# 	[0,0,0,1],
		# ],
		# "name": "", # SWAP - I
		# "values": [
		# 	[1,'','',0],
		# 	['','','',''],
		# 	['','','',''],
		# 	[0,'','',1],
		# ],
		# "name": "", # SWAP - X
		# "values": [
		# 	['','','',''],
		# 	['',0,1,''],
		# 	['',1,0,''],
		# 	['','','',''],
		# ],

		# "name": "C_{01}",
		# "values": [
		# 	[1,0,0,0],
		# 	[0,0,0,1],
		# 	[0,0,1,0],
		# 	[0,1,0,0],
		# ],
		# "name": "C_{01}-I",
		# "values": [
		# 	[1,'',0,''],
		# 	['','','',''],
		# 	[0,'',1,''],
		# 	['','','',''],
		# ],
		# "name": "C_{01}-X",
		# "values": [
		# 	['','','',''],
		# 	['',0,'',1],
		# 	['','','',''],
		# 	['',1,'',0],
		# ],
		# "name": "C_{10}",
		# "values": [
		# 	[1,0,0,0],
		# 	[0,1,0,0],
		# 	[0,0,0,1],
		# 	[0,0,1,0],
		# ],
		# "scale": 1.3,

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
		# 	[1,0,0,0,0,0,0,0], # 000
		# 	[0,1,0,0,0,0,0,0], # 001
		# 	[0,0,0,1,0,0,0,0], # 010
		# 	[0,0,1,0,0,0,0,0], # 011
		# 	[0,0,0,0,0,1,0,0], # 100
		# 	[0,0,0,0,1,0,0,0], # 101
		# 	[0,0,0,0,0,0,0,1], # 110
		# 	[0,0,0,0,0,0,1,0], # 111
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
		# "scale": 1,

		# kronecker product
		# "name": "A \\otimes B",
		# "values": [
		# 	["a_{00} B","a_{01} B"],
		# 	["a_{10} B","a_{11} B"],
		# ],
		# "scale": 1.3,

		## Chapter 3
		# "name": "H",
		# "values": [
		# 	[1,1],
		# 	[1,-1]
		# ],
		# "factor": "\\frac{1}{\\sqrt{2}}",
		# "scale": 1.5,

		### chapter 7
		"name": "H^{(2)}",
		"values": [
			[1, 1, 1, 1],
			[1,-1, 1,-1],
			[1, 1,-1,-1],
			[1,-1,-1, 1],
		],
		"factor": "\\frac{1}{2}",
		"scale": 1.2,

		### chapter 8
		# "name": "P",
		# "values": [
		# 	["a","b"],
		# 	["c","d"]
		# ],
		# "name": "P^{-1}",
		# "values": [
		# 	["d","-b"],
		# 	["-c","a"]
		# ],
		# "factor": "\\frac{1}{ad-bc}",

		## Appendix B
		# "name": "X_{1} Z_{0}",
		# "values": [
		# 		[0, 0, 1, 0],
		# 		[0, 0, 0,-1],
		# 		[1, 0, 0, 0],
		# 		[0,-1, 0, 0],
		# ],

		# "name": "X_{diagonal}",
		# "values": [
		# 	[1,0],
		# 	[0,-1]
		# ],
		# "subscript": "\\{\\ket{+},\\ket{-}\\}",

		## Appendix C
		# "name": "M",
		# "values": [
		# 	["m_{00}","m_{01}"],
		# 	["m_{10}","m_{11}"]
		# ],
		# "name": "\\alpha I + \\beta X + \\gamma Y + \\delta Z",
		# "values": [
		# 	["\\alpha + \\delta","\\beta - i \\gamma"],
		# 	["\\beta + i \\gamma","\\alpha - \\delta"]
		# ],

		# "name": "Sqrt\\ X",
		# "name": "\\sqrt{X}",
		# "values": [
		# 	["1+i","1-i"],
		# 	["1-i","1+i"]
		# ],
		# "name": "Sqrt\\ X",
		# "values": [
		# 	[1+1j,1-1j],
		# 	[1-1j,1+1j]
		# ],
		# "factor": "\\frac{1}{\\sqrt{2}}",

		# "name": "Phase(\\theta)",
		# "values": [
		# 	[1,0],
		# 	[0,"e^{i \\theta}"]
		# ],
		# "name": "Phase",
		# "values": [
		# 	[1,0],
		# 	[0,"e^{i\\theta}"]
		# ],

		## Appendix I
		# "name": "P",
		# "values": [
		# 	["1","-i"],
		# 	["i","-1"],
		# ],
		# "factor": "\\frac{1}{\\sqrt{2}}",
		# "scale": 1.3,

		## Other
		# "name": "U^2",
		# "values": [
		# 	["(\\lambda_{1})^{2}",0],
		# 	[0,"(\\lambda_{2})^{2}"]
		# ],
		
		
		# "factor": "\\frac{1}{\\sqrt{2}}",
		# "factor": "\\frac{1}{2}",

		# "subscript": "\\{U \\  basis\\}"
		# "subscript": "\\{\\ket{+},\\ket{-}\\}",
	}

	def construct(self):
		m = ' \\\\ '.join(
			' & '.join(str(i) for i in row)
			for row in self.values
		)

		# "\\begin{bmatrix} a_1 \\\\ a_2 \\end{bmatrix} \\otimes \\begin{bmatrix} b_1 \\\\ b_2 \\end{bmatrix} = \\begin{bmatrix} a_1 b_1 \\\\ a_1 b_2 \\\\ a_2 b_1 \\\\ a_2 b_2 \\end{bmatrix}",

		factor = getattr(self, "factor", "")

		s = f"{self.name} = {factor} \\begin{{bmatrix}} {m} \\end{{bmatrix}}"

		if hasattr(self, "subscript"):
			s += '_{%s}' % self.subscript

		print(s)

		scale = getattr(self, "scale", 2)

		self.add_tex(s, scale=scale)
		# self.add_tex(s, scale=None)

# dashed lines seperating a matrix
class DisplayMatrix2(WhiteScene):
	def construct(self):
		a = self._tex("C_{10} = \\begin{bmatrix} 1 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 0 & 0 & 1 & 0 \\end{bmatrix} = \\begin{bmatrix} I & 0 \\\\ 0 & X \\end{bmatrix}")
		a.scale(1.5)

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
class DisplayMatrix3(WhiteScene):
	def construct(self):
		# a = self._tex("I_1 \\otimes X_0 = \\begin{bmatrix} 1 & 0 \\\\ 0 & 1 \\end{bmatrix} \\otimes X_0 = \\begin{bmatrix} 1 \\cdot X_0 & 0 \\cdot X_0 \\\\ 0 \\cdot X_0 & 1 \\cdot X_0 \\end{bmatrix} = \\begin{bmatrix} 0 & 1 & 0 & 0 \\\\ 1 & 0 & 0 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 0 & 0 & 1 & 0 \\end{bmatrix} = \\begin{bmatrix} X & 0 \\\\ 0 & X \\end{bmatrix}")
		a = self._tex("X_1 \\otimes I_0 = \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} \\otimes I_0 = \\begin{bmatrix} 0 \\cdot I_0 & 1 \\cdot I_0 \\\\ 1 \\cdot I_0 & 0 \\cdot I_0 \\end{bmatrix} = \\begin{bmatrix} 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & 1 \\\\ 1 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\end{bmatrix} = \\begin{bmatrix} 0 & I \\\\ I & 0 \\end{bmatrix}")
		# a = self._tex("X_1 \\otimes Z_0 = \\begin{bmatrix} 0 & 1 \\\\ 1 & 0 \\end{bmatrix} \\otimes Z_0 = \\begin{bmatrix} 0 \\cdot Z_0 & 1 \\cdot Z_0 \\\\ 1 \\cdot Z_0 & 0 \\cdot Z_0 \\end{bmatrix} = \\begin{bmatrix} 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & -1 \\\\ 1 & 0 & 0 & 0 \\\\ 0 & -1 & 0 & 0 \\end{bmatrix} = \\begin{bmatrix} 0 & Z \\\\ Z & 0 \\end{bmatrix}")
		a.scale(0.6)

		l1 = DashedLine(
			start=1*DOWN + 1.7*RIGHT + 0.4*RIGHT,
			end=1*UP + 1.7*RIGHT + 0.4*RIGHT,
		).set_color(RED)

		l2 = DashedLine(
			start=2.7*RIGHT + 0.4*RIGHT + 0.2*RIGHT,
			end=0.6*RIGHT + 0.4*RIGHT + 0.1*LEFT,
		).set_color(RED)

		l1.scale(0.8)
		l2.scale(0.8)


		l1.shift(0.15*RIGHT)
		l2.shift(0.15*RIGHT)
		

		self.add(a, l1, l2)
		# self.add(a, b, TWO_WHO, c, ONE_WHERE)

# trying to automate the who-goes-where
class DisplayMatrix4(WhiteScene):
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
		a = self._tex(s)
		a.scale(1.5)

		self.add_col_rectangle(0, "\\ket{00}")
		self.add_row_rectangle(0, "\\ket{00}")

		# self.add_col_rectangle(1, "\\ket{01}")
		# self.add_row_rectangle(2, "\\ket{10}")

		# self.add_col_rectangle(2)
		# self.add_row_rectangle(1)
		# self.add_row_rectangle(1, "\\ket{01}")

		# self.add_col_rectangle(3)
		# self.add_row_rectangle(3)


		self.add(a)

	def add_row_rectangle(self, rownum, name=True):
		r = Rectangle(
			width=len(self.values)+0.7,
			height=0.8,
		)
		r.set_color(RED)

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
			n.set_color(RED)

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
		r.set_color(BLUE)

		# center the rectangle around the left-most column
		r.shift(0.15*RIGHT)

		# shift according to the column
		r.shift(colnum*1.1*RIGHT)

		self.add(r)

		if name is True:
			name = self._generate_name(colnum)
		if name:
			n = TexMobject(name)
			n.set_color(BLUE)

			n.shift(2.4*UP)
			n.shift(0.15*RIGHT)
			n.shift(colnum*1.1*RIGHT)
			
			self.add(n)

		return r

	def _generate_name(self, value):
		l = int(np.log2(len(self.values)))
		return "\\ket{%s}" % bin(value)[2:].zfill(l)

# showing a matrix with multiple names
class DisplayMatrix5(WhiteScene):
	def construct(self):
		# self.add_tex(
		# 	"C^{Z}_{10} = \\begin{bmatrix} I & 0 \\\\ 0 & Z \\end{bmatrix} = \\begin{bmatrix} 1 & 0 & 0 & 0 \\\\ 0 & 1 & 0 & 0 \\\\ 0 & 0 & 1 & 0 \\\\ 0 & 0 & 0 & -1 \\end{bmatrix} = C^{Z}_{01}",
		# 	# scale=1.3
		# )

		self.add_tex("\\sigma_{Y} = Y = \\begin{bmatrix} 0 & -i \\\\ i & 0 \\end{bmatrix}", scale=1.3)
		# self.add_tex("\\sigma_{Z} = Z = \\begin{bmatrix} 1 & 0 \\\\ 0 & -1 \\end{bmatrix}", scale=1.3)

# showing two equal matrices
class DisplayMatrix6(WhiteScene):
	def construct(self):
		values = [
			["a_{00} B","a_{01} B"],
			["a_{10} B","a_{11} B"],
		]
		m1 = ' \\\\ '.join(
			' & '.join(str(i) for i in row)
			for row in values
		)

		values = [
			["a_{00} b_{00}","a_{00} b_{01}","a_{01} b_{00}","a_{01} b_{01}"],
			["a_{00} b_{10}","a_{00} b_{11}","a_{01} b_{10}","a_{01} b_{11}"],
			["a_{10} b_{00}","a_{10} b_{01}","a_{11} b_{00}","a_{11} b_{01}"],
			["a_{10} b_{10}","a_{10} b_{11}","a_{11} b_{10}","a_{11} b_{11}"],
		]
		m2 = ' \\\\ '.join(
			' & '.join(str(i) for i in row)
			for row in values
		)

		name = "A \\otimes B"

		matrices = [m1, m2]

		s = name
		for m in matrices:
			s += f" = \\begin{{bmatrix}} {m} \\end{{bmatrix}}"
		
		# self.add_tex(s, scale=0.7)
		self.add_tex(s, scale=1)

# showing 2 equal matrices
class DisplayMatrix7(WhiteScene):
	def construct(self):
		self.add_tex("Phase(\\theta) = \\begin{bmatrix} 1 & 0 \\\\ 0 & e^{i\\theta} \\end{bmatrix} = e^{i\\frac{\\theta}{2}} \\begin{bmatrix} e^{-i\\frac{\\theta}{2}} & 0 \\\\ 0 & e^{i\\frac{\\theta}{2}} \\end{bmatrix}", scale=1.3)

class DisplayMatrix8(WhiteScene):
	CONFIG = {
		# "gate_name": "X",
		"gate_name": "X_{1} Z_{0}",
		# "bits": 1,
		"bits": 2,
	}
	def construct(self):
		rows = []
		for row in range(0, 2**self.bits):
			columns = []
			for column in range(0, 2**self.bits):
				s = f"\\bra{{{self.bin(row)}}}{self.gate_name}\\ket{{{self.bin(column)}}}"
				columns.append(s)
			rows.append(" & ".join(columns))
		m = " \\\\ ".join(rows)

		matrix = f"\\begin{{bmatrix}} {m} \\end{{bmatrix}}"
		print(matrix)

		self.add_tex(matrix, scale=None)

	def bin(self, n):
		return bin(n)[2:].zfill(self.bits)


class BellStateSimilarityToGHZState(WhiteScene):
	def construct(self):
		s1 = self._tex("\\frac{\\ket{000} + \\ket{111}}{\\sqrt{2}}", background_stroke_width=0)
		s2 = self._tex("\\frac{\\ket{000} - \\ket{111}}{\\sqrt{2}}", background_stroke_width=0)
		s3 = self._tex("\\frac{\\ket{011} + \\ket{100}}{\\sqrt{2}}", background_stroke_width=0)
		s4 = self._tex("\\frac{\\ket{011} - \\ket{100}}{\\sqrt{2}}", background_stroke_width=0)
		ss = [s1, s2, s3, s4]
		self.place_in_grid(ss, 2, 2)

		for s in ss:
			s[0][1:2].set_color(BLUE)
			s[0][2:3].set_color(RED)
			s[0][3:4].set_color(WHITE)

			s[0][7:8].set_color(BLUE)
			s[0][8:9].set_color(RED)
			s[0][9:10].set_color(WHITE)

		self.add(*ss)
		self.wait()

		self.play(
			s1[0][3:4 ].set_color, RED,
			s1[0][9:10].set_color, RED,
			s2[0][3:4 ].set_color, RED,
			s2[0][9:10].set_color, RED,
			s3[0][3:4 ].set_color, RED,
			s3[0][9:10].set_color, RED,
			s4[0][3:4 ].set_color, RED,
			s4[0][9:10].set_color, RED,
		)

		self.wait()

	HEIGHT_LIMIT = 3
	WIDTH_LIMIT = 5
	def place_in_grid(self, l, rows, columns):
		width_spacing = self.WIDTH_LIMIT * 2 / (columns+1)
		column_locations = [
			-self.WIDTH_LIMIT + (i+1) * width_spacing
			for i in range(columns)
		]

		height_spacing = self.HEIGHT_LIMIT * 2 / (rows+1)
		row_locations = [
			-self.HEIGHT_LIMIT + (i+1) * height_spacing
			for i in range(rows)
		]


		for ri, r in enumerate(row_locations):
			for ci, c in enumerate(column_locations):
				l[ri*columns + ci].move_to(r*DOWN + c*RIGHT)
