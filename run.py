
def add(x, y):
    """
    Return the sum of x and y.
    Parameters:
    x (float): The first number.
    y (float): The second number.
    Returns:
    float: The sum of x and y.
    """
    return x + y
def subtract(x, y):
    """
    Return the difference of x and y.
    Parameters:
    x (float): The first number.
    y (float): The second number.
    Returns:
    float: The difference between x and y.
    """
    return x - y
def confirm_continue():
    """
    Ask the user whether they want to perform another calculation.
    Returns:
    bool: True if the user wants to continue, False otherwise.
    """
    while True:
        next_calculation = input("\nContinue? (yes/no): ").strip().lower()
        if next_calculation in ['yes', 'y']:
            return True
        elif next_calculation in ['no', 'n']:
            return False
        else:
            print("Invalid input! Please enter 'yes' or 'no'.")


def calculator():
    """
    Main calculator function that allows users to perform arithmetic
    operations. This function will continue to prompt the user for
    operations and numbers until they decide to stop. The user can
    perform addition, subtraction, multiplication, and division.
    """
    print("Welcome to the Simple Calculator!")
    while True:
        perform_calculation()
        # Ask if the user wants to continue
        if not confirm_continue():
            print("\nThank you for using the calculator. Goodbye!")
            break
if __name__ == "__main__":
    calculator()
