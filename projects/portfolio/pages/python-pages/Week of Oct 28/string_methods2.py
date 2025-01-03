# Python String Methods Practice

# TODO: Use the capitalize() method to capitalize the first letter of the string
# Example: "python" -> "Python"
string1 = "python"
# Your code here
string1 = string1.capitalize()
print(f"1. {string1}")

# TODO: Use the center() method to center the string in a string of specified width
# Example: "python" -> "  python  "
string2 = "python"
# Your code here
string2 = string2.center(25, '~')
print(f"2. {string2}")

# TODO: Use the endswith() method to check if the string ends with a specified substring
# Example: Check if "python" ends with "on"
string3 = "python"
# Your code here
print(f"3. {string3.endswith("on")}")

# TODO: Use the find() method to find the first occurrence of a substring in the string
# Example: Find the position of "th" in "python"
string4 = "python"
# Your code here
position = string4.find("th")
print(f"4. {position}")

# TODO: Use the isalnum() method to check if all characters in the string are alphanumeric
# Example: Check if "python3" is alphanumeric
string5 = "python3"
# Your code here
if string5.isalnum() == True:
    print("5. The string is alphanumeric")

# TODO: Use the isalpha() method to check if all characters in the string are alphabetic
# Example: Check if "python" is alphabetic
string6 = "python"
# Your code here
if string6.isalpha() != False:
    print("6. The string is alphabetic")

# TODO: Use the islower() method to check if all characters in the string are lowercase
# Example: Check if "python" is in lowercase
string7 = "python"
# Your code here
print(f"7. {string7.islower()}")

# TODO: Use the isspace() method to check if all characters in the string are whitespaces
# Example: Check if "   " is all whitespace
string8 = "   "
# Your code here
if string8.isspace() == True:
    print("8. Why didn't you type anything visible?")

# TODO: Use the isupper() method to check if all characters in the string are uppercase
# Example: Check if "PYTHON" is in uppercase
string9 = "PYTHON"
# Your code here
if string9.isupper() == True:
    print("9. Stop yelling at me!")

# TODO: Use the join() method to join elements of an iterable with the string as the separator
# Example: Join ["Python", "is", "fun"] with "-" as separator
iterable1 = ["Python", "is", "fun"]
separator = "-"
# Your code here
joined = separator.join(iterable1)
print(f"10. {joined}")

# TODO: Use the lower() method to convert all characters in the string to lowercase
# Example: Convert "PYTHON" to lowercase
string10 = "PYTHON"
# Your code here
lower = string10.lower()
print(f"10. {lower} has been made lower case.")

# TODO: Use the lstrip() method to remove leading characters (spaces by default)
# Example: Remove leading spaces from "  python"
string11 = "  python"
# Your code here
print(f"11. {string11.lstrip()} has had the leading spaces removed.")

# TODO: Use the rstrip() method to remove trailing characters (spaces by default)
# Example: Remove trailing spaces from "python  "
string12 = "python  "
# Your code here
print(f"12. {string12.rstrip()} has had the trailing spaces removed.")

# TODO: Use the replace() method to replace all occurrences of a substring with another substring
# Example: Replace "python" with "snake" in "I love python"
string13 = "I love python"
# Your code here
replaced = string13.replace("python", "snek")
replaced = replaced.replace("love", "step on")
replaced = replaced.replace("I", "Don't")
print(f"13. I've replaced the string \"{string13}\"...\n\twith \"{
      replaced}\" in three stages \n\t\tbecause it was fun.")

# TODO: Use the rfind() method to find the highest index of a substring
# Example: Find the highest index of "n" in "python"
string14 = "python"
# Your code here
found = string14.rfind("n")
print(f"14. The highest index of \"n\" in \"{string14}\" is {found}.")

# TODO: Use the split() method to split the string at a specified separator
# Example: Split "python-is-fun" at "-"
string15 = "python-is-fun"
# Your code here
print(f"15. {string15.split("-")}")

# TODO: Use the startswith() method to check if the string starts with a specified substring
# Example: Check if "python" starts with "py"
string16 = "python"
# Your code here
print(f"16. Does python start with py?\n\t-Let's find out........\n\t-{string16.startswith(
    "py")}...\n\t-Looks like \"string16.startswith(\"py\")\" \n\t  shows it to be True.")

# TODO: Use the strip() method to remove both leading and trailing characters (spaces by default)
# Example: Remove spaces from "  python  "
string17 = "  python  "
# Your code here
print(f"17. Before, it was ugly, like this: \n\t\"{
      string17}\"\n    But now, it's beautiful, like this: \n\t\"{string17.strip(" ")}\"")

# TODO: Use the swapcase() method to swap the case of all characters in the string
# Example: Swap case of "Python"
string18 = "Python"
# Your code here
print(f"18. This is how we write things in the real world:\n\t\"{
      string18}\"\n    But this is how we write things in swapcase land:\n\t\"{string18.swapcase()}\"")

# TODO: Use the title() method to convert the first character of each word to uppercase
# Example: Convert "python is fun" to title case
string19 = "python is fun"
# Your code here
print(f"19. The title of the film shall henceforth be known as:\n\t\"{
      string19.title()}\".")

# TODO: Use the upper() method to convert all characters in the string to uppercase
# Example: Convert "python" to uppercase
string20 = "python"
# Your code here
print(f"20. I guess {string20} isn't going out with\n\ta whisper...but with a bang.\n\t\t\"{
      string20.upper()}\"")

input(print("Press any key to exit..."))
