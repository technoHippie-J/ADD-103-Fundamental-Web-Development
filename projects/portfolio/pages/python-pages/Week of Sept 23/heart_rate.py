# In this assignment, you will create a Python program to track your daily heart rate. The program will record the heart rate at different times of the day and calculate the average heart rate.

# Objective:
# Create a Python script to track heart rate readings taken at various times throughout the day and calculate the average heart rate.

# Requirements:
# Define Time Slots:
# Create a list named time_slots with different times of the day, such as "Morning", "Midday", "Afternoon", "Evening".

# User Input for Heart Rate:
# Use a loop to iterate over each time slot. For each time slot, use the input() function to ask the user to enter their heart rate ( in beats per minute). Convert this input to an integer.

# Storing Heart Rate Data:
# Create an empty list named heart_rates. For each time slot, append a sublist to heart_rates that contains the time slot and the corresponding heart rate.

# Calculate Average Heart Rate:
# Initialize a variable to keep track of the total heart rate. Use a loop to add up the heart rate recorded at each time slot. Calculate and print the average heart rate at the end.

print()
# initializes time list, heart rate empy list, and total hear rate container variable
time_slots = ["the Morning", "Midday", "the Afternoon", "the Evening"]
heart_rates = []
total_hr = 0

# loops through user entry for hr at each time
for time in time_slots:
    print(f"Please enter your heart rate from {
          time} in the format of beats per minute. ")
    rate = input("BPM: ")
    # adds time and hr to heart_rates list as a pair
    heart_rates.append([time, rate])
    total_hr += int(rate)  # adds previous total_hr total + rate to total_hr

# calculates average heart rate from 4 times of the day
avg_hr = total_hr / 4

print()
print(f"Your average heart rate for the day is {avg_hr}.")
print()
