# For Lesson - Scope

# Objective: Create a BMI calculator that takes a user's weight and height, calculates their BMI, and then categorizes their BMI into underweight, normal weight, overweight, or obese.

# Requirements:
# This should be done inside of a main function. The conversion variables should be above main because they are global.
# Input:
# Ask the user to enter their weight in pounds.
# Ask the user to enter their height in inches.
# Conversion to Metric:
# These variables should be global and constant (at the top of the page and ALL CAPS)
# Convert weight from pounds to kilograms (1 pound = 0.453592 kilograms).
# Convert height from inches to meters (1 inch = 0.0254 meters).
# BMI Calculation:
# Calculate the BMI using the formula: bmi = weight (kg) / (height (m) * height (m)).
# Ensure the calculation is done using metric units.
# BMI Categories:
# Underweight: bmi < 18.5
# Normal weight: 18.5 ≤ bmi < 24.9
# Overweight: 25 ≤ bmi < 29.9
# Obese: bmi ≥ 30
# Output:
# Display the calculated BMI with two decimal places.
# Display the BMI category based on the calculated BMI.
# Documentation:
# Comment the code to explain different sections or important lines.
# Sample Results:
# Enter your weight in pounds: 154
# Enter your height in inches: 68
# Your BMI is: 23.43
# You are in the normal weight category.


# About this Assignment:
# This assignment should take approximately 1-2 hours of study and 45 minutes of coding.
# Late submissions will result in a 10% deduction per day, up to a maximum of 50%.
# Submit your program on GitHub and provide the link for assessment.
# See grading details in the rubric below.
# You may fix and resubmit your program within a week of when the assignment is graded.


# define global variables, conversion rates in this case
POUNDS_TO_KG = 0.453592
INCHES_TO_M = 0.0254


def main():
    # ask user for weight and height
    print("\nPlease enter your weight in pounds.")
    weight = float(input("Enter: "))
    print("Now please enter your height in inches.")
    height = float(input("Enter: "))

    # convert pounds/inches to kg/meters
    weight_kg = weight * POUNDS_TO_KG
    height_m = height * INCHES_TO_M

    # calculate bmi
    bmi = weight_kg / (height_m ** 2)

    # display BMI then inform user of weight category they fit into
    print(f"Your BMI is {bmi:.2f}")
    if bmi < 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi < 24.9:
        print("You are considered normal weight.")
    elif bmi >= 25 and bmi < 29.9:
        print("You are overweight.")
    elif bmi >= 30:
        print("You are obese.")

    # add line to leave space between final output and bottom of terminal
    print()


main()
