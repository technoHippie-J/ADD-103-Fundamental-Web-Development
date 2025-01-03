# assignment budget breakdown calculator
# this program will calculate the budget breakdown for a
# given a set of monthly expenditures

# Requirements:
#  Design a Python program that prompts users to enter their total budget and amounts for different spending categories
#   Housing(rent or mortgage)
#   Utilities
#   Groceries
#   Transportation
#   Health Care
#   Personal Care
#   Clothing
#   Debt
#   Calculate the percentage of the total budget spent in each category.
#   Display the results in a user-friendly format, clearly showing the budget breakdown. (use f strings)
#   Ensure your code is well-commented to explain the functionality of different sections.

# variables - the numberical variables used by the program and
#    their initial states should be defined at the top of the
#    program.
housing_cost = float(0)
isp_cost = float(0)
electric_cost = float(0)
water_cost = float(0)
gas_cost = float(0)
cell_cost = float(0)
utilities_cost = float(isp_cost + electric_cost +
                       water_cost + gas_cost + cell_cost)
food_cost = float(0)
petrol_cost = float(0)
public_transport_cost = float(0)
car_insurance_cost = float(0)
transportation_cost = float(
    petrol_cost + car_insurance_cost + public_transport_cost)
health_insurance_cost = float(0)
healthcare_cost = float(0)
personal_care_cost = float(0)
clothing_cost = float(0)
initial_debt = float(0)
monthly_debt_paid = float(0)

# to add a quintuple space at the top
print("\n" * 5)


# start of user interaction portion of the program

# asks how user is feeling
print("Hello, how are you feeling today? \nPlease format your answer as either 'Good' or 'Bad'")
abstract_feeling = input("Entry:  ")
abstract_feeling = abstract_feeling.lower()
print()

# asks user to quantify their subjective experience of that feeling
print("On a scale of 1-10, how would you rate that.")
initial_feeling = int(input("Entry:  "))
print()

# My initital plan with the code above was to ask the user how they were feeling
# again after receiving their results, then compare the two numbers and provide a
# personalized response, showing joy at their mood improving or remorse for
# worsening it by providing the information. But since this program is already over
# 550 lines, I'm abandoning that idea for now, unless I find additional time this
# weekend.

# provide a personalized response to user based on how they feel
if abstract_feeling == "good" and initial_feeling > 3 and initial_feeling < 7:
    print("I'm glad you're feeling good today.\n")
elif abstract_feeling == "good" and initial_feeling >= 7:
    print("Sounds like you're feeling great! That's awesome!\n")
elif abstract_feeling == "good" and initial_feeling <= 3:
    print("I'm glad you're feeling good today, but it sounds like it could be better.\n")
elif abstract_feeling == "bad" and initial_feeling > 3 and initial_feeling < 7:
    print("I'm sorry you're feeling bad today. I hope it gets better.\n")
elif abstract_feeling == "bad" and initial_feeling >= 7:
    print("Wow, it sounds like today is going really poorly for you. I'm so sorry.\n")
elif abstract_feeling == "bad" and initial_feeling <= 3:
    print("I'm sorry you're not feeling so good today, but at least it's not that bad.\n")

# asks user for their name
print("What should I call you?")
user_name = input("Entry:  ")
print()

# creates relationship by showing user program recognizes them as a named autonomous
# being
print("Hello " + user_name)
print("Today, we are going to calculate your budget against your monthly expenditures. \n")

# requests nation of residence
print("Before we start, I'd like to ask which country do you live in?")
home_nation = input("Entry:  ")
print()

# asks user for budget
print("Please tell me your monthly budget, formatted to two decimal places, ie: 999.99")
budget = float(input("Entry:  "))
print()

# Housing
# asks user if they have a rent, mortgage, or none
print("Alright! So, starting off, do you have a rent, mortgage, or neither? \nPlease format your response as 'Rent' or 'Mortgage' or 'Neither'")
housing = input("Entry:  ")
housing = housing.lower()  # converts to lowercase
print()

