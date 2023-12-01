import random
import string

def generate_password(length, complexity):
    if complexity == "low":
        characters = string.ascii_letters + string.digits
    elif complexity == "medium":
        characters = string.ascii_letters + string.digits + string.punctuation
    elif complexity == "high":
        characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_lowercase + string.ascii_uppercase
    else:
        raise ValueError("Invalid complexity level")

    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    print("Password Generator")

    # Get user input for password length
    try:
        length = int(input("Enter the desired length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
        return

    # Get user input for password complexity
    complexity_levels = ["low", "medium", "high"]
    print("Choose the complexity level:")
    print("1. Low (Alphanumeric)")
    print("2. Medium (Alphanumeric + Symbols)")
    print("3. High (Alphanumeric + Symbols + Mixed Case)")

    try:
        choice = int(input("Enter your choice (1, 2, or 3): "))
        complexity = complexity_levels[choice - 1]
    except (ValueError, IndexError):
        print("Invalid choice. Please enter 1, 2, or 3.")
        return

    # Generate and print the password
    password = generate_password(length, complexity)
    print(f"\nGenerated Password: {password}")

if __name__ == "__main__":
    main()
