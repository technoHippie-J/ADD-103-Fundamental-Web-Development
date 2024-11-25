# Accept five names from the user.
# Store these names in a list.
# Sort the list using the Bubble Sort algorithm.
# Finally, reverse the sorted list using a Python list method.
# Requirements:
# Your program should prompt the user to enter five names.
# Use a loop to accept each name and append it to a list.
# Implement the Bubble Sort algorithm to sort the list of names in ascending order.
# Print the sorted list.
# After sorting, use a Python list method to reverse the order of the list.
# Print the final reversed list to the console.

# Initialize empty list of names
names = []

print()
# Request user input of names, appending (adding) them to the list
for name in range(5):
    print("Please enter a name.")
    name = input("Name: ")
    names.append(name)
    print()

# Flag to track if a swap has occurred
swapped = True

# Convert to lowercase
for i in range(0, len(names)):
    names[i] = names[i].lower()

while swapped:
    swapped = False  # resets flag at start of each iteration, allows for exit if no swap occurs
    for i in range(len(names) - 1):
        # Compare adjacent elements
        if names[i] > names[i + 1]:
            swapped = True  # Requires a swap
            names[i], names[i + 1] = names[i + 1], names[i]  # swaps elements

# Regarding the above if statement, through asking ChatGPT to explain the while segment of code, I learned I could avoid converting to lowercase and back to uppercase by using the following:

# if names[i].lower() > names[i + 1].lower():

# This would have the effect of converting all names to lowercase during and within the loop, but would not affect the capitalization of the names outside of the loop. This line would make for more elegant code, but I'm leaving my program as is with this comment included for future reference.

# The ChatGPT conversation I referenced can be found here: https://chatgpt.com/share/66fc53ae-12e0-8013-8cf6-c36bc88500be

# Convert back to uppercase
for i in range(0, len(names)):
    names[i] = names[i].capitalize()

# Regarding the above line, str.capitalize() will capitalize the first letter of a string while leaving the rest lowercase. The str.uppercase() method will capitalize all letters in a string.
# I originally used str.uppercase() and encountered this problem, then searched on Google and found str.capitalize() at the following link: https://www.geeksforgeeks.org/string-capitalize-python/#
# I also found the methods str.title(), which would capitalize the first letter of each word but runs into issues when encountering anything other than groups of consecutive letters, and str.capwords() which I think uses str.split(), str.capitalize(), and str.join() to handle separating words, capitalizing them, then rejoining them back into a single string, as well as many, many other techniques for handling the problem.
# For my purposes here, str.capitalize() works fine. These methods and techniques were found here: https://stackoverflow.com/questions/1549641/how-can-i-capitalize-the-first-letter-of-each-word-in-a-string

# Print sorted
print(names)

# Reverse sorted list
names.reverse()

# Print reversed
print()
print(names)

print()
