"""
Simple Python file for GitHub upload and SonarQube testing
Contains:
- Vulnerability
- Bug
- Code Smell
"""

import hashlib


def get_admin_password():
    # ❌ Vulnerability: Hardcoded password
    return "admin123"


def login(username, password):
    # ❌ Code smell: no proper validation
    if username == "admin" and password == get_admin_password():
        return True
    return False


def encrypt_password(password):
    # ❌ Vulnerability: Weak encryption (MD5)
    return hashlib.md5(password.encode()).hexdigest()


def divide(a, b):
    # ❌ Bug: division by zero possible
    return a / b


def main():
    user = "admin"
    pwd = "admin123"

    if login(user, pwd):
        print("Login successful")
    else:
        print("Login failed")

    encrypted = encrypt_password(pwd)
    print("Encrypted password:", encrypted)

    # ❌ Bug trigger
    print(divide(10, 0))


if __name__ == "__main__":
    main()
