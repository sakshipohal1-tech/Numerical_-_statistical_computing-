# Newton-Raphson Method
# Find root of f(x) = x^3 - 5*x + 1
# Derivative: f'(x) = 3*x^2 - 5

# Function definition
def f(x):
    return x**3 - 5*x + 1

# Derivative definition
def f_prime(x):
    return 3*x**2 - 5

# Initial value
x0 = 0.5
tolerance = 0.001
iteration = 0

print("=== NEWTON-RAPHSON METHOD ===")
print("Function: f(x) = x^3 - 5*x + 1")
print("Derivative: f'(x) = 3*x^2 - 5")
print("\nIteration | x0 | f(x0) | f'(x0) | x1 | Error")
print("-" * 60)

# Newton-Raphson process
while True:
    iteration = iteration + 1
    
    f_x0 = f(x0)
    f_prime_x0 = f_prime(x0)
    
    # Newton-Raphson formula: x1 = x0 - f(x0)/f'(x0)
    x1 = x0 - f_x0 / f_prime_x0
    
    error = abs(x1 - x0)
    
    print(f"{iteration:9d} | {x0:.4f} | {f_x0:.4f} | {f_prime_x0:.4f} | {x1:.4f} | {error:.4f}")
    
    if error < tolerance:
        break
    
    x0 = x1

# Final result
print("\n" + "=" * 60)
print(f"Root found after {iteration} iterations")
print(f"Approximate root: {x1:.6f}")
print(f"f({x1:.6f}) = {f(x1):.6f}")
