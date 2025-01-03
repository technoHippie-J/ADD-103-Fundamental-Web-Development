# Instructions:

# Start with Function Definitions:

# Begin by defining two functions: square and circle.
# Each function should take one parameter. For square, name the parameter side. For circle, name it radius.
# Write the square Function:

# Inside the square function, calculate the area of a square. Remember, the area of a square is the side length squared(side * side).
# Use the print function to display the result. The output should be: "The area of the square is [result] square units." Replace[result] with the actual calculated area.
# Make sure to convert the numerical result to a string using str() before concatenating it with other strings.
# Write the circle Function:

# In the circle function, calculate the area of a circle using the formula: area = π * radius * radius. You can use 3.14 for π(pi).
# Display the result using print, similar to the square function. The output should be: "The area of the circle is [result] square units."
# Test Your Functions:

# After defining both functions, test them by calling each one with a number of your choice.
# For example, you can call square(4) and circle(5), but feel free to use any positive numbers.
# Run Your Program:

# Execute your program to see the output.
# Ensure that the output correctly displays the areas for both the square and the circle with the numbers you chose.
# Tips:

# Pay attention to the syntax, especially the indentation and the use of parentheses and colons.
# Remember to use the print function to display the results.
# Sample Results: (if you pass 4 and 5, you should use different numbers)

# The area of the square is 16 square units.
# The area of the circle is 78.5 square units.

PI = 3.141592653589793238

# function containing formula for the area of a square


def square(side):
    area = (side ** 2)
    print(f"The area of the square is {area} square units.")

# function containing formula for the area of a cirlce


def circle(radius):
    area = PI * (radius ** 2)
    print(f"The area of the circle is {area} square units.")


def main():
    # get length of side and radius
    print()
    side = float(input("Please enter the length of the square's sides: "))
    radius = float(input("Please enter the circle's radius: "))
    print()

    # call functions using input variables
    square(side)
    print()
    circle(radius)
    print()


main()
