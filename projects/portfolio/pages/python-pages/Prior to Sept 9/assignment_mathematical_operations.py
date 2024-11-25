# the goal of this assignment is to solve a mathematical
# problem and display the results with the print statement
# make sure to use appropriate literals, mathematical
# operators, and escape sequences for formatting.

length = 10
width = 20
area = length * width

# the use of \n moves the following output to a new line
# and the use of \t indents the output with a tab
# using these escape sequences outside of quotes (as a string)
# causes a syntax error, preventing the program from running
# this is an error I ran into while writing this program
print("\n\tI think the following looks ugly:")
print("\n\t The area of the rectangle with:\n\t a length of",
      length, "and\n\t a width of ", width, "\n\t is         ", area, "\n")

# the above is how I read the requirements on the assignment page
# however below is how I think it reads better
print("\n\tI think the following looks better:")
print("\n\tThe area of the rectangle with a length of",
      length, "and a width of", width, "is", area, "\n")
