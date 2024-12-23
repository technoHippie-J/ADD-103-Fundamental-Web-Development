# Objective: Develop a program to manage ticket sales for an event.

# Context: You are in charge of ticket sales for a special event. The venue has 20 seats, each uniquely numbered from 1 to 20. Your task is to create a system that tracks and updates the availability of seats as they are sold.

# Assignment Steps:


# Initialize the Seating List:

# Create a list in your program representing the 20 seats. This list should initially include all seat numbers(1-20).
# Display Available Seats:

# Write code to display the list of available seats to the customer. This list should update as seats are sold.
# Implement the Ticket Purchase Process:

# Prompt the customer to select a seat by entering its number.
# Include instructions in your prompt, indicating that the customer should enter '0' to finish their purchase.
# Update Seat Availability:

# Once a seat is selected, remove it from the list of available seats.
# After each selection, display the updated list of available seats.
# Continue this process until the customer enters '0', indicating they are done buying tickets.
# Ensure User-Friendly Interaction:

# Your program should handle inputs gracefully. If a customer selects a seat that doesn't exist or is already sold, display a friendly message and prompt them to choose again.
# Test Your Program:

# Run your program to ensure it works as expected. Try different scenarios, such as selling all seats, selling a few seats, and entering invalid seat numbers.

available = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
             11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
sold = []  # For future addition of a "return ticket" loop
seats = []  # For future addition of user01, user02, etc...
users = []  # Creates user list
selected = 0  # Seat selected by user
confirm = 1  # Confirms purchase
purchased = 0  # Counter for final statement
user = 0

# I have to decide how to increment user01.
# I think I can use lists to save users then
# check if they exist so that the program
# can remember users and their purchases.
# Attempt after completing nested list assignment.

# keeps the loop going until the user has indicated they are finished or when there are still seats available for purchase.
while len(available) >= 0:
    finished = False  # Initialize/toggle flag to default state
    print("Hello! If you are a new user, please enter your username:")
    # This line requires incremental user entry with checking for existing user
    user = input(print("Username: "))
    users.append(user)  # adds username to the users list
    print(".\n")*3
    if user in users:
        print("Hello", user, "\nWould you like to purchase more tickets?")
        buy_more = input(print("Yes or No?"))
        buy_more = buy_more.lower()
        if buy_more == "yes":
            print()
        elif buy_more == "no":
            # testing if this will skip the rest of the while loop and return to the start of the program for next iteration. Found here:
            continue
    else:
        print("Thank you for registering,", user, "\n")
    while finished != True and len(available) >= 1:
        # if there are any seats left, continue the loop
        if len(available) != 0:
            print("The following seats are available:", available)
            print()
            print("Which seat from the above available list would you like to purchase?")
            selected = int(input("Seat: "))
            print()
            # checks if the selected seat is in the list of available
            if selected in available:
                print("You have selected seat", selected,
                      "\n\nIf this is correct, please enter the number 0 to complete your purchase, \notherwise enter the number 1 to go back.\n")
                confirm = int(input("Confirm? "))
                # if user wants to complete purchase:
                #   - adds sold seat to the sold and seats lists (seats being used to
                #       track seperate users purchases, while sold tracks total seats
                #       purchased between users)
                #   - removes sold seat from available list
                #   - adds to the purchased counter
                #   - asks user if they want to buy another
                if confirm == 0:
                    sold.append(selected)
                    seats.append(selected)
                    users.append([user, selected])
                    available.remove(selected)
                    purchased += 1
                    print()
                    print(
                        "Thank you for your purchase, your payment method has been charged.\n")
                    print(
                        "Would you like to purchase another seat?\n***Enter 0 for Yes, or 1 for No.***")
                    finished = int(input("Buy another? "))
            # informs user when a seat is unavailable
            elif selected in sold:
                print("I'm sorry, but that seat is not available.")
            elif selected not in range(1, 20):
                print("I'm sorry, but that seat does not exist.")
        elif len(available) == 0:
            print()
            print("I'm sorry, there are no remaining available tickets.")

    if purchased > 1:
        print()
        seats.sort()
        print("You have purchased seats", seats,
              "\nWe appreciate your patronage.")
    elif purchased == 1:
        print()
        print("You have purchased seat", seats,
              "\n\nWe appreciate your patronage.")

print()
print("The remaining seats are still available:", available)
print("The following seats were sold to the last user:", seats)
print("The following seats have been sold:", sold)
