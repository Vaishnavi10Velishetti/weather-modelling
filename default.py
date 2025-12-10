import math

# Function to solve quadratic equation
def solve_weather_equation(a, b, c):
    discriminant = b**2 - 4*a*c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2*a)
        root2 = (-b - math.sqrt(discriminant)) / (2*a)
        return root1, root2

    elif discriminant == 0:
        root = -b / (2*a)
        return root, root

    else:
        return None


# Function to show values instead of plotting (NO matplotlib)
def plot_weather_model(a, b, c):
    print("\nWeather Model Values (x from -4 to 4):")
    for x in range(-4, 5):
        y = a*(x**2) + b*x + c
        print(f"x = {x}, y = {y}")
    print()


# ---------------- MAIN MENU ------------------

print("1. Use hard-coded quadratic equation")
print("2. Enter coefficients manually")
print("3. Read coefficients from a file")

choice = input("Enter your choice (1/2/3): ")

if choice == '1':
    a = 2
    b = -7
    c = 3
    solutions = solve_weather_equation(a, b, c)
    print("Solutions:", solutions)
    plot_weather_model(a, b, c)

elif choice == '2':
    a = float(input("Enter coefficient a: "))
    b = float(input("Enter coefficient b: "))
    c = float(input("Enter coefficient c: "))
    solutions = solve_weather_equation(a, b, c)
    print("Solutions:", solutions)
    plot_weather_model(a, b, c)

elif choice == '3':
    try:
        filename = input("Enter the file name with coefficients (e.g., coefficients.txt): ")
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                coefficients = list(map(float, line.split()))
                a, b, c = coefficients
                solutions = solve_weather_equation(a, b, c)
                print(f"Coefficients: {coefficients} -> Solutions: {solutions}")
                plot_weather_model(a, b, c)
    except FileNotFoundError:
        print("File not found. Please provide a valid file name.")

else:
    print("Invalid choice. Please select 1, 2, or 3.")
