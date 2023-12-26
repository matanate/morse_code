from art import title_art
from dictionaries import DECRYPT_DICT, ENCRYPT_DICT
import sys


# Function to encrypt the string
def encrypt(input_str):
    # Initiate a string of the first character encryption
    result = ENCRYPT_DICT[input_str[0]]
    for char in input_str[1:]:
        # adds a space followed by encryption for each character.
        result += f" {ENCRYPT_DICT[char]}"

    return result


# Function to decrypt the string
def decrypt(input_str):
    # Initiate an empty string
    result = ""
    for char in input_str.split():
        # check for an '/' character that represent a space.
        if char != "/":
            result += f"{DECRYPT_DICT[char]}"
        else:
            result += " "
    return result


# Function to prompt the user for a string to encrypt/decrypt.
# The function receives a function decrypt/encrypt.
# And prints the result
def string_process(activation_func):
    # Catch exceptions where invalid strings were entered.
    try:
        input_string = input(
            f"Enter a string you would like to {activation_func.__name__}: "
        ).upper()
        result_string = activation_func(input_string)
        print(f"The {activation_func.__name__}ed string is: {result_string}")
    except KeyError:
        if activation_func == decrypt:
            print("The string you entered is not a morse code")
        else:
            print(
                "Invalid character was used\nValid characters: numbers, letters, space, ',', '.', '?', '/', '-', '(', ')'"
            )
        string_process(activation_func)


def main():
    # Print program title
    print(title_art)
    user_input = ""
    # Prompt the user to enter the desired functionality while an incorrect input is entered
    while not (user_input == "d" or user_input == "e" or user_input == "q"):
        user_input = input(
            "Enter 'd' to decrypt, 'e' to encrypt or 'q' to quit: "
        ).lower()
        # Assign the activation function that the user selected
        if user_input == "d":
            activation_func = decrypt
        elif user_input == "e":
            activation_func = encrypt
        elif user_input == "q":
            sys.exit(0)
    # Initiate string prompt and process
    string_process(activation_func)
    # Prompt the user to restart thr program or quit
    if (
        input("Enter 'y' to encrypt/decrypt another string or 'n' to quit: ").lower()
        == "y"
    ):
        main()


if __name__ == "__main__":
    main()
