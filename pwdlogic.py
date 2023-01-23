# Imports libraries
import secrets
import string
# Checks that input is positive number
def input_error_handler(prompt):
    num = 0
    while True:
        try:
            num = int(input(prompt))
            if num < 0:
                print("Please enter a positive number")
                continue
            break
        except ValueError:
            print("Please enter a number")
    return num
# Randomly grabs a character from the 'fulllist' as many times as specified
def general():
    length = input_error_handler("Enter password length: ")
    full_list = string.ascii_lowercase + string.ascii_uppercase + string.digits + string.punctuation
    return ''.join(secrets.choice(full_list) for i in range(int(length))) 
# Main logic function for the custom password option
def custom():
    # Inputs how many of each character user wants
    lowernum = input_error_handler("Lower case character count: ")
    uppernum = input_error_handler("Upper case character count: ")
    digitnum = input_error_handler("Digit count: ")
    specnum = input_error_handler("Special character count: ")
    # Creates list, then randomly adds each characters of each type to list for specified amount
    temp_list = []
    temp_list.extend(list(secrets.choice(string.ascii_lowercase) for i in range(int(lowernum))))
    temp_list.extend(list(secrets.choice(string.ascii_uppercase) for i in range(int(uppernum))))
    temp_list.extend(list(secrets.choice(string.digits) for i in range(int(digitnum))))
    temp_list.extend(list(secrets.choice(string.punctuation) for i in range(int(specnum))))
    # Uses Fisher-Yates shuffle to shuffle temp_list, returns password
    for i in range(len(temp_list)-1, 1, -1):
        j = secrets.randbelow(i + 1)
        temp = temp_list[i]
        temp_list[i] = temp_list[j]
        temp_list[j] = temp

    return ''.join(temp_list)
# While loop allows re-use
while True:
    # Asks user what option they want
    general_or_custom = input("General (g) or custom (c) password? Press (x) to exit: ").lower()
    # Checks and executes requested function, breaks for exit command
    if general_or_custom == "general" or general_or_custom == "g":
        print(general())
    elif general_or_custom == "custom" or general_or_custom == "c":
        print(custom())
    elif general_or_custom == "exit" or general_or_custom == "x":
        print("Program terminated")
        break
    else:
        print('Error, invalid input. Please enter a valid command')