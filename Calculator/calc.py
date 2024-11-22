def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y

def power(x, y):
    return x ** y

def modulus(x, y):
    return x % y

def floor_division(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x // y

def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_operation():
    operations = ["+", "-", "*", "/", "**", "%", "//"]
    while True:
        op = input("Choose an operation (+, -, *, /, **, %, //): ")
        if op in operations:
            return op
        print("Invalid operation. Please choose from +, -, *, /, **, %, //.")

a = get_number("Enter the first number: ")
b = get_number("Enter the second number: ")
c = get_operation()

if c == "+":
    print("Result:", add(a, b))
elif c == "-":
    print("Result:", subtract(a, b))
elif c == "*":
    print("Result:", multiply(a, b))
elif c == "/":
    print("Result:", divide(a, b))
elif c == "**":
    print("Result:", power(a, b))
elif c == "%":
    print("Result:", modulus(a, b))
elif c == "//":
    print("Result:", floor_division(a, b))
else:
    print("Invalid operation")