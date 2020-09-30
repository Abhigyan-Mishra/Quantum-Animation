from manimlib.imports import *

OUTPUT_DIRECTORY = "wave"

class TestWave(Scene):
	CONFIG = {
		'n': 20, # there will be 2n+1 particles
	}
	def construct(self):
		self.wait(0.2)

		wave = Wave(
			n=self.n,
			omega=2,
		)

		# bars = wave.get_bars()
		# self.add(*bars)
		
		wave.particles[self.n].set_color(GREEN)

		# show the particles
		self.add(wave.particles)
		self.wait(2)

		wave.resume_updating()
		self.wait(3)

		# slowly add the rest
		for i in wave.color_particles_from_center():
			self.wait(2 - 0.075*i)

		# let it play a bit more
		self.wait(10)


class Test(Scene):
	CONFIG = {
		'n': 20, # there will be 2n+1 particles
	}
	def construct(self):
		self.wait(0.2)
		bar_top = Line(1*UP   + 10*RIGHT, 1*UP   + 10*LEFT)
		bar_bot = Line(1*DOWN + 10*RIGHT, 1*DOWN + 10*LEFT)
		self.add(bar_bot, bar_top)

		particles = [
			WaveParticle(
				point=ORIGIN + i*RIGHT*0.25,
				omega=1,
				phase=0 + i*10*DEGREES,
				amplitude=1,
			).set_color(BLACK)
			for i in range(-self.n, self.n+1)
		]

		particles[self.n].set_color(GREEN)

		self.add(*particles)

		# show the particles
		self.wait(2)

		# let the particles play
		# though, only the middle one will be shown
		for x in particles:
			x.add_updater(x.__class__.wave)

		self.wait(3)

		# slowly add the rest
		for i in range(self.n):
			particles[self.n-i-1].set_color(WHITE)
			particles[self.n+i+1].set_color(WHITE)
			self.wait(2 - 0.075*i)

		# let it play a bit more
		self.wait(10)
