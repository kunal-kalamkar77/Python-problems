# Problem statement - Create a program to generate random number
import random

def random_int(lower=1, upper=100):
	"""Return a random integer in [lower, upper]."""
	return random.randint(lower, upper)

if __name__ == "__main__":
	print("Random integer (1-100):", random_int(1, 100))
