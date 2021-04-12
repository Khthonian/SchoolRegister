def sch_register():
    # Ask for user's first and last name
    full_name = input("Please enter your full name: ")
    # Extract the first and last name from sch_register
    full_name_extract = full_name.split()
    first_name = full_name_extract[0]
    last_name = full_name_extract[-1]
    # Say Hello xx
    print("Hello ", first_name)
    # Ask the user to enter their age
    age = int(input("What is your age: "))
    # Ask for user's age
    # If age is under 11, return message that alerts they are too young
    # If age is over 18, return message that alerts they are too old
    # If 11<age<18, ask for DOB (dd/mm/yyyy)
    # Display birth year
    age_verify = 0
    while age_verify != 2:
        if age < 11:
            print("Sorry, you are too young to be registered in the school")
            age = int(input("What is your age: "))
        elif age > 18:
            print("Sorry, you are too old to be registered in the school")
            age = int(input("What is your age: "))
        else:
            age_verify = 2
            dob = input("What is your date of birth (dd/mm/yyyy): ")
            yob = dob[-4:]
            print("You were born in the year", yob)
    # Create email address based upon full name, year of birth and a random number
    import random
    random_number = (random.randint(10,99))
    email_prefix = f'{first_name.lower()}{last_name.lower()}{yob}{random_number}'
    email_suffix = '@school.ac.uk'
    email = f'{email_prefix}{email_suffix}'
    return email
    
def pwd_validate(pwd):
    password = 0
    symbols = "!@#$%^&*"
    # Detail the categories for password validation
    # Then check to see if the length is correct
    # If the length is correct, proceed to check the other categories
    while password != 5:
        character_upper = 0
        character_lower = 0
        character_digit = 0
        character_symbol = 0
        if len(pwd) == 12:
            password += 1
        for i in pwd:
            if i.isupper():
                character_upper = 1
            if i.islower():
                character_lower = 1
            if i.isdigit():
                character_digit = 1
            if i in symbols:
                character_symbol = 1
        password += character_upper + character_lower + character_digit + character_symbol
        if password == 5:
            return pwd
        else:
            password = 0
            print("Your password has been denied. Please input a password with uppercase, lowercase, numeric, and symbol characters.")
            pwd = input("\nPlease enter your new password, it should be 12 characters long: ")
    
    
# Program main --- Do not change the code below but feel free to comment out 
# sections of code when working on individual functions. 
# Calling Task 1 function
email = sch_register()
print("Your new school email is: ", email)

# Calling Task 2 function
pwd = input("\nPlease enter your new password, it should be 12 characters long: ")
print("Your new password is: ")
print(pwd_validate(pwd))