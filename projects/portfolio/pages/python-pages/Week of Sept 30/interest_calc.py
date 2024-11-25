# For Lesson PE1 4.3 - Returning a Result from a Function

# Objective: Write a Python function named calculate_interest that computes and returns the simple interest based on given parameters.

# Background
# Simple interest is calculated using the formula:

# Simple Interest = (Principal Amount × Rate of Interest × Time) / 100

# Your task is to translate this formula into a Python function.

# Function Requirements
# The function should be named calculate_interest.
# It should take three parameters:
# principal - The principal amount(the initial sum of money).
# rate - The rate of interest(as a percentage).
# time - The time the money is invested or borrowed for, in years.
# Get the information from the customer, then call the function and pass the information in .
# The function should calculate the simple interest using the given formula and return the result.
# Example
# If you call calculate_interest(1000, 5, 2), the function should return 100. This is because the simple interest on $1000 at a 5 % interest rate over 2 years is $100.

# Task Instructions
# Define the function calculate_interest with the appropriate parameters.
# Inside the function, apply the formula to calculate the simple interest.
# Ensure that the function returns the calculated interest and stores it in a variable named result.
# Print the variable, in a user-friendly string, formatted.
# print(f"The simple interest for a principal amount of ${principal_amount:,.2f} \
#                 at an interest rate of {interest_rate}% over a period of \
#                 {investment_time} years is: ${calculated_interest:,.2f}")

# the \ is a symbol you can use to split a string over multiple lines

# The {principal_amount:,.2f} format specifier formats the principal amount as a floating-point number with two decimal places, and includes commas as thousand separators.
# The {calculated_interest:,.2f} does the same for the calculated interest.
# Test your function with different values to ensure it works correctly.

def main():
    def calculate_interest(principle, rate, time):
        simple_interest = (principle * rate * time) / 100
        return simple_interest

    print()
    principle = float(input("Please enter princple amount: "))
    rate = int(input("Please enter the interest rate as a whole number: "))
    time = int(input("Please enter the investment time in whole years: "))
    print()
    result = calculate_interest(principle, rate, time)

    print(f"The simple interest for a principle amount of ${principle:,.2f} at an interest rate of {
          rate}% over a period of {time} years is: ${result:,.2f}")
    print()


main()
