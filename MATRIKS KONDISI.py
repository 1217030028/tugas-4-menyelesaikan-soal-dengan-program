import numpy as np

# Matriks C
C = np.array([[1, 1e-10],
              [1e-10, 1]])

# Hitung nilai kondisi matriks C
cond_C = np.linalg.cond(C)

print("Nilai kondisi matriks C:", cond_C)

# Menentukan apakah matriks C berkondisi buruk
if cond_C > 1e12:
    print("Matriks C berkondisi buruk.")
else:
    print("Matriks C tidak berkondisi buruk.")
