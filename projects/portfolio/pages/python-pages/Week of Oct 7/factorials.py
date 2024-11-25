# Understanding Factorials
# Factorials!Links to an external site.

# A factorial is a mathematical operation applied to a non-negative integer n, denoted by n!, that results in the product of all positive integers less than or equal to n. For example, the factorial of 5 (5!) is calculated as 5 x 4 x 3 x 2 x 1, which equals 120.

# Objective
# Your task is to write a Python program using a recursive function to calculate the factorial of a number. A recursive function is a function that calls itself to solve a problem.

# Assignment Instructions
# Start by defining a function named factorial that takes one parameter, n, representing the number you're calculating the factorial for.
# In your factorial function, first define the base case. The base case for our recursion will be when n is 1 or 0, because the factorial of 1 and 0 is 1.
# For the recursive step, if n is greater than 1, the function should return n multiplied by a call to itself with n-1.
# Create a main function. Inside this function, prompt the user to enter a non-negative integer. Use the int() function to convert the input to an integer.
# Call the factorial function from your main function with the user's input as its argument, and print the result in a format like "The factorial of n is result.".
# Finally, call your main function to run the program.
# Upload to GitHub and submit your link to hand in the program.
# About this Assignment:
# This assignment should take approximately 1-2 hours of study and 45 minutes of coding.
# Late submissions will result in a 10% deduction per day, up to a maximum of 50%.
# Submit your program on GitHub and provide the link for assessment.
# See grading details in the rubric below.
# You may fix and resubmit your program within a week of when the assignment is graded.


# defines the function to find a factorial with parameter "n" to represent the number entered by the user
def factorial(n):
    # once n equals 1 or 0, the function will return n as the result of the recursion stack collapsed into itself one achieving the base case
    if n == 1 or n == 0:
        return n
    # returns n multiplied by this function with the parameter of n - 1
    elif n > 1:
        return n * factorial(n-1)

# main program function


def main():
    # requests a non-negative integer from the user
    print("Please enter a non-negative whole number.")
    num = int(input("Enter: "))

    # defines the variable result as a call of the factorial function using the input number as its parameter
    result = factorial(num)

    # displayes the result of the function
    print(f"The factorial of {num} is {result}.")


main()
