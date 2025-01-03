"""
This script collects the titles of books from a user, stores them in a list, sorts them, then displays the list for the user.

"""
# create global variable COLLECTION
COLLECTION = []
BUGGED = False

# define function to handle title entry


def title_request():
    title = input("Enter title: ")
    title = title.lower()  # convert title to lowercase
    return title

# define function to handle request cycle


def request_cycle():
    global COLLECTION
    while len(COLLECTION) < 10:
        done = False  # begin loop complete flag
        print("Please enter the title of a book you would like to add to the list.")
        title = title_request()
        COLLECTION.append(title)  # add title to COLLECTION
        COLLECTION.sort()  # sort COLLECTION
        done = False  # begin loop complete flag
        error_count = 0  # error count for input validation
        # begin "add more"/error handling loop
        while not done:
            if len(COLLECTION) == 10:
                break
            if error_count == 0:
                print()
                print("Thank you for your entry.\n")
            print("Would you like to add another title? (y/n): ")
            try:
                confirm_add = input("Enter: ")
                # removes edge spaces and makes lowercase
                confirm_add = confirm_add.strip().lower()
                # if input is not a letter, raise error
                if confirm_add.isalpha() == False:
                    error_count += 1
                    raise ValueError
                # if input is not 'y' or 'n', raise error
                elif confirm_add != "y" and confirm_add != "n":
                    error_count += 1
                    raise ValueError
                # error escape
                else:
                    # reset error flag to 0
                    error_count = 0
                    # consequences of entry
                    if confirm_add == "n":
                        done = True  # end loop
                    # if user wants to add another title and the list contains less than 10
                    elif confirm_add == "y" and len(COLLECTION) < 10:
                        print()
                        print(
                            "Please enter the title of a book you would like to add to the list.")
                        title = title_request()
                        COLLECTION.append(title)  # add title to COLLECTION
                        COLLECTION.sort()  # sort COLLECTION
                    elif confirm_add == "y" and len(COLLECTION) == 10:
                        done = True
            # error handling for incorrect input characters
            except ValueError:
                print()
                print("Invalid entry. Please enter only the letter 'y' or 'n'.\n")

    print("You have entered all 10 titles!")
    print("Please wait while we sort your titles...\n")
    return COLLECTION


def main():
    print()
    print("Book Title Collecto-Matic 3000")
    print("------------------------------\n")
    print("Today, we will enter 10 book titles into a collection and sort them for you.\n")
    request_cycle()
    print("Thank you for your input. Here are the titles you entered, sorted:\n")
    # print each title in COLLECTION on a new line
    for title in COLLECTION:
        title = title.title()  # capitalize each word in title
        print(title)
    print()


main()
