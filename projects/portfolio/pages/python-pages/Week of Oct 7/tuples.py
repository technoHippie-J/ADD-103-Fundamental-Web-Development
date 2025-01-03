# Create a tuple named programming_classes with these classes: 'Intro to Python', 'Advanced Python', 'Database Essentials', 'Web Development Basics', 'Data Structures in Python', 'Web Design Fundamentals'.
# Write a program that uses a for loop to print each class in the tuple.
# Use the len function to print how many classes are in the tuple.
# Make sure to use a main function for this program.
# Try this out, and you'll get a good grasp of how tuples work in Python!


# About this Assignment:
# This assignment should take approximately 1-2 hours of study and 25 minutes of coding.
# Late submissions will result in a 10% deduction per day, up to a maximum of 50%.
# Submit your program on GitHub and provide the link for assessment.
# See grading details in the rubric below.
# You may fix and resubmit your program within a week of when the assignment is graded.


def main():
    print()
    programming_classes = ("Intro to Python", "Advanced Python", "Database Essentials",
                           "Web Development Basics", "Data Structures in Python", "Web Design Fundamentals")
    for p_class in programming_classes:
        print(p_class)
    length = len(programming_classes)
    print(f"There are {
          length} classes required for the programming certificate.\n")


main()
