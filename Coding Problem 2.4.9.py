principal = 5000
rate = 0.05
time = 5

#This one's short enough that we wouldn't be unreasonable
#to try to do it in one line. Be careful with the
#parentheses, though:

import math
amount = principal * math.e ** (rate * time)

#Written like this, Python first evaluates rate * time, then
#raises math.e to the result, then multiplies principal by
#the result. If we left off the parentheses, then by default
#Python evaluates the exponent ** first. So, it would
#multiply principal and time by e^rate, which isn't correct.

print("After " + str(time) + " years invested with a " + str(rate) + " interest rate, a $" + str(principal) + " investment will be worth $" + str(round(amount, 2)) + ".")

#Notice that we're using a function in this print statement
#that we haven't talked about: round(). round() takes two
#parameters: a float and an integer. It rounds the float
#to the number of decimal places given by the integer.
#Using this, we're able to round an ugly value like
#6420.127083438707 to a cleaner value like 6420.13.
