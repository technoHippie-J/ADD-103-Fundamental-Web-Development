# Step-by-Step Instructions:

# Start your Python script: Open your Python environment and start a new script. Make sure to use a main() function.
# Prompt for User Input: Use the input() function to ask the user to enter a character.
# user_input = input("Enter a character: ")
# Validate the Input: Implement a loop to ensure the input is only one character. Use the len() function to check the length of the input.
# while len(user_input) != 1:
#     print("Please enter exactly one character.")
#     user_input = input("Enter a character: ")
# Explain that the loop will continue asking for input until the user enters exactly one character.
# Convert to ASCII Value: Once a valid character is received, use the ord() function to convert the character to its ASCII value.
# ascii_value = ord(user_input)
# Display the Result: Print the ASCII value to the user.
# print(f"The ASCII value of {user_input} is {ascii_value}")
# Test Your Program: Run your script and input various characters to ensure it works correctly.
# Submit Your Work: Upload the code to GitHub and hand in a link to the code.

def main():
    user_input = input("Enter a character: ")
    while len(user_input) != 1:
        print("Please enter exactly one character.")
        user_input = input("Enter a character: ")
    ascii_value = ord(user_input)
    print(f"The ASCII value of {user_input} is {ascii_value}")
    # for fun, let's convert an ASCII value to a character
    asc = int(input("Please enter an ascii value: "))
    character = chr(asc)
    print(f"That character would be {character}")


main()
