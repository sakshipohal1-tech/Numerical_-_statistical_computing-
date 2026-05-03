# Jacobi Iteration Method
# Solve system of linear equations

# System of equations:
# 10x - y - 2z = 7
# -x + 10y - 2z = 8
# -x - y + 10z = 9

# Rearranged for Jacobi:
# x = (7 + y + 2z) / 10
# y = (8 + x + 2z) / 10
# z = (9 + x + y) / 10

# Initial approximations
x = 0
y = 0
z = 0

tolerance = 0.0001
max_iterations = 20
iteration = 0

print("=== JACOBI ITERATION METHOD ===")
print("\nSystem of equations:")
print("10x - y - 2z = 7")
print("-x + 10y - 2z = 8")
print("-x - y + 10z = 9")

print("\nIteration | x | y | z | Error")
print("-" * 55)

# Jacobi iteration
for iteration in range(1, max_iterations + 1):
    # Store old values
    x_old = x
    y_old = y
    z_old = z
    
    # Calculate new values using old values (simultaneous)
    x = (7 + y_old + 2*z_old) / 10
    y = (8 + x_old + 2*z_old) / 10
    z = (9 + x_old + y_old) / 10
    
    # Calculate error
    error = max(abs(x - x_old), abs(y - y_old), abs(z - z_old))
    
    print(f"{iteration:9d} | {x:.4f} | {y:.4f} | {z:.4f} | {error:.6f}")
    
    # Check for convergence
    if error < tolerance:
        print(f"\nConverged after {iteration} iterations")
        break

# Final result
print("\n" + "=" * 55)
print("Final Solution:")
print(f"x = {x:.6f}")
print(f"y = {y:.6f}")
print(f"z = {z:.6f}")
