import random
import string

def generate_password(length=12, use_digits=True, use_special=True):
    """Generate a random password with given constraints."""
    lower = string.ascii_lowercase
    upper = string.ascii_uppercase
    digits = string.digits if use_digits else ""
    special = string.punctuation if use_special else ""
    
    all_chars = lower + upper + digits + special
    if not all_chars:
        print("You must allow at least one type of character!")
        return None

    password = "".join(random.sample(all_chars, length))
    return password

def main():
    print("=== Password Generator ===")
    try:
        length = int(input("Enter password length (default 12): ") or 12)
        use_digits = input("Include numbers? (y/n): ").lower() == 'y'
        use_special = input("Include special characters? (y/n): ").lower() == 'y'

        password = generate_password(length, use_digits, use_special)
        if password:
            print(f"\nGenerated Password: {password}")
    except ValueError:
        print("Invalid input! Please enter a valid number for length.")

if __name__ == "__main__":
    main()
