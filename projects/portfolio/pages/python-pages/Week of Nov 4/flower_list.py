

# import sys for sys.exit method
# import sys

# initialize list
flower_list = []


# request user input


def get_flower():
    flower = input("Enter: ")
    return flower

# add flower to list


def add_flower(flower):
    flower_list.append(flower)  # append user entry to list

# find flower if on list and report name and item number (index + 1), or inform flower is not on list


def find_flower(flower):
    try:
        # takes flower entry as parameter, indexes list to check presence, reports flower+index if present, or the list does not contain if not present using a try/except statement to do so
        i = flower_list.index(flower)
        print(
            f"\n|--- The list contains ({flower}) at location ({i + 1}) ---|")
    except ValueError:
        print(f"\n|--- The list does not contain ({flower}) ---|")
    return flower


# ammend list with add_flower() and check if user wants to add another


def add_to_list():
    print("\nPlease enter a flower: ")
    # call get_flower function and return result to var flower
    flower = get_flower().title()
    add_flower(flower)  # call add_flower function to add to list
    print(f"\n\n|--- Your entry of ({
          flower}) was successful ---|\n\n\nWould you like to add another? (y/n)")
    more = False  # set loop flag
    while more == False:
        try:
            query = input("Enter: ").lower()  # make lower to conform to reqs
            if query == "y":
                # set loop flags to True, leaving loop and moving on to if condition
                more = True
                done = False
            elif query == "n":
                # set done and more flags to leave loop and function, continues to if condition
                more = True
                done = True
            elif query != "y" and query != "n":
                raise ValueError(f"\n\n|--- I'm sorry, but ({
                                 query}) is not a valid entry ---|\n\nPlease enter 'y' for yes or 'n' for no.")
        except ValueError as e:
            print(f"\n{e}")

    # if user wants to add more, enter next recursion
    if more == True and done != True:
        # recursion loop
        add_to_list()

    if done == True:
        # once finished, sorts list with new entries, capitalizes their first letter each, then prints each item as a numbered list
        sort_n_display()

# sort the list, capitalize by title, print numbered list


def sort_n_display():
    flower_list.sort()
    # capitalize in Title format loop
    for i in range(len(flower_list)):
        flower_list[i] = flower_list[i].title()
    # print numbered list loop
    print("\n************")
    for index, item in enumerate(flower_list):
        print(f"{index + 1}: {item}")
    print("************")

# check if a flower is in the list function


def search_list():
    search = "y"  # set search loop flag
    while search == "y":
        print("\nEnter your search query: ")
        flower = get_flower()  # user input function
        flower = flower.title()  # capitalize first letter of flower name
        # call find flower function to display flower and its index number
        print(f"|--- ({find_flower(flower)}) ---|")
        print("\nWould you like to search for another? (y/n)")
        error = True  # set error flag
        # allow user to search for another or go back to main menu
        while error == True:
            more = input("Enter: ")
            try:
                if more == "y":
                    # set error flag to False to leave while loop, and continue to next iteration of parent loop
                    error = False
                    continue
                elif more == "n":
                    # set both loop flags to the exit conditions, completing function
                    search = "n"
                    error = False
                else:
                    raise ValueError(
                        f"\n\n|--- ({more}) is not a valid input ---|\n\nPlease enter either 'y' for yes, or 'n' for no.")
            except ValueError as e:
                print(f"\n{e}")

# find a flower based on its index number function


