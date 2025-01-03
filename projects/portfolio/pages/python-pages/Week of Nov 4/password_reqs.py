"""
This program prompts the user to input a password and ensures it meets specific criteria:
- Between 8 to 20 characters long.
- Contains at least one uppercase letter.
- Contains at least one lowercase letter.
- Includes at least one number.
- Includes at least one symbol from the set: !@#$%&*.

The program uses a while loop to repeatedly ask for the password until all criteria are met.
Once a valid password is entered, the user is prompted to enter it again for confirmation.
If the second password entry matches the first, a success message is displayed.
Otherwise, the user is prompted to start the process again.

Functions:
- chk_alpha(string): Checks if the password contains at least one letter.
- chk_upper(string): Checks if the password contains at least one uppercase letter.
- chk_lower(string): Checks if the password contains at least one lowercase letter.
- chk_number(string): Checks if the password contains at least one number.
- chk_symbol(string): Checks if the password contains at least one symbol out of an accepted list.
- chk_length(string): Checks if the password complies with minimum and maximum length limitions.

The program also uses try-except blocks to handle any errors or exceptions that occur.
"""

# Assignment Outline:
# Set up your program in a main() function
# Create a Python program that asks the user to input a password.
# Ensure the password meets the following criteria:
# Between 8 to 20 characters long.
# Contains at least one uppercase letter.
# Contains at least one lowercase letter.
# Includes at least one number.
# Includes at least one symbol from the set: !@  # $%&*.
# Use a while loop to keep asking for the password until all criteria are met.
# Once a valid password is entered, prompt the user to enter it again for confirmation.
# Use try -except blocks to handle any errors or exceptions that occur.
# If the second password entry matches the first, display a success message. Otherwise, prompt the user to start the process again.

pass_attempt = " "


# check if password attempt contains a letter
# comments apply to most included functions
# and will be added in the exception

# define function
def chk_alpha(string):
    # try to see if a letter is included
    try:
        # set found flag
        exit = False
        for i in string:
            if i.isalpha():
                exit = True
        if exit == True:
            return True
        else:
            # If no letter found, raise error
            raise ValueError("***No letters found***")
    # if error raised, display error message
    except ValueError as e:
        print()
        print(e)
        return False

# check if password attempt contains a uppercase letter


def chk_upper(string):
    try:
        exit = False
        for i in string:
            if i.isupper():
                exit = True
        if exit == True:
            return True
        else:
            raise ValueError("***No uppercase letter found***")
    except ValueError as e:
        print()
        print(e)
        return False


# check if password attempt contains a lowercase letter
def chk_lower(string):
    try:
        exit = False
        for i in string:
            if i.islower():
                exit = True
        if exit == True:
            return True
        else:
            raise ValueError("***No lowercase letter found***")
    except ValueError as e:
        print()
        print(e)
        return False


# check if password attempt contains a number
def chk_number(string):
    try:
        exit = False
        for i in string:
            if i.isdigit():
                exit = True
        if exit == True:
            return True
        else:
            raise ValueError("***No number found***")
    except ValueError as e:
        print()
        print(e)
        return False


# check if password attempt contains a symbol from the allowed list
def chk_symbol(string):
    try:
        exit = False
        for i in string:
            if i in "!@#$%&*":
                exit = True
        if exit == True:
            return True
        else:
            raise ValueError("***Approved symbol not found***")
    except ValueError as e:
        print()
        print(e)
        return False


# check if password meets minimum and maximum character length reqs
def chk_length(string):
    try:
        # check if both requirements are met
        if 8 <= len(string) and len(string) <= 20:
            return True
        # check if too short, raise associated error
        elif len(string) < 8:
            raise ValueError("***Password is too short***")
        # check if too long, raise associated error
        elif len(string) > 20:
            raise ValueError("***Password is too long***")
    except ValueError as e:
        print()
        print(e)
        return False


# main program
def main():
    # set all checks to false for recursive loops
    alpha = upper = lower = number = symbol = length = False
    print()
    print("Please enter a password that includes all of the following criteria:\n\t- Between 8 to 20 characters long\n\t- Contains at least one uppercase letter\n\t- Contains at least one lowercase letter\n\t- Includes at least one number\n\t- Includes at least one symbol from the set: !@#$%&*.\n")

    pass_attempt = input("Password: ")

    # check criteria
    alpha = chk_alpha(pass_attempt)
    upper = chk_upper(pass_attempt)
    lower = chk_lower(pass_attempt)
    number = chk_number(pass_attempt)
    symbol = chk_symbol(pass_attempt)
    length = chk_length(pass_attempt)

    # check if all criteria are met, or enter recursion until all are true
    while not (alpha and upper and lower and number and symbol and length):
        print("That is not a valid password!")
        main()  # Recursive call if validation fails
        return  # Ensure exit after successful recursion

    # Once every criteria is met, program continues with confirmation
    print()
    print("Thank you for entering a valid password!\nPlease enter your password again to confirm.")
    # set comparator default value
    restart = False
    conf_pass = ""
    # enter password confirm loop
    while restart == False:
        # set success counter to 0
        counter = 0
        # loop until 1st and 2nd entries match
        while conf_pass != pass_attempt:
            conf_pass = input("Password: ")
            # if match, add to counter, set flag to end loop, print success
            if conf_pass == pass_attempt:
                counter += 1
                restart = True
                print()
                print(
                    "Password creation success!\nThank you for creating a password.\nYou are now safer!\n")
            # if no match, ask user if they want to try again or start over
            else:
                print()
                print("That was not the same password.\nYou can try confirmation again, or you can start over.\nWould you like to try confirmation again? (y/n)")
                # set loop flag
                error = True
                # while flag
                while error == True:
                    try:
                        try_again = input("Enter: ").lower()
                        # if user wants to start over
                        if try_again == "n":
                            # set restart flag to True to break loop and enter next recursion
                            restart = True
                            # set error flag to false as no error occured
                            error = False
                            # break from password mismatch loop, pass_attempt resets next recursion.
                            conf_pass = pass_attempt
                        # if user wants to try again, sets error flag to false to break from loop and return to password confirmation entry.
                        elif try_again == "y":
                            print("\nPlease try entering your password again.")
                            error = False
                        # error handling for illegal input
                        elif try_again != "n" and try_again != "y":
                            # raise error and leave error flag to True, as error had occurred
                            raise ValueError(
                                "\nI'm sorry, you did not enter a valid reponse. Please enter 'y' for yes, or 'n' for no.")
                    except ValueError as e:
                        print()
                        print(e)

    # if user wants to restart and success counter is 0, leads to recursion. Counter requirement is necessary or program hangs after successful entry.
    if restart == True and counter == 0:
        main()
        return


main()
