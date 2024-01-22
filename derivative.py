import sympy as sp
import numpy as np

# Define the variable and the function
y = sp.symbols('y')
A = sp.symbols('A')
B = sp.symbols('B')
C = sp.symbols('C')

f = (sp.acos(y/A)-B)/C

# Calculate the derivative
df_dy = sp.diff(f, y)
df_dA = sp.diff(f, A)
df_dB = sp.diff(f, B)
df_dC = sp.diff(f, C)

# Print the result
print("Original function:", f)
print("Derivative in y:", df_dy)
print("Derivative in A:", df_dA)
print("Derivative in B:", df_dB)
print("Derivative in C:", df_dC)