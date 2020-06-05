# Problem 9
# Finding Singular values of Matrix

import numpy as np

# defining matrix
A=np.array([[2,1],[1,0],[0,1]])
B=np.array([[1,1,0],[1,0,1],[0,1,1]])

# performing SVD decomposition
ua,sa,va=np.linalg.svd(A)
ub,sb,vb=np.linalg.svd(B,hermitian=True)

# printing output
print("Singular values of matrix \n 2 1\n 1 0 \n 0 1 \n:")
print(sa)
print("Singular values of matrix \n 1 1 0\n 1 0 1 \n 0 0 1 \n :")
print(sb)
