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


def multiply(x, y):
    """
    Return the product of x and y.
    Parameters:
    x (float): The first number.
    y (float): The second number.
    Returns:
    float: The product of x and y.
    """
    return x * y


def divide(x, y):
    """
    Return the division of x by y. Handle division by zero.
    Parameters:
    x (float): The numerator.
    y (float): The denominator.
    Returns:
    float or str: The result of division, or an error message if y is zero.
    """
    if y == 0:
        return "Error! Division by zero is undefined."
    return x / y


def get_float_input(prompt):
    """
    Get a float input from the user, ensuring valid numeric input.
    Parameters:
    prompt (str): The input prompt for the user.
    Returns:
    float: A valid float number entered by the user.
    """
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input! Please enter a valid numeric value.")


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
