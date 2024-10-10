import numpy as np
from scipy.integrate import solve_bvp
import matplotlib.pyplot as plt

def bvp_rhs(x,y):
	return np.vstack((y[1], 5 - 3*y[1] - 6*y[0]))

#left BC first, right BC second
def bvp_bc(ya,yb):
	return np.array([ya[0] - 3, yb[0] +2*yb[1] - 5])

#define initial mesh and guess
x_init = np.linspace(1, 3, 10)
y_init = np.zeros((2, x_init.size))

#solve the BV problem
sol = solve_bvp(bvp_rhs, bvp_bc, x_init, y_init)

#Evaluate the solution at a finer mesh
x_eval = np.linspace(1, 3, 100)
BS = sol.sol(x_eval)
plt.plot(x_eval, BS[0])
plt.xlabel('x')
plt.ylabel('BS[1]')
plt.title('Solution Plot')
plt.grid(True)
plt.show()











