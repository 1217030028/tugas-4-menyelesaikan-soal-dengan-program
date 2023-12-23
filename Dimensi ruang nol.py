import numpy as np
from scipy.linalg import null_space

# Matriks C
C = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# Mencari ruang nol dari matriks C
null_space_C = null_space(C)

# Dimensi ruang nol C
dimensi_ruang_nol_C = null_space_C.shape[1]

print("Dimensi ruang nol matriks C:", dimensi_ruang_nol_C)
