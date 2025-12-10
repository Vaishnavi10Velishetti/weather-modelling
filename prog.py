import math

# Quadratic solver function
def quadratic_solver(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check the discriminant
    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

    elif discriminant == 0:
        root = -b / (2 * a)
        return root, root

    else:
        return None


# Weather equation solver
def solve_weather_equation(a, b, c):
    solutions = quadratic_solver(a, b, c)
    return solutions


# Example usage
print(solve_weather_equation(1, -5, 6))
