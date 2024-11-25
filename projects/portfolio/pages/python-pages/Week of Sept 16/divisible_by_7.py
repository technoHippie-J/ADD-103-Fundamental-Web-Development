# In this assignment, you will write a Python program to identify and print all the numbers divisible by 7 that fall between 1 and 300. This task will help you practice using loops and conditional statements in Python.

# Objective:
# Your program should iterate through the numbers 1 to 300. For each number, it should check if the number is divisible by 7. A number is divisible by 7 if the remainder is 0 when the number is divided by 7. This can be checked using the modulus operator ( % ) in Python.

# Requirements:
# Use a for loop to iterate through the range of numbers from 1 to 300.
# Inside the loop, use an if statement to check if a number is divisible by 7. To do this, use the modulus operator ( % ) and compare the remainder with 0.
# If a number is divisible by 7, print that number.
# Ensure your program outputs each qualifying number on a separate line.

# -------------

for i in range(1, 301):    # 1-301 so range is inclusive of 300, even if not displayed
    if i % 7 == 0:         # checks if the remainder from dividing by 7 is 0
        print(i)           # displays the iteration to screen
