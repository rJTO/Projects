# Generates (not-so-secure) passwords of user-defined length & count

import random

get_count = True
get_length = True
chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()'

print("Password Generator\n==================")

# Gets valid number of passwords from user
while get_count:
    while True:
        try:
            pass_count = int(input("Enter the number of passwords to generate: "))
            break
        except ValueError:
            print("Invalid input")
    get_count = False

# Gets valid password length from user
while get_length:
    while True:
        try:
            pass_length = int(input("Enter desired password character length: "))
            break
        except ValueError:
            print("Invalid input")
    get_length = False

# Generates defined password count and length
for i in range(pass_count):
    passwords = ''
    for j in range(pass_length):
        passwords += random.choice(chars)
    print(passwords)