# if/elif/else: if user has a rent or mortgage payment, program asks what their cost
# is, elif if user has no monthly payment, asks the user for additional information
# so a personalized response can be given, then moves on to next question.
if housing == "rent" or housing == "mortgage":
    print("How much do you pay for your " + housing +
          " each month? \nPlease format your response with two decimal places, ie: 999.99")
    housing_cost = float(input("Entry:   "))
elif housing == "neither":
    print("Thank you for your response. Have you paid off your mortgage? Or do you live with \nsomeone who pays a mortgage or rent? \nPlease format your response as either 'Paid off' or 'Live with someone'")
    housing_status = input("Entry:  ")
    housing_status = housing_status.lower()  # converts to lowercase
    print()

    # personalized responses with error detection
    if housing_status == "paid off":
        print(
            f"Congratulations! That's wonderful! You are among an ever-shrinking group of \nhome-owning citizens in {str(home_nation)}.")
    elif housing_status == "live with someone":
        print("Thank you for your response. I understand that there is a non-zero chance I may be speaking to a bum.")
    else:
        print("I'm sorry, I did not understand the input you entered. Moving on...")
print()

# ISP
# asks user if they have internet service
print("Do you have internet service? \nPlease format your response as 'Yes' or 'No'")
has_isp = input("Entry:   ")
has_isp = has_isp.lower()  # converts to lowercase
print()

# if else: if user has internet service, program asks what their cost is, else if user
# does not have internet service, thanks the user for response and moves on to the next
# question
if has_isp == "yes":
    print("How much do you pay for your internet bill each month? \nPlease format your response with two decimal places, ie: 999.99")
    isp_cost = float(input("Entry:   "))
else:
    print("Thank you for your response. I understand that you do not participate in the modern world.")
print()

# Electricity
# asks user if they pay an electric bill
print("Do you pay an electric bill? \nPlease format your response as 'Yes' or 'No'")
has_electric = input("Entry:  ")
has_electric = has_electric.lower()  # converts to lowercase
print()

# if else: if user pays an electric bill, program asks what their cost is, else if user
# does not pay an electric bill, thanks the user for response and moves on to the next
# question
if has_electric == "yes":
    print("How much do you pay for electricity each month? \nPlease format your response with two decimal places, ie: 999.99")
    electric_cost = float(input("Entry:  "))
else:
    print("Thank you for your response. I understand that you are a Luddite.")
print()

# Water
# asks user if they pay a water bill
print("Do you pay an water bill? \nPlease format your response as 'Yes' or 'No'")
has_water = input("Entry:  ")
has_water = has_water.lower()  # converts to lowercase
print()

# if else: if user pays an water bill, program asks what their cost is, else if user
# does not pay an water bill, thanks the user for response and moves on to the next
# question
if has_water == "yes":
    print("How much do you pay for water each month? \nPlease format your response with two decimal places, ie: 999.99")
    water_cost = float(input("Entry:  "))
else:
    print("Thank you for your response. \n")
    print("Do you have a well on your property?  \nPlease format your response as 'Yes' or 'No'")
    has_well = input("Entry:  ")
    has_well = has_well.lower()  # converts to lowercase
    print()
    if has_well == "no":
        print("Thank you for your response. I do not understand how you are still alive.")
    else:
        print("Thank you for your response. I was worried for a moment that you do not have access to water, \nare dehydrated, and possibly smell bad.")
print()

# Gas
# asks user if they pay an gas bill
print("Do you pay an gas bill? \nPlease format your response as 'Yes' or 'No'")
has_gas = input("Entry:  ")
has_gas = has_gas.lower()  # converts to lowercase
print()

# if else: if user pays an gas bill, program asks what their cost is, else if user
# does not pay an gas bill, thanks the user for response and moves on to the next
# question
if has_gas == "yes":
    print("How much do you pay for gas each month? \nPlease format your response with two decimal places, ie: 999.99")
    gas_cost = float(input("Entry:  "))
else:
    print("Thank you for your response. I understand that you get cold in winter.")
print()

# Cell
# asks user if they pay an cell phone bill
print("Do you pay for a cell phone bill? \nPlease format your response as either 'Yes' or 'No'")
has_cell = input("Entry:  ")
has_cell = has_cell.lower()  # converts to lowercase
print()

