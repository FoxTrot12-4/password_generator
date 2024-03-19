import random
import string

def generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols):
    characters = ''
    if use_lowercase:
        characters += string.ascii_lowercase
    if use_uppercase:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("Please include at least one character type.")
        return None

    return ''.join(random.choice(characters) for _ in range(length))

def main():
    print("Welcome to the Secure Password Generator!")
    while True:
        try:
            length = int(input("Enter the length of the password: "))
            break
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    while True:
        use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
        use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
        use_digits = input("Include digits? (y/n): ").lower() == 'y'
        use_symbols = input("Include symbols? (y/n): ").lower() == 'y'

        if use_lowercase or use_uppercase or use_digits or use_symbols:
            break
        else:
            print("Please include at least one character type.")

    password = generate_password(length, use_lowercase, use_uppercase, use_digits, use_symbols)
    if password:
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
