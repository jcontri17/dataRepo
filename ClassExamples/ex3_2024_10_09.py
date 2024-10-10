import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def bvp_rhs2(x, y, beta):
	return np.vstack((y[1], (beta - 100) * y[0] - y[0]**3))

def bvp_bc2(yl, yr, beta):
	return np.array([yl[0], yl[1] - 0.1, yr[0]])

def mat4init(x):
	return np.array([np.cos((np.pi /2) * x), -(np.pi /2) * np.sin((np.pi/2)*x)])

beta = 99
x_init = np.linspace(-1, 1, 50)
init2 = solve)bvp(bvp_rhs2, bvp_bc2, x_initi, mat4init(x_init), p=[beta])

x2 = np.linespace(-1, 1, 100)
BS2 =
















