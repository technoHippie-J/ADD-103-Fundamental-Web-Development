# working with and formatting numbers
# variables

hamburger = 3.99
cheese_burger = 4.99
soda = .99
tax = .02

total = (hamburger * 2) + cheese_burger + (2 * soda)
taxed = total * tax
grand_total = total + taxed

print("\n\nYou ordered:\n")
print(f"Two hamburgers at ${hamburger} each.")
print(f"One cheeseburger at ${cheese_burger} each.")
print(f"Two sodas at ${soda} each.")
print(f"For a total of: ${total:.2f}")
print(f"With a tax of: ${taxed:.2f}")
print(f"\nYou owe: ${grand_total:.2f}\n\n")