# if else: if user pays an cell phone bill, program asks what their cost is, else if
# user does not pay an cell phone bill, thanks the user for response and moves on to
# the next question
if has_cell == "yes":
    print("How much do you pay for your cell phone each month? \nPlease format your response with two decimal places, ie: 999.99")
    cell_cost = float(input("Entry:  "))
else:
    print("Thank you for your response. I understand that you do not have friends.")
print()

# Food
# asks user how much they spend on food each month
print("How much do you pay for food each month? \nPlease format your response with two decimal places, ie: 999.99")
food_cost = float(input("Entry:  "))
print()

# Transportation
# asks user if they have a car, else if they use public transportation, else if they
# use a motorless form of transport, like a bike, scooter, or just walking
print("Do you use a vehicle to get around? \nPlease format your response as either 'Yes' or 'No'")
has_car = input("Entry:  ")
has_car = has_car.lower()  # converts to lowercase
print()

# if (if else(if else)) else(if else): if user uses a vehicle, asks if they have vehicle insurance. If they have insurance, asks how much it costs per month, otherwise thanks them for their response, and asks if they also use public transportation. If they do, asks how much it costs monthly. If they don't own a vehicle, asks if they use public transportation, and if they do, how much it costs monthly.
if has_car == "yes":
    print("How much do you spend in gas each month? \nPlease format your response with two decimal places, ie: 999.99")
    petrol_cost = float(input("Entry:  "))
    print()

    print("Do you have vehicle insurance? \nPlease format your response as either 'Yes' or 'No'")
    has_car_insurance = input("Entry:  ")
    has_car_insurance = has_car_insurance.lower()  # converts to lowercase
    print()

    if has_car_insurance == 'yes':
        print("How much do you spend on vehicle insurance each month? \nPlease format your response with two decimal places, ie: 999.99")
        car_insurance_cost = float(input("Entry:  "))
        print()
    else:
        print("Thank you for your response. I understand that you are irresponsible.\n")

    print("Do you also ever use public transportation to get around? \nPlease format your response as either 'Yes' or 'No'")
    public_transport = input("Entry:  ")
    public_transport = public_transport.lower()  # converts to lowercase
    print()

    if public_transport == "yes":
        print("How much do you spend on public transportation each month? \nPlease format your response with two decimal places, ie: 999.99")
        public_transport_cost = float(input("Entry:  "))
        print()
    else:
        print("Thank you for your response. I understand that you do not use public transportation.\n")

else:
    print("Thank you for your response. I understand that you do not use a vehicle.\n")
    print("Do you use public transportation to get around? \nPlease format your response as either 'Yes' or 'No'")
    public_transport = input("Entry:  ")
    public_transport = public_transport.lower()  # converts to lowercase
    print()

    if public_transport == "yes":
        print("How much do you spend on public transportation each month? \nPlease format your response with two decimal places, ie: 999.99")
        public_transport_cost = float(input("Entry:  "))
        print()
    else:
        print("Thank you for your response. I understand that you do not use public transportation.\n")

# Healthcare
# asks user if they have health insurance
print("Do you have a health insurance policy? \nPlease format your response as either 'Yes' or 'No'")
has_health_insurance = input("Entry:  ")
has_health_insurance = has_health_insurance.lower()  # converts to lowercase
print()

