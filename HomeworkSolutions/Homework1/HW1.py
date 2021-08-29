import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

from scipy.optimize import minimize
from scipy.optimize import LinearConstraint
from scipy.optimize import Bounds

givenfun = lambda x: ((x[0]-x[1])**2+(x[1]+x[2]-2)**2+(x[3])**2+(x[4]-1)**2)

cons = ({'type': 'eq', 'fun': lambda x: x[0] + 3*x[1]},
        {'type': 'eq', 'fun': lambda x: x[2] + x[3] - 2*x[4]},
        {'type': 'eq', 'fun': lambda x: x[1] - x[4]})

bnds = ((-10, 10), (-10, 10), (-10, 10), (-10, 10), (-10, 10))
x0=(1,1,1,1,1)
res = minimize(givenfun, x0, method='SLSQP',
               bounds=bnds,constraints=cons)
print(res.x)
