"""Secure command-line password generator."""

import secrets
import string


def generate_password(length: int) -> str:
    """Generate a cryptographically secure random password."""
    if length < 4:
        raise ValueError("Password length must be at least 4.")

    characters = string.ascii_letters + string.digits + string.punctuation
    return "".join(secrets.choice(characters) for _ in range(length))


def main() -> None:
    print("=" * 34)
    print("     Smart Password Generator")
    print("=" * 34)

    try:
        length = int(input("Enter password length (4+): "))
        password = generate_password(length)
    except ValueError as error:
        print(f"Error: {error}")
        return

    print(f"Generated password: {password}")
    print("Tip: Store passwords in a password manager and never share them.")


if __name__ == "__main__":
    main()