if has_health_insurance == "yes":
    print("How much do you spend on health insurance each month? \nPlease format your response with two decimal places, ie: 999.99")
    health_insurance_cost = float(input("Entry:  "))
    print()

    print("How much do you spend on healthcare out-of-pocket each month? \nIf the value changes each month, you may enter one of three options: \n\t1) Enter your average monthly cost, or... \n\t2) Enter the word 'Average' to be presented with an entry field for each month \n\t   and have the average cost calculated for you, or... \n\t3) Enter 'None' if you don't pay anything out-of-pocket for healthcare.")
    healthcare_self_cost = input("Entry:  ")
    healthcare_self_cost = healthcare_self_cost.lower()  # converts to lowercase
    print()

    if healthcare_self_cost == "average":
        print("Please enter the monthly cost for each month. \nPlease format your responses with two decimal places, ie: 999.99 \nIf you did not pay anything during a certain month, please enter '0.00'")
        hc_jan = float(input("January:  "))
        hc_feb = float(input("February:  "))
        hc_mar = float(input("March:  "))
        hc_apr = float(input("April:  "))
        hc_may = float(input("May:  "))
        hc_jun = float(input("June:  "))
        hc_jul = float(input("July:  "))
        hc_aug = float(input("August:  "))
        hc_sep = float(input("September:  "))
        hc_oct = float(input("October:  "))
        hc_nov = float(input("November:  "))
        hc_dec = float(input("December:  "))
        print()

        healthcare_self_cost_avg = float((hc_jan + hc_feb + hc_mar + hc_apr + hc_may +
                                          hc_jun + hc_jul + hc_aug + hc_sep + hc_oct + hc_nov + hc_dec) / 12)

        print(f"For your reference, your average monthly out-of-pocket cost for healthcare is ${
              healthcare_self_cost_avg:,.2f}.")
        print()

    elif healthcare_self_cost == "none":
        print("Thank you for your response. I understand you do not pay anything out-of-pocket for healthcare. You must have excellent health insurance. \n")

    # checks if the string contains a numerical value, and if so, converts to a float
    elif healthcare_self_cost.replace(".", "").isnumeric():
        healthcare_self_cost = float(healthcare_self_cost)

elif has_health_insurance == "no":
    print("Thank you for your response. I understand you do not value your health.\n")\

    print("How much do you spend on healthcare out-of-pocket each month? \nIf the value changes each month, you may enter one of three options: \n\t1) Enter your average monthly cost, or... \n\t2) Enter the word 'Average' to be presented with an entry field for each month \n\t   and have the average cost calculated for you, or... \n\t3) Enter 'None' if you don't pay anything out-of-pocket for healthcare.")
    healthcare_self_cost = input("Entry:  ")
    healthcare_self_cost = healthcare_self_cost.lower()  # converts to lowercase
    print()

    if healthcare_self_cost == "average":
        print("Please enter the monthly cost for each month. \nPlease format your responses with two decimal places, ie: 999.99 \nIf you did not pay anything during a certain month, please enter '0.00'")
        hc_jan = float(input("January:  "))
        hc_feb = float(input("February:  "))
        hc_mar = float(input("March:  "))
        hc_apr = float(input("April:  "))
        hc_may = float(input("May:  "))
        hc_jun = float(input("June:  "))
        hc_jul = float(input("July:  "))
        hc_aug = float(input("August:  "))
        hc_sep = float(input("September:  "))
        hc_oct = float(input("October:  "))
        hc_nov = float(input("November:  "))
        hc_dec = float(input("December:  "))
        print()

        healthcare_self_cost_avg = float((hc_jan + hc_feb + hc_mar + hc_apr + hc_may +
                                          hc_jun + hc_jul + hc_aug + hc_sep + hc_oct + hc_nov + hc_dec) / 12)

        print(f"For your reference, your average monthly out-of-pocket cost for healthcare is ${
              healthcare_self_cost_avg:,.2f}.")
        print()

    elif healthcare_self_cost == "none":
        print("Thank you for your response. I understand you do not pay anything out-of-pocket for healthcare. \nYou must be remarkably healthy. \n")

    elif healthcare_self_cost != "average" and healthcare_self_cost != "none":
        # checks if the string contains a numerical value, and if so,
        # converts to a float
        def is_float(healthcare_self_cost):
            if healthcare_self_cost.replace(".", "").isnumeric():
                healthcare_self_cost = float(healthcare_self_cost)

# Personal Care
# asks user if they have personal care expenditures
print("Do you have any monthly expenditures for personal care, ie: haircuts, hygiene, etc...? \nPlease format your response as 'Yes' or 'No'")
has_personal_care = input("Entry:  ")
has_personal_care = has_personal_care.lower()  # converts to lowercase
print()

# if else: if user has personal care expenditures, program asks what their cost is, else if user
# does not have personal care expenditures, thanks the user for response and moves on to the next
# question
if has_personal_care == "yes":
    print("How much do you pay for your personal care expenditures each month? \nPlease format your response with two decimal places, ie: 999.99")
    personal_care_cost = float(input("Entry:  "))
