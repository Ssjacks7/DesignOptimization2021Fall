# This code minimizes the given function when bound by the given constraints
# (See Homework 1) using a variety of different initial conditions. The results
# of the minimized functions are then displayed and the results are compared.

# Sam Jackson, MAE 494, HW1

# Importing optimize
from scipy.optimize import minimize

# Defining the given function to be optimized
givenfun = lambda x: ((x[0]-x[1])**2+(x[1]+x[2]-2)**2+(x[3])**2+(x[4]-1)**2)

# Defining the given constraints that the function should be optimized under
cons = ({'type': 'eq', 'fun': lambda x: x[0] + 3*x[1]},
        {'type': 'eq', 'fun': lambda x: x[2] + x[3] - 2*x[4]},
        {'type': 'eq', 'fun': lambda x: x[1] - x[4]})
bnds = ((-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10))

# Defining the initial guesses given to the minimize functions
# These were chosen arbitrarily and are the same for all x's for convenience
x0a=(1, 1, 1, 1, 1)
x0b=(-1, -1, -1, -1, -1)
x0c=(100, 100, 100, 100, 100)
x0d=(-100, -100, -100, -100, -100)

# Plugging all of the above into the minimize functions and using SLSQP method
resa = minimize(givenfun, x0a, method='SLSQP', bounds=bnds, constraints=cons)
resb = minimize(givenfun, x0b, method='SLSQP', bounds=bnds, constraints=cons)
resc = minimize(givenfun, x0c, method='SLSQP', bounds=bnds, constraints=cons)
resd = minimize(givenfun, x0d, method='SLSQP', bounds=bnds, constraints=cons)

# Printing out the minimize results using the different initial guesses
print('Minimize results with all initial guesses =  1  :', resa.x)
print('Minimize results with all initial guesses = -1  :', resb.x)
print('Minimize results with all initial guesses =  100:', resc.x)
print('Minimize results with all initial guesses = -100:', resd.x)

# As we can see from the results, the choice of initial guess doesn't matter
# too much, as all results were approximately the same (~0.0001 difference).
# Though the initial guesses didn't matter for optimization for the initial
# guesses that were tried, it is still possible that there are some that
# lead to different solutions as there might be more local minimums.
