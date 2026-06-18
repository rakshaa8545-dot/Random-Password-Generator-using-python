import random
import string


def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """
    Generates a random password based on user preferences.
    """
    characters = ""

    if use_letters:
        characters += string.ascii_letters

    if use_numbers:
        characters += string.digits

    if use_symbols:
        # Includes special characters such as %, &, (), etc.
        characters += string.punctuation

    if not characters:
        raise ValueError("No character types selected for password generation.")

    # Ensure the password contains at least one of each requested type
    password = []

    if use_letters:
        password.append(random.choice(string.ascii_lowercase))
        password.append(random.choice(string.ascii_uppercase))

    if use_numbers:
        password.append(random.choice(string.digits))

    if use_symbols:
        password.append(random.choice(string.punctuation))

    # Check if length is sufficient
    if length < len(password):
        raise ValueError(
            f"Password length must be at least {len(password)} for selected options."
        )

    remaining_length = length - len(password)

    for _ in range(remaining_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    return "".join(password)


def get_user_input():
    print("--- Random Password Generator ---")

    try:
        length = int(
            input("Enter the desired password length (minimum 11 for high security): ")
        )

        if length < 11:
            print(
                "Warning: For better security, passwords should be at least 11 characters long."
            )

        if length < 1:
            print("Error: Length must be at least 1.")
            return None

        print("\nPreferences (y/n):")

        inc_letters = (
            input("Include alphabets (lower & upper case)? ").lower() == "y"
        )
        inc_numbers = input("Include numbers? ").lower() == "y"
        inc_symbols = (
            input("Include special characters (%, &, (), etc.)? ").lower() == "y"
        )

        if not (inc_letters or inc_numbers or inc_symbols):
            print("Error: You must select at least one character type.")
            return None

        return length, inc_letters, inc_numbers, inc_symbols

    except ValueError:
        print("Error: Please enter a valid number for the length.")
        return None


def main():
    user_data = get_user_input()

    if user_data:
        length, letters, numbers, symbols = user_data

        try:
            password = generate_password(length, letters, numbers, symbols)

            print(f"\nGenerated Password: {password}")
            print(f"Password Length: {len(password)}")

        except Exception as e:
            print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()