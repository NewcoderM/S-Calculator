
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
