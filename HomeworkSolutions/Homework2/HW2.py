import numpy as np

H=np.array([[4,-4],[-4,3]])
E=np.linalg.eigvals(H)
print(E)
