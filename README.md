# Morse Code Encryption and Decryption

## Overview

This Python program allows users to encrypt and decrypt strings using a dictionary-based approach for Morse code.  
The encryption and decryption dictionaries are predefined, mapping characters to their Morse code equivalents.

## Features

- **Encryption:** Convert a plaintext string into Morse code.
- **Decryption:** Convert Morse code back into the original plaintext.
- **User Interaction:** Easy-to-use command-line interface with prompts for user input.
- **Error Handling:** Robust error handling for invalid input strings.

## Getting Started

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/morse-encryption.git
   cd morse-encryption
   ```

2. Run the program:

   ```bash
   python morse_code_program.py
   ```

3. Follow the on-screen prompts to encrypt, decrypt, or quit the program.

## Usage

- Enter 'e' to encrypt a string.
- Enter 'd' to decrypt a Morse code string.
- Enter 'q' to quit the program.

## Examples

### Encrypting a String

Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: e  
Enter a string you would like to encrypt: Hello World  
The encrypted string is: .... . .-.. .-.. --- .-- --- .-. .-.. -..

### Decrypting Morse Code

Enter 'e' to encrypt, 'd' to decrypt, or 'q' to quit: d  
Enter a string you would like to decrypt: .... . .-.. .- .-.. -.. -.-- -.-- -.-- -... .- -.-.  
The decrypted string is: HAPPY HAPPY HAPPY BACK

## Dependencies

- None

## License

This program is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
