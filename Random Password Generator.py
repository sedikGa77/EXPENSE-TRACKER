#Random Password Generator
import random
import string
password=[]
length=int(input("enter password length:"))
include_upper = input("include uppercase letters? (y/n): ").lower() == 'y'
include_lower = input("include lowercase letters? (y/n): ").lower() == 'y'
include_digits = input("include numbers? (y/n): ").lower() == 'y'
include_symbols = input("include symbols? (y/n): ").lower() == 'y'
characters = ""
if include_upper:
    characters += string.ascii_uppercase
if include_lower:
    characters += string.ascii_lowercase
if include_digits:
    characters += string.digits
if include_symbols:
    characters += string.punctuation

if not characters:
    print("you must select at least one option!")
    exit()
password = ''.join(random.choice(characters) for _ in range(length))
print("Your generated password is:", password)
