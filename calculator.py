# calculator.py
import math

# --- Core Calculation Functions ---

def square_root(number):
    """Calculates the square root of a non-negative number."""
    if number < 0:
        raise ValueError("Cannot calculate square root of a negative number.")
    return math.sqrt(number)

def factorial(number):
    """Calculates the factorial of a non-negative integer."""
    if not isinstance(number, int) or number < 0:
        raise ValueError("Factorial is only defined for non-negative integers.")
    return math.factorial(number)

def natural_log(number):
    """Calculates the natural logarithm of a positive number."""
    if number <= 0:
        raise ValueError("Natural logarithm is only defined for positive numbers.")
    return math.log(number)

def power(base, exponent):
    """Calculates base raised to the power of exponent."""
    return math.pow(base, exponent)


# --- User Interface and Main Loop ---

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
        
        try:
            if choice == '1':
                num = float(input("Enter a number: "))
                print(f"Result: {square_root(num)}")
            elif choice == '2':
                num = int(input("Enter an integer: "))
                print(f"Result: {factorial(num)}")
            elif choice == '3':
                num = float(input("Enter a number: "))
                print(f"Result: {natural_log(num)}")
            elif choice == '4':
                base = float(input("Enter the base: "))
                exponent = float(input("Enter the exponent: "))
                print(f"Result: {power(base, exponent)}")
            elif choice == '5':
                print("Thank you for using the calculator. Goodbye!")
                break
            else:
                print("Invalid choice. Please select a valid option.")
        except ValueError as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()