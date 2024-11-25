# In this exercise, you will practice using logical operators ( and , or , not) in Python. Your task is to create a program that prompts the user for two integer inputs and then demonstrates the use of these operators.

# User Input: Start by asking the user to input two distinct integers.
# Logical Operators: Implement six different logical comparisons using the input integers. Include two examples for each of the following operators:
# and
# or
# not
# Display Results: For each comparison, print both the logical statement and its result.
# Guidelines for Logical Comparisons:
# Ensure that your comparisons are meaningful and not too obvious(e.g., avoid comparisons like num1 == num1).
# Try to use comparisons that could yield different results based on user input.

# ---------------

print()
int_a = int(input("Please enter an integer: "))
int_b = int(input("Please enter another integer: "))
print()

print("Both numbers are greater than 0: ", (int_a > 0 and int_b > 0))
print("Both numbers are greater than 100: ", (int_a > 100 and int_b > 100))
print("Either number is even?", (int_a % 2 == 0 or int_b % 2 == 0))
print("Either number is less than 100?", (int_a < 100 or int_b < 100))

if not int_a == int_b:
    print("First number is not equal to second number: ", (int_a != int_b))
else:
    print("First number is not equal to second number: ", (int_a != int_b))

if not int_a == 0:
    print("Number 1 is not 0: ", (int_a != 0))
else:
    print("Number 1 is not 0: ", (int_a != 0))
print()

# Today, I learned that coding on so little sleep is probably not a good idea...
# Below is what I just did before realizing every pairing was redundant *facepalm*

# if int_a > 0 and int_b > 0:
#     print("Both numbers are greater than 0: ", (int_a > 0 and int_b > 0))
# elif int_a <= 0 or int_b <= 0:
#     print("Both numbers are greater than 0: ", (int_a > 0 and int_b > 0))

# if int_a > 100 and int_b > 100:
#     print("Both numbers are greater than 100: ",
#           (int_a > 100 and int_b > 100))
# elif int_a <= 100 or int_b <= 100:
#     print("Both numbers are greater than 100: ",
#           (int_a > 100 and int_b > 100))

# if int_a % 2 == 0 or int_b % 2 == 0:
#     print("Either number is even?", (int_a % 2 == 0 or int_b % 2 == 0))
# else:
#     print("Either number is even?", (int_a % 2 == 0 or int_b % 2 == 0))

# if int_a < 100 or int_b < 100:
#     print("Either number is less than 100?", (int_a < 100 or int_b < 100))
# else:
#     print("Either number is less than 100?", (int_a < 100 or int_b < 100))

# if not int_a == int_b:
#     print("First number is not equal to second number: ", (int_a != int_b))
# else:
#     print("First number is not equal to second number: ", (int_a != int_b))

# if not int_a == 0:
#     print("Number 1 is not 0: ", (int_a == 0))
# else:
#     print("Number 1 is not 0: ", (int_a == 0))

# print()
