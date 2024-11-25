# Debt
# asks user how much debt they have, and how much of it they pay each month
print("Do you have any debt? \nPlease format your response as 'Yes' or 'No'")
has_debt = input("Entry:  ")
has_debt = has_debt.lower()  # converts to lowercase
print()

# if else: if user has debt, program asks how much they have and how much of it they pay each month, else if user
# does not have debt, thanks the user for response and moves on to the next question
if has_debt == "yes":
    print("How much debt to you have? \nPlease format your response with two decimal places, ie: 999.99")
    initial_debt = float(input("Entry:  "))
    print()
    print(f"Thank you for your response. I understand that you have ${
          initial_debt:,.2f} in debt.")
    print("How much of your debt do you pay off each month? \nPlease provide your response as a percentage rounded to the nearest whole number.")
    debt_percentage_paid = float(input("Entry:  "))
    print()
    print(f"Thank you for your response. I understand that you pay {
          debt_percentage_paid:.2f}% of your debt each month.")
else:
    print("Thank you for your response. I understand that you are a societal anomaly.")
print()

# calculates the total amount of debt paid each month based on the percentage paid and initial debt entered by the user
# initial_debt = y
# debt_percentage_paid = x
# monthly_debt_paid = z
# x/100 = z/y
# (x*y)/100=z
monthly_debt_paid = ((initial_debt * debt_percentage_paid) / 100)

# tells the user the dollar amount of their debt they pay each month
print(f"For your reference, you will pay ${
      monthly_debt_paid:,.2f} towards your total debt this month.\n")
