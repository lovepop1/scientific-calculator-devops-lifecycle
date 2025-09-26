import math

def square_root():
    """Calculates the square root of a number."""
    try:
        num = float(input("Enter a number to find its square root: "))
        if num < 0:
            print("Error: Cannot calculate the square root of a negative number.")
        else:
            result = math.sqrt(num)
            print(f"The square root of {num} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def factorial():
    """Calculates the factorial of a number."""
    try:
        num = int(input("Enter a non-negative integer to find its factorial: "))
        if num < 0:
            print("Error: Factorial is not defined for negative numbers.")
        else:
            result = math.factorial(num)
            print(f"The factorial of {num} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid integer.")

def natural_log():
    """Calculates the natural logarithm (base e) of a number."""
    try:
        num = float(input("Enter a positive number to find its natural logarithm: "))
        if num <= 0:
            print("Error: Natural logarithm is only defined for positive numbers.")
        else:
            result = math.log(num)
            print(f"The natural logarithm of {num} is {result}")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

def power_function():
    """Calculates the power of a number (x^b)."""
    try:
        base = float(input("Enter the base number (x): "))
        exponent = float(input("Enter the exponent (b): "))
        result = math.pow(base, exponent)
        print(f"{base} raised to the power of {exponent} is {result}")
    except ValueError:
        print("Invalid input. Please enter valid numbers for both base and exponent.")

def main():
    """Main function to run the calculator menu."""
    print("Welcome to the Scientific Calculator!")
    
    while True:
        print("\n--- Menu ---")
        print("1. Square Root (√x)")
        print("2. Factorial (!x)")
        print("3. Natural Logarithm (ln(x))")
        print("4. Power Function (x^b)")
        print("5. Exit")
        
        choice = input("Please select an operation (1-5): ")
        
        if choice == '1':
            square_root()
        elif choice == '2':
            factorial()
        elif choice == '3':
            natural_log()
        elif choice == '4':
            power_function()
        elif choice == '5':
            print("Thank you for using the calculator. Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option from the menu.")

if __name__ == "__main__":
    main()