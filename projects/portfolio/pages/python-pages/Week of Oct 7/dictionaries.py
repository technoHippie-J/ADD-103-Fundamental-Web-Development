# Objective:


# Your mission is to create a Python program that uses a dictionary to translate letters into the NATO Phonetic Alphabet. This program will ask users for a word and then spell it out using the NATO codes.

# I would plan this program before attempting it. Here is what pseudocode would look like for this program:


# Start

# // Step 1: Create the NATO Phonetic Alphabet Dictionary
# Define nato_alphabet as a dictionary with each English alphabet letter as a key and its NATO phonetic term as the value
# // Example: {"A": "Alpha", "B": "Bravo", ..., "Z": "Zulu"}

# // Step 2: Develop the Spelling Program
# Define a function spell_word():
#     Prompt user for a word and store it in a variable 'user_word'
#     Convert 'user_word' to uppercase(to match dictionary keys)

#     For each letter in 'user_word':
#         Find the corresponding NATO phonetic term in nato_alphabet
#         Print the NATO phonetic term

# // Step 3: Incorporate a Main Function
# Define main():
#     Call the spell_word() function

# // Step 4: Test Your Program
# Call main()

# End
# Steps to Follow:
# Create the NATO Phonetic Alphabet Dictionary:

# Begin by constructing a dictionary in Python named nato_alphabet.
# Each key in this dictionary should be a letter of the English alphabet, and its corresponding value should be the NATO phonetic term. For example, {"A": "Alpha", "B": "Bravo", ...}.
# Here's a snippet of the NATO Phonetic Alphabet for reference:
# A - Alpha
# B - Bravo
# C - Charlie
# ...
# Z - Zulu
# You can find the full chart here Download here.
# Develop the Spelling Program:

# Write a function that prompts the user to input a word.
# The program should then iterate through each letter of the input word.
# For each letter, find the corresponding NATO phonetic term in your dictionary and print it out.
# Ensure your program can handle both uppercase and lowercase inputs.
# Incorporate a Main Function:

# Encapsulate your program logic within a main() function.
# This is a best practice in Python programming, making your code organized and more readable.
# Test Your Program:

# After completing your program, test it with various words to ensure it works correctly.
# Try both common and unusual words to thoroughly test the functionality.
# Example Output:
# If the user inputs the word "Hello", your program should output:

# Hotel
# Echo
# Lima
# Lima
# Oscar
# About this Assignment:
# This assignment should take approximately 1-2 hours of study and 60 minutes of coding.
# Late submissions will result in a 10% deduction per day, up to a maximum of 50%.
# Submit your program on GitHub and provide the link for assessment.
# See grading details in the rubric below.
# You may fix and resubmit your program within a week of when the assignment is graded.


def main():
    # creates dictionary
    nato_alphabet = {
        "A": "Alpha",
        "B": "Bravo",
        "C": "Charlie",
        "D": "Delta",
        "E": "Echo",
        "F": "Foxtrot",
        "G": "Golf",
        "H": "Hotel",
        "I": "India",
        "J": "Juliett",
        "K": "Kilo",
        "L": "Lima",
        "M": "Mike",
        "N": "November",
        "O": "Oscar",
        "P": "Papa",
        "Q": "Quebec",
        "R": "Romeo",
        "S": "Sierra",
        "T": "Tango",
        "U": "Uniform",
        "V": "Victor",
        "W": "Whiskey",
        "X": "X-ray",
        "Y": "Yankee",
        "Z": "Zulu"
    }

    # Function to request word, process it, and translate to NATO alphabet
    def word_request():
        print("Please enter a word.")
        user_word = input("Enter: ")
        # makes input uppercase
        user_word = user_word.upper()
        # iterates over each letter in the word, then accesses the dictionary and prints the value corresponding to the letter
        for letter in user_word:
            print(nato_alphabet[letter])

    # calls the function
    word_request()


# calls main function
main()
