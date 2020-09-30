import numpy as np
import matplotlib.pyplot as plt

def tests():
	X = np.linspace(0, 5, 100)
	X = np.linspace(0, 2, 1000)
	# for power in np.arange(0.25, 4.25, 0.25):
	# for power in np.arange(1, 6, 1):
	# for power in np.arange(0.25, 3.25, 0.25):
	for power in np.arange(0.5, 3.5, 0.5):
		for factor in np.arange(0.5, 2.5, 0.5):
			plt.plot(X, factor * X**(-power), label=f"${factor} \\cdot x^{{-{power}}}$")
	plt.legend()
	plt.xlabel("X")
	plt.ylabel("Force")
	plt.ylim((0, 25))
	plt.show()


def plot_separation():
	X = np.linspace(0, 2, 1000)
	for power in np.arange(0.5, 3.5, 0.5):
		for factor in np.arange(0.5, 2.5, 0.5):
			plt.plot(X, factor * X**(-power), label=f"${factor} \\cdot x^{{-{power}}}$")

	plt.legend()
	plt.xlabel("X")
	plt.ylabel("Force")
	plt.ylim((0, 25))
	plt.show()


def plot_explanation_1():
	X = np.linspace(0, 2, 1000)
	plt.plot(X, X, label=f"${1} \\cdot x^{{{1}}}$")

	plt.legend()
	plt.xlabel("X")
	plt.ylabel("Force")
	# plt.ylim((0, 25))
	plt.show()

def plot_explanation_2():
	X = np.linspace(0, 2, 1000)
	for power in np.arange(0.5, 3.5, 0.5):
		plt.plot(X, 1 * X**power, label=f"${1} \\cdot x^{{{power}}}$")

	plt.legend()
	plt.xlabel("X")
	plt.ylabel("Force")
	# plt.ylim((0, 25))
	plt.show()

def plot_explanation_3():
	X = np.linspace(0, 2, 1000)
	for factor in np.arange(0.5, 2.5, 0.5):
		plt.plot(X, factor * X**1, label=f"${factor} \\cdot x^{{{1}}}$")

	plt.legend()
	plt.xlabel("X")
	plt.ylabel("Force")
	# plt.ylim((0, 25))
	plt.show()

def plot_explanation_4():
	X = np.linspace(0, 2, 1000)
	for power in np.arange(0.5, 3.5, 0.5):
		for factor in np.arange(0.5, 2.5, 0.5):
			plt.plot(X, factor * X**power, label=f"${factor} \\cdot x^{{{power}}}$")

	plt.legend()
	plt.xlabel("X")
	plt.ylabel("Force")
	# plt.ylim((0, 25))
	plt.show()

# plot_explanation_4()
plot_separation()
