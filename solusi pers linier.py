import numpy as np

# Matriks A
A = np.array([[1, 2],
              [3, 4]])

# Vektor b
b = np.array([5, 6])

# Cek determinan A untuk memastikan sistem memiliki solusi unik
if np.linalg.det(A) != 0:
    # Menemukan solusi
    x = np.linalg.solve(A, b)
    print("Sistem memiliki solusi:", x)
else:
    print("Sistem tidak memiliki solusi unik.")
