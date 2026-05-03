# Gauss Elimination Method
# Solve system of linear equations: Ax = B

# System of equations:
# 2x + y + z = 8
# -3x - y + 2z = -11
# -2x + y + 2z = -3

# Coefficient matrix (3x3)
A = [
    [2, 1, 1],
    [-3, -1, 2],
    [-2, 1, 2]
]

# Constant matrix (B)
B = [8, -11, -3]

n = 3

print("=== GAUSS ELIMINATION METHOD ===")
print("\nSystem of equations:")
print("2x + y + z = 8")
print("-3x - y + 2z = -11")
print("-2x + y + 2z = -3")

# Create augmented matrix
print("\nAugmented Matrix:")
for i in range(n):
    print(f"[{A[i][0]}, {A[i][1]}, {A[i][2]} | {B[i]}]")

# Forward Elimination
print("\n--- FORWARD ELIMINATION ---")

for i in range(n):
    # Find pivot
    max_row = i
    for k in range(i + 1, n):
        if abs(A[k][i]) > abs(A[max_row][i]):
            max_row = k
    
    # Swap rows
    A[i], A[max_row] = A[max_row], A[i]
    B[i], B[max_row] = B[max_row], B[i]
    
    # Make all rows below this one 0 in current column
    for k in range(i + 1, n):
        if A[i][i] != 0:
            c = A[k][i] / A[i][i]
            for j in range(i, n):
                if i == j:
                    A[k][j] = 0
                else:
                    A[k][j] = A[k][j] - c * A[i][j]
            B[k] = B[k] - c * B[i]

print("\nUpper Triangular Matrix:")
for i in range(n):
    print(f"[{A[i][0]:.4f}, {A[i][1]:.4f}, {A[i][2]:.4f} | {B[i]:.4f}]")

# Back Substitution
print("\n--- BACK SUBSTITUTION ---")

x = [0 for _ in range(n)]

for i in range(n - 1, -1, -1):
    x[i] = B[i]
    for j in range(i + 1, n):
        x[i] = x[i] - A[i][j] * x[j]
    x[i] = x[i] / A[i][i]

# Results
print("\n" + "=" * 50)
print("Solution:")
print(f"x = {x[0]:.6f}")
print(f"y = {x[1]:.6f}")
print(f"z = {x[2]:.6f}")
