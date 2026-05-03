# Newton Forward Interpolation Method
# Find value of y at a given x using forward difference table

# Given data points
x_values = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5]
y_values = [1.0, 1.105, 1.223, 1.350, 1.492, 1.649]

# Interpolation point
x_point = 0.24

print("=== NEWTON FORWARD INTERPOLATION ===")
print("\nGiven Data Points:")
print("x: ", x_values)
print("y: ", y_values)
print(f"\nFind y at x = {x_point}")

# Calculate h (step size)
h = x_values[1] - x_values[0]

# Calculate p = (x - x0) / h
p = (x_point - x_values[0]) / h

print(f"\nStep size h = {h}")
print(f"p = ({x_point} - {x_values[0]}) / {h} = {p:.4f}")

# Create forward difference table
n = len(x_values)
diff_table = []
for i in range(n):
    diff_table.append([y_values[i]])

# Calculate forward differences
for j in range(1, n):
    for i in range(n - j):
        diff_table[i].append(diff_table[i][j-1] - diff_table[i+1][j-1])

# Display forward difference table
print("\n--- FORWARD DIFFERENCE TABLE ---")
print("x | y | ΔY | Δ²Y | Δ³Y | Δ⁴Y | Δ⁵Y")
print("-" * 60)
for i in range(n):
    row = f"{x_values[i]:.1f} |"
    for j in range(len(diff_table[i])):
        row += f" {diff_table[i][j]:.4f} |"
    print(row)

# Newton Forward Interpolation formula
# f(x) = y0 + p*Δy0 + p(p-1)/2! * Δ²y0 + p(p-1)(p-2)/3! * Δ³y0 + ...

result = y_values[0]

# First order
result = result + p * diff_table[0][1]

# Second order
result = result + (p * (p - 1) / 2) * diff_table[0][2]

# Third order
result = result + (p * (p - 1) * (p - 2) / 6) * diff_table[0][3]

# Fourth order
result = result + (p * (p - 1) * (p - 2) * (p - 3) / 24) * diff_table[0][4]

# Fifth order
result = result + (p * (p - 1) * (p - 2) * (p - 3) * (p - 4) / 120) * diff_table[0][5]

# Result
print("\n" + "=" * 60)
print("Calculation using Newton Forward Formula:")
print(f"f(0.24) = {y_values[0]:.4f}")
print(f"        + {p:.4f} * {diff_table[0][1]:.4f}")
print(f"        + {p*(p-1)/2:.6f} * {diff_table[0][2]:.4f}")
print(f"        + {p*(p-1)*(p-2)/6:.8f} * {diff_table[0][3]:.4f}")
print(f"        + {p*(p-1)*(p-2)*(p-3)/24:.10f} * {diff_table[0][4]:.4f}")
print(f"        + {p*(p-1)*(p-2)*(p-3)*(p-4)/120:.12f} * {diff_table[0][5]:.4f}")
print("\n" + "=" * 60)
print(f"Interpolated value at x = {x_point}: y = {result:.6f}")
