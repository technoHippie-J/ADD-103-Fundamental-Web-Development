"""
    finding the ASCII values of a string
    """


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
