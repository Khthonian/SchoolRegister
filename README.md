# School Register

This Python script provides two functions: `sch_register()` and `pwd_validate(pwd)`. The `sch_register()` function allows a user to register for a school by providing their full name, age, and date of birth (DOB). It then generates a school email address based on the user's information. The `pwd_validate(pwd)` function allows the user to create a password and validates if it meets specific criteria.

## `sch_register()` Function

### How to Use

1. Run the Python script in your Python environment.
2. The program will prompt you to enter your full name.
3. Next, you need to enter your age.
4. If you are under 11 years old or over 18 years old, the program will notify you that you are not eligible for school registration.
5. If your age is between 11 and 18 (inclusive), you will be asked to provide your date of birth in the format "dd/mm/yyyy."
6. The program will then display the year of birth based on the provided date of birth.
7. The function will create a school email address for you using the first name, last name, year of birth, and a random number.

## `pwd_validate(pwd)` Function

### How to Use

1. After running the script, the program will prompt you to enter a new password.
2. The password should be 12 characters long.
3. The password must contain at least one uppercase letter, one lowercase letter, one numeric digit, and one symbol from the set "!@#$%^&*".
4. If the password meets all the criteria, it will be accepted and displayed as the new password.
5. If the password does not meet the criteria, the program will ask you to input a new password until it meets all the requirements.

## Note

You can uncomment specific sections of the code to work on individual functions separately. To use the functions independently, comment out the function call of the other function.
