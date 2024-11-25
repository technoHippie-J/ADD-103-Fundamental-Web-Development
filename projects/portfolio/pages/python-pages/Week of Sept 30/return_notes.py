# Wednesday Notes


def add_numbers(number1, number2):
    # add two numbers together
    total = number1 + number2
    return total


print()
# Using the function
result = add_numbers(5, 3)
print("The sum is:", result)

# return the divisor and remainder


def division(num1, num2):
    whole = num1 // num2
    remainder = num1 % num2
    return whole, remainder


whole, remainder = division(12, 7)
print(f"The answer is {whole} with a remainder of {remainder}")
print()


def division(num1, num2):
    whole = num1 // num2
    remainder = num1 % num2
    return whole, remainder


# the return variables are passed to a new spot in memory, they do
# not refer to the same spot in memory
w, r = division(12, 7)
print(f"The answer is {whole} with a remainder of {remainder}")
print()
