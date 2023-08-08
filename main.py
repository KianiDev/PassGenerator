# KianiDev
import random
import string
def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = "".join(random.choice(characters) for i in range(length))
    return "Heres your password: " + password
print(generate_password(input("Enter password length: ")))