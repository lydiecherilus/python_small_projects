''' the program generates a password with random letters, numbers and symbols 
the password length depends on the user's input'''

import random
import string

# to check input validity
is_input_valid = False

# ask for user input
while not is_input_valid: # loop until the user enters a valid integer
    try:
        number_of_letters = int((input("How many letters do you want in your password?\n")))
        number_of_numbers = int((input("How many numbers do you want in your password?\n")))
        number_of_symbols = int((input("How many symbols do you want in your password?\n")))
        is_input_valid = True # if this point is reached, valid integers were entered for all 3 inputs
    except ValueError:
        print("Please only input digits")  

# generate the letters, numbers and symbols
random_letters = random.sample(string.ascii_letters, number_of_letters ) # generate random letters
random_numbers = random.sample(string.digits, number_of_numbers) # generate random numbers
random_symbols = random.sample(string.punctuation, number_of_symbols ) # generate random symbols

# combine and randomize input position 
user_password_input = random_letters + random_numbers + random_symbols
random_user_password_input = random.sample(user_password_input, len(user_password_input))

# return password
password = "".join(random_user_password_input)
print(f"Your password is: {password}")


# use this link to create your password: https://replit.com/@lydiecherilus/passwordgenerator?v=1
