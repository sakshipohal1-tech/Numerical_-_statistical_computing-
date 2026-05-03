# Bisection Method
# Find root of f(x) = x^3 - 5*x + 1

# Function definition
def f(x):
    return x**3 - 5*x + 1

# Initial values
a = 0
b = 1
tolerance = 0.001
iteration = 0

print("=== BISECTION METHOD ===")
print("Function: f(x) = x^3 - 5*x + 1")
print("\nIteration | a | b | c | f(c) | Error")
print("-" * 50)

# Bisection process
while abs(b - a) > tolerance:
    iteration = iteration + 1
    c = (a + b) / 2
    f_c = f(c)
    error = abs(b - a)
    
    print(f"{iteration:9d} | {a:.4f} | {b:.4f} | {c:.4f} | {f_c:.4f} | {error:.4f}")
    
    if f(a) * f_c < 0:
        b = c
    else:
        a = c

# Final result
c = (a + b) / 2
print("\n" + "=" * 50)
print(f"Root found after {iteration} iterations")
print(f"Approximate root: {c:.6f}")
print(f"f({c:.6f}) = {f(c):.6f}")
