from getpass import getpass
from pathlib import Path
from argon2 import PasswordHasher

PASSWORD_FILE = Path(__file__).with_name("password.txt")
ph = PasswordHasher()


def main():
    username = input("Username: ").strip()
    if not username or ":" in username:
        print("Username must not be empty or contain a colon.")
        return

    # Check the username, since Argon2 generates a fresh salt for each hash.
    if PASSWORD_FILE.exists():
        for line in PASSWORD_FILE.read_text(encoding="utf-8").splitlines():
            if line.partition(":")[0] == username:
                print("That username already exists.")
                return

    password = getpass("Password: ")
    if not password:
        print("Password must not be empty.")
        return

    hashed_password = ph.hash(password)
    with PASSWORD_FILE.open("a", encoding="utf-8") as file:
        file.write(f"{username}:{hashed_password}\n")
    print("User saved successfully.")


if __name__ == "__main__":
    main()
