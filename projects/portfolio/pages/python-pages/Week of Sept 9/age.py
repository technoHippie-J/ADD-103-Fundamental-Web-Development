# Write a Python program that uses if else statements and :

# Ask the user for their age.
# Check to see if the user is old enough to drive.
# Check to see if the user can vote.
# Check to see if the user can legally buy alcohol.
# Check to see if the user is eligible for a senior discount(65).
# Print all the results on the screen.

print()
print("Hello! How old are you?")  # asks user for their age
user_age = int(input("Age: "))  # age entry field
print()

# can the user drive, and how
if user_age <= 14:
    print("I'm sorry, you are not old enough to drive.")
elif user_age == 15:
    print("You are old enough to drive on a permit with a parent or guardian with you.")
elif user_age >= 16:
    print("You are old enough to drive.")

# can the user vote
if user_age <= 17:
    print("I'm sorry, you are not old enough to vote.")
elif user_age >= 18:
    print("You are old enough to vote.")

# can the user buy alcohol
if user_age <= 20:
    print("No, you are not old enough to buy alcohol. Don't even try.")
elif user_age >= 21:
    print("You are old enough to buy alcohol. Drink responsibly.")

# can the user receive senior discounts
if user_age <= 64:
    print("I'm sorry, you are not old enough to receive senior discounts. Must be so difficult being young.\n")
elif user_age >= 65:
    print("You are eligible for senior discounts!\n")

# show the user appreciation and provide exit prompt
print("Thank you for taking this age evaluation. \nPlease press enter to exit the program.")
input("Press Enter...")
print()
