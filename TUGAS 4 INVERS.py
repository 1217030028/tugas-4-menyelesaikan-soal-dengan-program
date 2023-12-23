import numpy as np

# Matriks B
B = np.array([[10, -22],
              [3, 45]])

# Invers matriks B
invers_B = np.linalg.inv(B)

print("Invers matriks B:")
print(invers_B)
