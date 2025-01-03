# Objective: Enhance a basic Python program by implementing try and except statements to handle errors in user input, focusing on data type errors.

# Starting Code

# # Simple Python program to calculate the square of a number


# def square_number():
#     number = input("Enter a number to square: ")
#     squared_number = int(number) ** 2
#     print(f"The square of {number} is {squared_number}.")


# square_number()

# Instructions
# Understand the Code: Review the provided Python script. It calculates the square of a user-input number.
# Identify Potential Errors: Consider errors that might occur with non-numeric input.
# Add Exception Handling: Implement try and except blocks to catch a ValueError. Handle incorrect data types with an error message and reprompt.
# Test Your Code: Ensure the exception handling works correctly with various inputs.
# GitHub Upload: Upload your py file to GitHub and hand in the link


# About this Assignment:
# This assignment should take approximately 1-2 hours of study and 45 minutes of coding.
# Late submissions will result in a 10 % deduction per day, up to a maximum of 50 % .
# Submit your program on GitHub and provide the link for assessment.
# See grading details in the rubric below.
# You may fix and resubmit your program within a week of when the assignment is graded.


# Simple Python program to calculate the square of a number

def main():
    def square_number():
        number = input("\nEnter a number to square: ")
        # attempts to perform calculation
        try:
            squared_number = int(number) ** 2
        # displays indication that non-numeric characters were entered and cannot be used if non-numeric characters were entered
        except ValueError:
            print("Cannot perform mathematical operations using non-numeric characters.")
        # displays the result if calculation is successful
        else:
            print(f"The square of {number} is {squared_number}.")
        # informs the user the function has completed execution, regardless of success or if an error was encountered.
        finally:
            print("Function execution complete.\n")

    square_number()


main()
