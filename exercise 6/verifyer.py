from getpass import getpass
from pathlib import Path
from argon2 import PasswordHasher
from argon2.exceptions import InvalidHashError, VerificationError

PASSWORD_FILE = Path(__file__).with_name("password.txt")
ph = PasswordHasher()


def main():
    username = input("Username: ").strip()
    password = getpass("Password: ")

    if not PASSWORD_FILE.exists():
        print("No users registered yet. Run hasher.py first.")
        return

    for line in PASSWORD_FILE.read_text(encoding="utf-8").splitlines():
        stored_username, separator, stored_hash = line.partition(":")
        if separator and stored_username == username:
            try:
                ph.verify(stored_hash, password)
            except (VerificationError, InvalidHashError):
                print("Invalid username or password.")
            else:
                print("Login successful!")
            return

    print("Invalid username or password.")


if __name__ == "__main__":
    main()