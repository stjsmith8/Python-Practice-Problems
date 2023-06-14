meal_cost = 10.00
tax_rate = 0.08
tip_rate = 0.20

#The best way to do this is to first calculate the values we
#need, and second worry about what we need to do with them.
#
#So, let's start by finding the total tax to charge and the
#total tip to leave:

tax = meal_cost * tax_rate
tip = meal_cost * tip_rate

#Next, let's find the total meal cost:

total = meal_cost + tax + tip

#Now let's print:
print("Subtotal:", meal_cost)
print("Tax:", tax)
print("Tip:", tip)
print("Total:", total)

#You might be tempted to calculate tax and tip in-line like
#this:

print("Subtotal:", meal_cost)
print("Tax:", meal_cost * tax_rate)
print("Tip:", meal_cost * tip_rate)
print("Total:", meal_cost + meal_cost * tax_rate + meal_cost * tip_rate)

#However, imagine if you made a mistake in the calculation
#for tax or tip. Using this second method, you would have
#to fix that in two places. In programming, we want to avoid
#every having multiple segments of code that do the same
#thing. If we end up needing that, we should have one
#segment of code that performs the desired operation, and we
#should use the results of that one segment in both places
#where it was needed.

