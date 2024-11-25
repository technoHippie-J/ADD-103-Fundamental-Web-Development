# Welcome to your Python assignment! This task will help you practice working with lists, user input, and basic calculations. Follow the steps below:

# Create a List: Start by creating a list named days that includes all seven days of the week.
# Initialize an Empty List: Create an empty list called steps. This will store the number of steps taken each day.
# User Input: Using a loop, ask the user to enter the number of steps they took for each day, based on your days list. For example, "How many steps did you take on Monday?"
# Store Steps: Append the user's input (number of steps) to the steps list for each day.
# Display Daily Steps: Show the user the steps recorded for each day.
# Total Steps: Calculate and display the total number of steps taken in the week.
# Average Steps: Create a variable named average to calculate the average steps taken. Use the formula: average = round(total / len(steps)). Display the average steps.
# Remember to test your program to ensure it runs correctly.

# initializes two lists, one for week days, one empty, and an empty
# variable for total steps
days = ["Monday", "Tuesday", "Wednesday",
        "Thursday", "Friday", "Saturday", "Sunday"]
steps = []
total = 0

print()
# for loop asking for daily steps, then ammending the steps list
# with the entry in relation to same index of the days list, then
# creates a variable that adds each day's steps to itself for the
# weekly total
for day in days:
    day_steps = int(input(f"How many steps did you take on {day}? "))
    steps.append(day_steps)
    total += day_steps

# for each index position in the days list, assigns that position
# to the day (from days), and step (from steps) variables,
# then displays to useer
print()
for i in range(7):  # changed from len(days) to (7) because we know the length of the list
    day = days[i]
    step = steps[i]
    print(f"You took {step} steps on {day}.")

# calculate the average daily steps
average = round(total/len(steps))

# displays total steps and average daily steps
print()
print(f"You have taken {total} steps this week.")
print(f"You have taken an average of {average} steps per day.")

# displays steps list for reference
print()
print(f"The appended list, for reference: {steps}")
print()
