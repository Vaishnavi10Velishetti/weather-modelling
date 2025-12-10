# Quadratic equation values
a = 1
b = -3
c = 2

# Calculate discriminant
discriminant = b**2 - 4*a*c

print("Quadratic Equation: {}x^2 + {}x + {}".format(a, b, c))
print("Discriminant:", discriminant)

# Check real roots
if discriminant >= 0:
    root1 = (-b + discriminant**0.5) / (2*a)
    root2 = (-b - discriminant**0.5) / (2*a)
    print("Real Roots:")
    print("Root 1:", root1)
    print("Root 2:", root2)

    # Generate values instead of plotting
    print("\nX and Y values of the quadratic (from -4 to 4):")
    for x in range(-4, 5):
        y = a*(x**2) + b*x + c
        print(f"x={x}, y={y}")

else:
    print("No real roots. Cannot generate graph data.")
