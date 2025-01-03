# Objective:
# Develop a Python-based Madlib based on a song of your choice. The program should collect at least 8 different pieces of information from the user and incorporate them into the song using named arguments. The goal is to practice using functions, user input, and string manipulation in Python.

# Important Note:
# Choose any song you like for your madlib, but remember, no Rickrolling! Be creative and respectful in your song choice.

# Task:
# Select a Song: Choose a song that is well-known and suitable for a classroom setting. Avoid any song with inappropriate or offensive content.

# Identify Variables: Determine at least 8 different variables that the user will provide to customize the song. These could include names, adjectives, nouns, places, etc.

# Write the Function:

# Define a function named custom_song that takes at least 8 parameters corresponding to the variables you've identified.
# Use f-strings to incorporate these parameters into the song's lyrics.
# Ensure the function prints the customized song lyrics.
# Collect User Input:

# Write code to collect user input for each of the 8 variables.
# Use clear and descriptive prompts to guide the user.
# Call the Function:

# Call the custom_song function with the user inputs as named arguments.
# Ensure the order of arguments matches the parameters in your function definition

# Song: There's a Great Big Beautiful Tomorrow
# Songwriter: Rex Allen
# Used In: Carousel of Progress

# There's a great, big, beautiful tomorrow
# Shining at the end of every day
# There's a great, big, beautiful tomorrow
# And tomorrow's just a dream away

# Man has a dream and that's the start
# He follows his dream with mind and heart
# And when it becomes a reality
# It's a dream come true for you and me

# So there's a great, big, beautiful tomorrow
# Shining at the end of every day
# There's a great, big, beautiful tomorrow
# Just a dream away

# Modified Song

# There's a (variable F - adjective), (variable G - adjective), (variable H - adjective) (variable A - noun)
# Shining at the end of every (variable B - noun)
# There's a (variable F - adjective), (variable G - adjective), (variable H - adjective) (variable A - noun)
# And (variable A - noun)'s just a (variable C - noun) away

# Man has a (variable C - noun) and that's the start
# He follows his (variable C - noun) with (variable D - noun) and (variable E - noun)
# And when it becomes a reality
# It's a (variable C - noun) come true for you and me

# So there's a (variable F - adjective), (variable G - adjective), (variable H - adjective) (variable A - noun)
# Shining at the end of every (variable B - noun)
# There's a (variable F - adjective), (variable G - adjective), (variable H - adjective) (variable A - noun)
# Just a (variable C - noun) away


def main():
    var_a = input("Please enter a noun: ")
    print()
    var_b = input("Please enter another noun: ")
    print()
    var_c = input("Please enter another noun: ")
    print()
    var_d = input("Please enter another noun: ")
    print()
    var_e = input("Please enter another noun: ")
    print()
    var_f = input("Please enter an adjective: ")
    print()
    var_g = input("Please enter another adjective: ")
    print()
    var_h = input("Please enter one more adjective: ")

    def custom_song(var_a, var_b, var_c, var_d, var_e, var_f, var_g, var_h):
        print(f"There's a {var_f}, {var_g}, {var_h} {var_a}")
        print(f"Shining at the end of every {var_b}")
        print(f"There's a {var_f}, {var_g}, {var_h} {var_a}")
        print(f"And {var_a}'s just a {var_c} away.")
        print()
        print(f"Man has a {var_c} and that's the start")
        print(f"He follows his {var_c} with {var_d} and {var_e}")
        print(f"And when it becomes a reality")
        print(f"It's a {var_c} come true for you and me")
        print()
        print(f"So there's a {var_f}, {var_g}, {var_h} {var_a}")
        print(f"Shining at the end of every {var_b}")
        print(f"There's a {var_f}, {var_g}, {var_h} {var_a}")
        print(f"Just a {var_c} away!")
        print()

    print()
    custom_song(var_a, var_b, var_c, var_d, var_e, var_f, var_g, var_h)


main()

# while I understand "varA, varB..." is not the most meaningful variable name,
# it seemed to be appropriate enough for this type of assignment, since
# otherwise it'd end up with "noun01, noun02..." etc, which wouldn't really be
# any more meaningful than how it is now. The only way I could see to make
# them more meaningful would be to include location, ie: verse, line
# so they would look like this: noun_v01_l03 or something similar, which might
# be more meaningful, but is also much longer. For the purposes of this
# assignment, varA, etc... is sufficient I think, but for longer, more complex
# programs, I would use the more detailed name that includes location information.

# forgot camel-back notation isn't used in this class, so I came back in and
# edited the variables to all be lowercase.


# go back later to modify variables to more meaningful name using original words
