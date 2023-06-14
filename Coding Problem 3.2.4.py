temperature = -3.7
celsius = True

#There are a lot of ways to do this! To make this easier,
#we'll include them all in this file. If you run this file,
#you'll see the answer printed multiple times.

#First, perhaps most obviously, we can just check each case
#separately:

if celsius and temperature <= 0:
    print("Freezing")
elif not celsius and temperature <= 32:
    print("Freezing")
else:
    print("Not freezing")

#This reasoning checks if it's below 0 in Celsius, then checks
#if it's below 32 and Fahrenheit. If neither is true, it's not
#freezing.
#
#That elif can be rephrased as an or, though, so that we don't
#have to have two lines printing "Freezing":

if (celsius and temperature <= 0) or (not celsius and temperature <= 32):
    print("Freezing")
else:
    print("Not freezing")

#Notice that the two logical expressions are the same, but that
#they're in parentheses. This forces Python to evaluate this in
#the right order, and helps us read it correctly.
#
#Note, though, that there's a very different approach we could
#take as well. Instead of checking Fahrenheit and Celsius
#together, we could convert one to the other:

if not celsius:
    temperature = (temperature - 32) / 1.8
if temperature <= 0:
    print("Freezing")
else:
    print("Not freezing")

#This approach requires more lines, but the lines themselves are
#simpler.
