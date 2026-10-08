# Password Generator

A Python command-line application designed to generate secure, randomized passwords based on user-defined parameters.

## Features

- **Custom Password Length**: Users can define the exact length of the password (minimum 4 characters).
- **Character Type Selection**: Users can optionally include numerical digits and special symbols alongside standard uppercase and lowercase letters.
- **Guaranteed Character Inclusion**: Prevents edge cases where randomly generated passwords might accidentally omit a requested character type.
- **Input Validation**: Gracefully catches and handles invalid text entries when a numerical length is expected, preventing application crashes.

## How It Works

The application operates through a straightforward procedural logic designed for reliability and true randomness:

1. **Input Collection & Validation**: The 'main()' function prompts the user for their desired password length and uses a 'try-except' block to handle 'ValueError' exceptions (e.g., if a user types "ten" instead of "10").
2. **Pool Construction**: In the ;generate_password()' function, the base character pool always includes 'string.ascii_letters'. If the user inputs 'y' for numbers or symbols, 'string.digits' and 'string.punctuation' are appended to this pool.
3. **Guaranteed Selection**: To guarantee that a requested character type is actually included in the final output, the script immediately selects one random character from each requested category and adds it to a 'password_chars' list.
4. **Randomization & Shuffling**: A 'while' loop fills the remaining requested length by randomly choosing characters from the combined pool. Since the guaranteed characters were added first, 'random.shuffle()' is applied to the list to completely randomize the order before joining it into a final string.

## Example Usage

**Starting the application:**
To use the password generator, navigate to the project directory in your terminal and execute the Python script:
```bash
python main.py

Example terminal output:
--- Secure Password Generator ---
Enter password length (minimum 4): 12
Include numbers? (y/n): y
Include symbols? (y/n): y

Generated Password: K4uZ>"j^wWiU
---------------------------------

Thanks for using Password Generator
