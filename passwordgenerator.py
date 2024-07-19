import random

characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ123456789!@#$%^&*_"

def generate_password(length):
    return ''.join(random.choice(characters) for _ in range(length))

while True:
    password_length = int(input('Enter the length of password: '))
    password_count = int(input('How many passwords do you want: '))
    
    for _ in range(password_count):
        print('Here is your password:', generate_password(password_length))
    
    if input('Do you want to generate another password? (Y/N): ').strip().lower() == 'n':
        break

print('Thanks for using the password generator!')