else:
    print("Thank you for your response. I understand that you smell bad.")
print()

# Clothing
# asks user how much the spend on clothing
print("Do you have monthly expenditures on clothing? \nPlease format your response as 'Yes' or 'No'")
has_clothing = input("Entry:  ")
has_clothing = has_clothing.lower()  # converts to lowercase
print()

# if else: if user has personal care expenditures, program asks what their cost is, else if user
# does not have personal care expenditures, thanks the user for response and moves on to the next
# question
if has_clothing == "yes":
    print("How much do you pay for your clothing each month? \nPlease format your response with two decimal places, ie: 999.99")
    clothing_cost = float(input("Entry:  "))
else:
    print("Thank you for your response. I understand that you are out of style.")
print()

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
          initial_debt:,.2f} in debt.\n")
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
# z/100 = x/y
# (z*y)/100=x
if has_debt == "yes":
    monthly_debt_paid = ((initial_debt * debt_percentage_paid) / 100)
    # tells the user the dollar amount of their debt they pay each month
    print(f"For your reference, you will pay ${
        monthly_debt_paid:,.2f} towards your total debt this month.\n")

# reminder of what the final output should be (so I don't have to keep scrolling)
#   Calculate the percentage of the total budget spent in each category.
#   Display the results in a user-friendly format, clearly showing the budget breakdown. (use f strings)
#   Ensure your code is well-commented to explain the functionality of different sections.

# ___VARIABLES TO CACULATE___
# housing_cost
# food_cost

# transportation_cost(
#    petrol_cost
#    car_insurance_cost
#    public_transport_cost)

# health_insurance_cost
"""
 -healthcare_cost
 -if user asked for their monthly out-of-pocket healthcare cost to be averaged out, use "healthcare_self_cost_avg"
 -if user entered "none" for healthcare_self_cost, then ignore
 -if healthcare_self_cost is numerical, use this
 -healthcare_self_cost OR healthcare_self_cost_avg
 """

# personal_care_cost
# clothing_cost
# monthly_debt_paid

# utilities_cost(
#    isp_cost
#    electric_cost
#    water_cost
#    gas_cost
#    cell_cost)
#

# utilities cost calculation
utilities_cost = (isp_cost + electric_cost + water_cost + gas_cost + cell_cost)

# transportation cost calculation
transportation_cost = (
    petrol_cost + car_insurance_cost + public_transport_cost)

# healthcare cost calculation
# the function "isinstance(x,y)" checks to see if "x" is data type "y"
# which in this case checks to see if healthcare_self_cost is a float
if has_health_insurance == "yes" and isinstance(healthcare_self_cost, float):
    healthcare_cost = (health_insurance_cost + healthcare_self_cost)
elif has_health_insurance == "yes" and healthcare_self_cost == "average":
    healthcare_cost = (health_insurance_cost + healthcare_self_cost_avg)
elif has_health_insurance == "yes" and healthcare_self_cost == "none":
    healthcare_cost = health_insurance_cost
elif has_health_insurance == "no" and isinstance(healthcare_self_cost, float):
    healthcare_cost = healthcare_self_cost
elif has_health_insurance == "no" and healthcare_self_cost == "average":
    healthcare_cost = healthcare_self_cost_avg
elif has_health_insurance == "no" and healthcare_self_cost == "none":
    healthcare_cost = float(0)

# calculate total monthly expenses
total_expenses = (housing_cost + food_cost + transportation_cost + healthcare_cost +
                  personal_care_cost + clothing_cost + monthly_debt_paid + utilities_cost)

# calculate percentage of total expenses for each category
"""
    base expression
    x/y = %/100
    x = category cost
    y = total expenditures
    % = target percentage value
    (100 * x) / y = %
    """

# housing percentage
housing_percentage = (100 * housing_cost) / total_expenses

# food percentage
food_percentage = (100 * food_cost) / total_expenses

# transportation percentage
transportation_percentage = (100 * transportation_cost) / total_expenses

# healthcare percentage
healthcare_percentage = (100 * healthcare_cost) / total_expenses

