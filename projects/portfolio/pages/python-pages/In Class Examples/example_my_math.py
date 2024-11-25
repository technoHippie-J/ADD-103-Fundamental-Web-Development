# Demonstrating math

# Addition
a = 10
b = 5
c = 12


print(4 + 5)
print(a + a)
print(12 + a)

# the following will not do a math operation
# as the quotes make the variable a string
# making it no longer recognized as a variable
print("a" + "a")

# Subtraction
print(c - b)

# using the variables alone will not present an error
# however it will not display as it is not meaningful
# to us due to not being within a print function
# however, once stored in a variable, it will display
# when the variable is included in a print function
aa = a+a
print("The variable aa holds the value", aa)

# if the comma is not included, a syntax error will be the result
# print("The variable aa holds the value" aa)

# when attempting to add a number to a string, there will be
# an error, but it will not be presented as a syntax error,
# but rather a runtime error presented as a TypeError
# print("The variable aa holds the value" + aa)

# however, doing so with a string will work, as python recognizes
# the variable to contain a string and can add the two together
# as strings
print("The variable aa holds the value" + str(aa))

# numbers hold more meaning when combined with words
print(a * a, "Multiplication")
print(a/b, "Division")
print(c//b, "Floor Division")
print(c % b, "Modulus")
