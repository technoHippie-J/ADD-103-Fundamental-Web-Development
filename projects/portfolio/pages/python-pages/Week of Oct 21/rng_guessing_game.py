# Assignment Objectives:
# Use the random module to generate a random number.
# Implement a while loop to allow continuous guessing until the correct number is guessed.
# Use the abs() function to determine the difference between the guess and the actual number.
# Provide feedback based on the proximity of the guess to the actual number.

# Task Details:
# Import the random module and use it to generate a random number between 1 and 100.
# Put the rest of the code in the main function
# use try and except statements. The except statement should look for ValueError
# Write a while loop that allows the user to enter a guess for the number.
# Inside the loop, use the abs() function to calculate the absolute difference between the guess and the actual number.
# Based on this difference, provide the following feedback to the user:
# If the difference is within 5, print "Very Hot".
# If the difference is within 15, print "Hot".
# If the difference is within 25, print "Cool".
# If the difference is more than 25, print "Cold".
# The loop should continue until the user guesses the correct number.
# Make sure to call the main function!
# After completing the program, upload it to your GitHub repository.
# Submit the link to your GitHub repository in Canvas.

# Additional Notes:
# The abs() function is a built-in Python function used to calculate the absolute value of a number. The absolute value of a number is its distance from zero on the number line, regardless of direction. For example, abs(-5) and abs(5) both return 5.

"""
    Enumerate source: https://www.w3schools.com/python/ref_func_enumerate.asp

"""

import random

# If I wanted to create a program that contained multiple games, I could create the games as function and call them within main, like below. Combined with a loop, code within the main function can act as a home menu for the user to select the game they'd like to play.

# Included games
games = ["Guessing Game", "Hangman", "Tic Tac Toe",
         "Rock Paper Scissors", "Simon Says"]

# Guessing Game


def guessing_game():
    print("Welcome to the Random Number Guessing Game!")
    # flag to play again
    play_again = True
    while play_again == True:
        print()
        # generate random number
        target = random.randint(0, 101)
        print("Please guess a number.")
        guess = int(input("Enter: "))
        print()
        # For testing purposes, the target number will be printed
        print("*** For Meri's testing purposes, the target number is:",
              target, " ***\n")
        # primary game loop
        while guess != target:
            if guess != target:
                if abs(guess - target) <= 5:
                    print("Very Hot")
                    guess = int(input("Try again: "))
                elif abs(guess - target) <= 15:
                    print("Hot")
                    guess = int(input("Try again: "))
                elif abs(guess - target) <= 25:
                    print("Cool")
                    guess = int(input("Try again: "))
                else:
                    print("Cold")
                    guess = int(input("Try again: "))
            else:
                print()
        print()
        print("Congratulations! You guessed the correct number!\nThank you for playing the Random Number Guessing Game!\n\nWould you like to play again? Enter 1 for Yes or 0 for No.")
        print()
        # check if user wants to play again
        play_again = int(input("Enter: "))
        if play_again == 0:
            print("\nThank you for playing! \nThe game will now close\n")

# Hangman game


def hangman():
    print("Welcome to Hangman!\n")
    print("***This game is under construction. Please check back later.*** \n\nPlease hit any key to return to the main menu...")
    input()

# Tic Tac Toe game


def tic_tac_toe():
    print("Welcome to Tic Tac Toe!\n")
    print("***This game is under construction. Please check back later.*** \n\nPlease hit any key to return to the main menu...")
    input()

# Rock Paper Scissors game


def rock_paper_scissors():
    print("Welcome to Rock Paper Scissors!\n")
    print("***This game is under construction. Please check back later.*** \n\nPlease hit any key to return to the main menu...")
    input()

# Simon Says game


def simon_says():
    print("Welcome to Simon Says!\n")
    print("***This game is under construction. Please check back later.*** \n\nPlease hit any key to return to the main menu...")
    input()

# Main function


def main():
    # flag to end program
    end = False
    # loop to display menu
    while end == False:
        print("\n|-_Game Menu_-|\n")
        print(
            "Please select a game to play by entering \nthe number next to your selection.\n")
        # Enumerate the games list to display the games in a numbered list
        for i, game in enumerate(games):
            print(f"{i + 1}. {game}")
        print("0. Exit")
        print()
        choice = input("Enter: ")
        print()
        # If the user selects a game, the corresponding function containing the game loop will be called
        if choice == "1":
            guessing_game()
        elif choice == "2":
            hangman()
        elif choice == "3":
            tic_tac_toe()
        elif choice == "4":
            rock_paper_scissors()
        elif choice == "5":
            simon_says()
        # If the user selects 0, they will be prompted to confirm if they want to exit the program.
        elif choice == "0":
            print("Are you sure you want to exit? \nEnter 1 for Yes or 0 for No.\n")
            end = int(input("Enter: "))
            print("\nThank you for playing! \nThe program will now close\n")
        # If the user enters a number that is not in the range of the games list, they will be prompted to try again.
        elif choice != range(0, 5):
            print("\nInvalid selection. Please try again.")


# Call main function
main()
