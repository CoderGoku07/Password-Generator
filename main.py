import random
import string


def generate_password(length, use_numbers, use_symbols):
    pool = string.ascii_letters
    password_chars = []

    # Guarantee at least one random letter
    password_chars.append(random.choice(string.ascii_letters))

    # Guarantee at least one number if requested
    if use_numbers:
        pool += string.digits
        password_chars.append(random.choice(string.digits))
    
    # Guarantee at least one symbol if requested
    if use_symbols:
        pool += string.punctuation
        password_chars.append(random.choice(string.punctuation))

    # Fill the remaining length with random choices from the combined pool
    while len(password_chars) < length:
        password_chars.append(random.choice(pool))

    # Shuffle the list so the guaranteed characters aren't always at the start
    random.shuffle(password_chars)

    # Convert the list of characters back into a single string
    return "".join(password_chars)


def main():
    print("\n--- Secure Password Generator ---")
    
    try:
        length = int(input("Enter password length (minimum 4): "))
        if length < 4:
            print("Error: Password length must be at least 4.")
            return
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    use_numbers = input("Include numbers? (y/n): ").strip().lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").strip().lower() == 'y'

    password = generate_password(length, use_numbers, use_symbols)
    
    print(f"\nGenerated Password: {password}")
    print("---------------------------------\n")
    print("Thanks for using Password Generator")

if __name__ == "__main__":
    main()