# Password Generator

import random

letters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "0123456789"
symbols = "!@#$%^&*"

characters = letters + numbers + symbols

password = ""

for i in range(12):
    password += random.choice(characters)

print("Your password is:")
print(password)