# Simple Calculator
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Cannot divide by zero"
    return a / b


print("------ Simple Calculator ------")
print("Made by Md Shahid")

while True:
    try:
        # Take input
        num1 = float(input("\nEnter first number: "))
        num2 = float(input("Enter second number: "))

        # Menu
        print("\nChoose operation:")
        print("1. Addition (+)")
        print("2. Subtraction (-)")
        print("3. Multiplication (*)")
        print("4. Division (/)")

        choice = input("Enter choice (1/2/3/4): ")

        # Perform operation
        if choice == "1":
            print("Result:", add(num1, num2))

        elif choice == "2":
            print("Result:", subtract(num1, num2))

        elif choice == "3":
            print("Result:", multiply(num1, num2))

        elif choice == "4":
            print("Result:", divide(num1, num2))

        else:
            print("Invalid choice!")

        # Continue or stop
        again = input("\nDo you want to calculate again? (yes/no): ")

        if again.lower() != "yes":
            print("Calculator Closed.")
            break

    except ValueError:
        print("Invalid input! Please enter numbers only.")