# personal care percentage
personal_care_percentage = (100 * personal_care_cost) / total_expenses

# clothing percentage
clothing_percentage = (100 * clothing_cost) / total_expenses

# monthly debt percentage
monthly_debt_percentage = (100 * monthly_debt_paid) / total_expenses

# utilities percentage
utilities_percentage = (100 * utilities_cost) / total_expenses

# Display percentage values for each category to the user

print("I will now calculate the percentage of your monthly expenses for each category. \nI understand this is not as relevant as percentage of your budget, \nbut we'll get to that in a moment. \n\nPlease press enter when you are ready.")
input("Press Enter...")

print()
print(f"Your HOUSING costs account for {
      housing_percentage:.2f}% of your monthly expenses.")
print(f"Your FOOD costs account for {
      food_percentage:.2f}% of your monthly expenses.")
print(f"Your TRANSPORTATION costs account for {
      transportation_percentage:.2f}% of your monthly expenses.")
print(f"Your HEALTHCARE costs account for {
      healthcare_percentage:.2f}% of your monthly expenses.")
print(f"Your PERSONAL CARE costs account for {
      personal_care_percentage:.2f}% of your monthly expenses.")
print(f"Your CLOTHING costs account for {
      clothing_percentage:.2f}% of your monthly expenses.")
print(f"Your monthly DEBT payment accounts for {
      monthly_debt_percentage:.2f}% of your monthly expenses this month.")
print(f"Your UTILITIES costs account for {
      utilities_percentage:.2f}% of your monthly expenses.\n")

# calculate percent of their total budget each category eats up

# housing percentage
housing_budget_percentage = (100 * housing_cost) / budget

# food percentage
food_budget_percentage = (100 * food_cost) / budget

# transportation percentage
transportation_budget_percentage = (100 * transportation_cost) / budget

# healthcare percentage
healthcare_budget_percentage = (100 * healthcare_cost) / budget

# personal care percentage
personal_care_budget_percentage = (100 * personal_care_cost) / budget

# clothing percentage
clothing_budget_percentage = (100 * clothing_cost) / budget

# monthly debt percentage
monthly_debt_budget_percentage = (100 * monthly_debt_paid) / budget

# utilities percentage
utilities_budget_percentage = (100 * utilities_cost) / budget

print("I will now calculate the percentage of your budget for each category. \nPlease tell me when you are ready.")
input("Press Enter...")

print()
print(f"Your HOUSING costs account for {
      housing_budget_percentage:.2f}% of your budget.")
print(f"Your FOOD costs account for {
      food_budget_percentage:.2f}% of your budget.")
print(f"Your TRANSPORTATION costs account for {
      transportation_budget_percentage:.2f}% of your budget.")
print(f"Your HEALTHCARE costs account for {
      healthcare_budget_percentage:.2f}% of your budget.")
print(f"Your PERSONAL CARE costs account for {
      personal_care_budget_percentage:.2f}% of your budget.")
print(f"Your CLOTHING costs account for {
      clothing_budget_percentage:.2f}% of your budget.")
print(f"Your monthly DEBT payment accounts for {
      monthly_debt_budget_percentage:.2f}% of your budget this month.")
print(f"Your UTILITIES costs account for {
      utilities_budget_percentage:.2f}% of your budget.\n")

# displays the user's budget versus their monthly expenses, indicating whether
# they are over budget or under budget for the month
print(f"Your total monthly expenses are {
      str(total_expenses)} against a monthly budget of {str(budget)}\n")
if total_expenses > budget:
    print("I'm sorry, it looks like you are going over budget this month. \nI guess you'll be adding to your debt this month?\n")
elif budget > total_expenses:
    print("Congratulations! You're under budget this month!\n")
elif budget == total_expenses:
    print("Looks like you have exactly enough to cover your expenses this month.\n")

# thanks the user for their time
print(f"Thank you, {str(user_name)}, for using this excessively written program for what was \n\tmeant to be a simple assignment. \nYour time is appreciated. I hope you enjoyed your experience and \n\tthat the results were to your liking.\n")

# end program prompt
input("Press enter to exit the program.")
print()
