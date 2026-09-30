import random
import string
print("=" * 45)
print("          PASSWORD GENERATOR")
print("=" * 45)
print()
print("Create a strong password easily.")
print("Answer Yes or No for the options below.")
print()
# Ask the user for password length
length = int(input("Enter password length: "))
print()
# Ask which characters the user wants
capital = input("Include capital letters (A-Z)? Yes/No: ")
small = input("Include small letters (a-z)? Yes/No: ")
numbers = input("Include numbers (0-9)? Yes/No: ")
symbols = input("Include special characters (!@#$)? Yes/No: ")
# Convert answers to lowercase
capital = capital.lower()
small = small.lower()
numbers = numbers.lower()
symbols = symbols.lower()
# Create an empty character list
characters = ""
# Add characters according to the user's choice
if capital == "yes":
characters = characters + string.ascii_uppercase
if small == "yes":
characters = characters + string.ascii_lowercase
if numbers == "yes":
characters = characters + string.digits
if symbols == "yes":
characters = characters + string.punctuation
print()
# Check if the user selected at least one option
if characters == "":
print("Error: You must select at least one option.")
else:
# Check password length
if length <= 0:
print("Error: Password length must be greater than 0.")
else:
password = ""
# Generate the password
for i in range(length):
character = random.choice(characters)
password = password + character
print("=" * 45)
print("        PASSWORD GENERATED")
print("=" * 45)
print()
print("Your password is:")
print(password)
print()
print("Password length:", length)
print("=" * 45)
print()
print("Thank you for using Password Generator!"