def find_index():
    search = "y"
    print(
        f"\n|--- The list currently contains ({len(flower_list)}) items ---|")
    while search == "y":
        print("\nEnter a number to find the corresponding flower: ")
        index = get_flower()  # use get_flower() for user input across search query types; would probably change the name moving forward to maybe "get_data()" or something similar
        try:
            index = int(index)  # convert input string to int
            index -= 1
            if 0 <= (index) <= len(flower_list):  # ensure index entry is valid
                # assign flower at the indexed position to var flower
                flower = flower_list[index]
                print(
                    f"\n--- The ({flower}) sits at item (#{index + 1}) ---\n")
            else:
                print(f"\n\n|--- ({index}) is not a valid index number ---|\n\nPlease enter a number greater than or equal to 0, and less than or equal to the total number of items in the list.\n\nRemember, the list currently contains |--- ({
                      len(flower_list)}) ---| items.")
        # if a non-numeric value was entered
        except ValueError:
            print(
                f"\n\n|--- ({index}) is an invalid input ---|\n\nPlease enter a numeric value\n")
        except IndexError:
            print(f"\n\n|--- ({index}) is outside the list's range ---|\n")

        print("\nWould you like to search for another? (y/n)")
        error = True  # error flag
        while error == True:
            more = input("Enter: ")
            try:
                if more == "y":
                    # set error flag to false, continue out of loop
                    error = False
                    continue
                elif more == "n":
                    # set search flag to no, set error flag to false
                    search = "n"
                    error = False
                else:
                    raise ValueError(
                        f"\n\n|--- ({more}) is not a valid input ---|\n\nPlease enter either 'y' for yes, or 'n' for no.")
            except ValueError as e:
                print(f"\n{e}")


def length():
    print(f"\nThe list is ({len(flower_list)}) items long.")


# main program


def main():
    # This variable would be used to keep track of how many times the program has been used to perform a test, resetting when the program closes. If we had learned how to manage files, this variable would be saved to a file and recalled at program startup, keeping track of the total uses over time.
    usage_counter = 0
    cont = False  # set continue flag for while loop
    while cont == False:
        print("\nThank you for using the Flower Dictionary service!\nPlease select from one of the following options by entering the menu item number.")
        error = True  # set error loop flag
        # main program functions
        while error == True:
            print("\n\t1) Register flower(s) in the dictionary.\n\t2) Search for flower(s) by name.\n\t3) Search for flower(s) by index.\n\t4) Display number of items in list.\n\t5) Display list")
            selection = input("\nEnter: ")
            try:
                if selection == "1":
                    # calls function, adds to usage_counter, and sets error flag to false to leave while loop, same for all 3 options with their respective functions
                    add_to_list()
                    usage_counter += 1
                    error = False
                elif selection == "2":
                    search_list()
                    usage_counter += 1
                    error = False
                elif selection == "3":
                    find_index()
                    usage_counter += 1
                    error = False
                elif selection == "4":
                    length()
                    usage_counter += 1
                    error = False
                elif selection == "5":
                    sort_n_display()
                    usage_counter += 1
                    error = False
                else:
                    # force raise ValueError when input != 1, 2, 3, 4, or 5
                    raise ValueError(
                        f"\n\n|--- ({selection}) was not a valid entry, try again ---|")
            except ValueError as e:
                print(f"\n{e}")
        print("\nWould you like to perform another operation?\nPlease enter 'y' for yes or 'n' to close the program.")
        error2 = True  # set choice flag
        # allows user to go back to main menu and perform another operation, or quit the program
        while error2 == True:
            # convert to lowercase for condition reqs
            more = input("\nEnter: ").lower()
            try:
                if more == "y":
                    # set choice flag to false, leaving loop
                    error2 = False
                elif more == "n":
                    # if I went further with the program, I would save the below variable to an external document so the program would be able to display how many times it was used before the last time the program was closed.
                    usage_counter = (
                        f"Operations before shutdown = {usage_counter}")
                    print(usage_counter)
                    print(
                        "\nThank you for using the Flower Dictionary Service.\nPress enter to exit.")
                    close = input("")
                    return
                    # OLDsys.exit()  # terminates the program
                else:
                    raise ValueError(
                        f"({more}) was not a valid entry, try again.")
            except ValueError as e:
                print(f"\n\n{e}")
            except IndexError:
                print("\n\nThat index number is outside the list's range.")


main()
