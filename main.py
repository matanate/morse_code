# Import necessary modules
from art import title_art
from dictionaries import DECRYPT_DICT, ENCRYPT_DICT
import sys


# Function to encrypt the string
def encrypt(input_str):
    """
    Encrypts the input string using a predefined encryption dictionary.

    Args:
        input_str (str): The string to be encrypted.

    Returns:
        str: The encrypted string.
    """
    # Initiate a string of the first character encryption
    result = ENCRYPT_DICT[input_str[0]]
    # Iterate over the remaining characters, adding space and encryption for each
    for char in input_str[1:]:
        result += f" {ENCRYPT_DICT[char]}"

    return result


# Function to decrypt the string
def decrypt(input_str):
    """
    Decrypts the input string using a predefined decryption dictionary.

    Args:
        input_str (str): The string to be decrypted.

    Returns:
        str: The decrypted string.
    """
    # Initiate an empty string
    result = ""
    # Iterate over each substring separated by spaces.
    for char in input_str.split():
        # check for a '/' character that represent a space.
        if char != "/":
            result += f"{DECRYPT_DICT[char]}"
        else:
            result += " "
    return result


# Function to prompt the user for a string to encrypt/decrypt.
# The function receives a function decrypt/encrypt and prints the result
def string_process(activation_func):
    """
    Prompts the user for a string, applies the specified activation function,
    and prints the result. Handles invalid input and prompts the user recursively.

    Args:
        activation_func (function): The encryption or decryption function.

    Returns:
        None
    """
    # Catch exceptions where invalid strings were entered.
    try:
        input_string = input(
            f"Enter a string you would like to {activation_func.__name__}: "
        ).lower()
        # Check for an empty string
        if not input_string.strip():
            raise ValueError("Input string cannot be empty.")

        result_string = activation_func(input_string)
        print(f"The {activation_func.__name__}ed string is: {result_string}")
    except KeyError:
        if activation_func == decrypt:
            print("The string you entered is not a morse code")
        else:
            print(
                "Invalid character was used\nValid characters: numbers, letters, space, ',', '.', '?', '/', '-', '(', ')'"
            )
        # Recursively call the function to handle the exception and prompt again
        string_process(activation_func)
    except ValueError as e:
        print(e)
        string_process(activation_func)


# Main function
def main():
    """
    The main function that orchestrates the program's flow.
    Prompts the user to select an operation (encrypt/decrypt/quit),
    processes the user input, and repeats or exits accordingly.

    Returns:
        None
    """
    # Define a dictionary to map user inputs to functions
    user_choices = {"d": decrypt, "e": encrypt, "q": sys.exit}

    # Print program title
    print(title_art)

    # Prompt the user to enter the desired functionality until a valid choice is made
    while True:
        user_input = input(
            "Enter 'd' to decrypt, 'e' to encrypt, or 'q' to quit: "
        ).lower()
        if user_input in user_choices:
            if user_input == "q":
                user_choices[user_input](0)
            activation_func = user_choices[user_input]
            break
        else:
            print("Invalid choice. Please enter 'd', 'e', or 'q'.")
    # Initiate string prompt and process
    string_process(activation_func)
    # Prompt the user to restart thr program or quit
    if (
        input("Enter 'y' to encrypt/decrypt another string or 'n' to quit: ").lower()
        == "y"
    ):
        main()


# Entry point of the program
if __name__ == "__main__":
    main()
