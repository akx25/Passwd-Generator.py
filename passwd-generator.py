import string
import secrets

account = input("Enter E-Mail or username used for the password: ")
length = int(input("Enter password length: "))

characters = string.ascii_letters + string.digits + string.punctuation
password = "".join(secrets.choice(characters) for _ in range(length))

with open("passwords.txt", "a", encoding="utf-8") as file:
    file.write(f"Account: {account}\nPassword: {password}\n\n")

print(f"Generated password for {account} and saved to passwords.txt")