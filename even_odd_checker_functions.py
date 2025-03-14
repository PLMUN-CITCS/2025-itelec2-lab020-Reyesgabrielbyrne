def get_integer_input() -> int:
    """
    This function prompts the user to enter an integer.
    It reads the input, converts it to an integer, and returns it.
    It will keep asking for a valid integer if the input is invalid.

    Returns:
        int: The integer entered by the user.
    """
    while True:
        try:
            # Prompt the user to enter an integer
            user_input = input("Enter an integer: ")
            # Convert the input to an integer
            number = int(user_input)
            return number
        except ValueError:
            # Handle the case where the input is not a valid integer
            print("Invalid input! Please enter a valid integer.")

def check_even_odd(number: int) -> str:
    """
    This function checks whether the given integer is even or odd.
    It uses the modulo operator (%) to check divisibility by 2.

    Args:
        number (int): The integer to be checked.

    Returns:
        str: A formatted string indicating whether the number is "Even" or "Odd".
    """
    if number % 2 == 0:
        return f"{number} is an Even number."
    
    return f"{number} is an Odd number."

def main():
    # Get an integer input from the user
    number = get_integer_input()
    # Check if the number is even or odd
    result = check_even_odd(number)
    # Display the result
    print(result)

# Run the main function if the script is executed
if __name__ == "__main__":
    main()