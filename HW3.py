import numpy as np
from scipy.sparse import csr_matrix
from scipy.sparse.linalg import spsolve
from scipy.sparse import spdiags

def jacobi(a, b, k):
    n = len(b)  # find n
    d = np.diag(a)  # extract diagonal of a
    l = np.tril(a)
    u = np.triu(a)
    r = a - np.diag(d)  # remainder matrix
    x = np.zeros(n)  # initialize x

    for _ in range(k):  # Jacobi iterations
        x = (b - r @ x) / d

    return x

#Problem 2
n = 100
A = (np.diag([2]*n) + np.diag([1]*(n-1), k=1) + np.diag([1]*(n-1), k=-1))
a_sparse = csr_matrix(A)
b = np.zeros(n)
b[0] = 1
b[n-1] = -1
x_exact = np.ones(n)
x_exact[1::2] = -1
tol = 5e-4
result = jacobi(a_sparse, b, 50)
error = np.max(np.abs(result - x_exact))



#Problem 3
def SOR(a, b, k):
    a_sparse = csr_matrix(a)
    w = 1.25
    n = len(b)  # find n
    d = spdiags(np.diag(a), 0, n, n)  # extract diagonal of a
    l = np.tril(a_sparse) - d
    u = np.triu(a_sparse) - d
    x = np.zeros(n)  # initialize x
    
    for _ in range(k):  # Jacobi iterations
        x = spsolve(w*l + d, (((1 - w)*d) + w*u)@x + w*b)

    return x
