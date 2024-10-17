def add(x, y):
    """Add two numbers."""
    return x + y

def subtract(x, y):
    """Subtract two numbers."""
    return x - y

def multiply(x, y):
    """Multiply two numbers."""
    return x * y

def divide(x, y):
    """Divide two numbers."""
    if y == 0:
        raise ValueError("Cannot divide by zero!")
    return x / y

# Main program
def main():
    operations = {
        '1': add,
        '2': subtract,
        '3': multiply,
        '4': divide
    }
    print("Select any operation from below:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    while True:
        choice = input("Enter your choice (1/2/3/4): ")
        if choice in operations:
            try:
                num1 = float(input("Enter your first number: "))
                num2 = float(input("Enter your second number: "))
                result = operations[choice](num1, num2)
                print(f"The result for input is: {result}")
            except ValueError as e:
                print(f"Invalid input: {e}")
            if input("Let's do next calculation? (yes/no): ").lower() == 'no':
                break
        else:
            print("Invalid input. Please try again.")

if __name__ == "__main__":
    main()
    