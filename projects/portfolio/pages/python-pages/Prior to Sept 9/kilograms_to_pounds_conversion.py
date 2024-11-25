# Create a Python program that converts kilograms to pounds
# Use at least four different samples to convert

# 1 pound = 2.20462 kilograms
# conversion factor = 2.20462

# Define variables for pound (lb) sample entries
lb_01 = 10
lb_02 = 25
lb_03 = 52.75
lb_04 = 220

# How I remember conversions, using the pound (lb) and
# kilogram (kg) examples
# ((x_lbs) / 1lb ) = ((y_kg) / 2.20462kg)
# if converting 10lbs, then the equation would look like:
# (10/1) = (x/2.20462)
# (10 * 2.20462) = (x / 1)
# (22.0462 / 1) = x
# x = 22.0462

# Conversion factor
conversion_factor = 2.20462

# Calculate kilograms (kg) for each pound value
kg_01 = lb_01 * conversion_factor
kg_02 = lb_02 * conversion_factor
kg_03 = lb_03 * conversion_factor
kg_04 = lb_04 * conversion_factor

# Output the results
print(f"\n{lb_01} pounds is equal to {kg_01:.2f} kilograms.\n")
print(f"{lb_02} pounds is equal to {kg_02:.2f} kilograms.\n")
print(f"{lb_03} pounds is equal to {kg_03:.2f} kilograms.\n")
print(f"{lb_04} pounds is equal to {kg_04:.2f} kilograms.\n")
print("All results are rounded to two decimal points.\n")
