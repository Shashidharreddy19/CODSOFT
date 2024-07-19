def calculator():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    operation = input("Enter operation (+, -, *, /): ")

    if operation == '+':
        print(num1 + num2)
    elif operation == '-':
        print(num1 - num2)
    elif operation == '*':
        print(num1 * num2)
    elif operation == '/':
        if num2 != 0:
            print(num1 / num2)
        else:
            print("Cannot divide by zero")
    else:
        print("Invalid operation")

def calculator2():
    expression = input("Enter an expression: ")
    try:
        result = eval(expression)
        print(result)
    except Exception as e:
        print(f"Error evaluating expression: {e}")

def main():
    intro_message = (
        "Welcome to the calculator! Choose between two calculators:\n"
        "1. Calculator with separate arguments\n"
        "2. Calculator with an expression\n"
        "Press 'q' to quit.\n"
    )
    print(intro_message)

    while True:
        choice = input("Which calculator do you want to use? (1 / 2). Press 'q' to quit: ").strip()
        if choice == '1':
            calculator()
        elif choice == '2':
            calculator2()
        elif choice == 'q':
            break
        else:
            print("Please enter a valid option.")

    rating = int(input("Rate this app from 1 to 10: "))
    review = input("Enter your review: ")
    name = input("Enter your name: ")

    with open('user_reviews.txt', 'a') as file:
        file.write(f"Name: {name}, Rating: {rating}, Review: {review}\n")
    print('Thanks for your review!')

if __name__ == "__main__":
    main()
