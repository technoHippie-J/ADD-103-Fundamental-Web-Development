# Accept a numeric grade from the user and display a letter grade. The  grading scale is 90 - 100: A, 80-89: B, 70-79: C, 60-69: D, Below 60: F

# Check to see if the number given is between 0 and 100.

# request number grade from user
print()
print("Hello, please enter your grade as a number value, ie: 95, 82, 74, etc...")
grade = input("Grade: ")

# checks to ensure user entered a number, and provides error message if they entered anything else
if grade.isnumeric():
    print("Thank you for entering your numeric grade.\n")
    grade = int(grade)  # converts to int if user entered a number

    # checks to see if entry falls within given ranges, and determines it to be invalid if it falls outside of acceptable ranges
    if grade <= 100 and grade >= 90:
        grade = "A"
    elif grade <= 89 and grade >= 80:
        grade = "B"
    elif grade <= 79 and grade >= 70:
        grade = "C"
    elif grade <= 69 and grade >= 60:
        grade = "D"
    elif grade <= 59:
        grade = "F"
    elif grade >= 101:
        grade = "invalid"
else:
    # informs user if they did not enter a number value
    print("\nI'm sorry, but you did not enter your grade in a numeric format.")

# if/elif used to ensure proper grammar
# provides user their letter grade
if grade == "A" or grade == "F":
    print(f"Your letter grade is an {str(grade)}\n")
elif grade == "B" or grade == "C" or grade == "D":
    print(f"Your letter grade is a {str(grade)}\n")
# informs user if they have given an invalid number value
elif grade == "invalid":
    print("You have given an invalid number outside of the acceptable range.\n")

input("Please press enter to exit the program...")
