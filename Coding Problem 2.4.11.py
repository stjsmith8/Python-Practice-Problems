dosage = 100
time_since_last_dose = 7
is_nighttime = True
took_something_cross_reactive = True

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.
#
#Let's try to use our mathematical operators and logical
#operators together.
#
#Imagine you've been battling a cold. You're deciding whether
#to take cough syrup or not, and if so, how much to take.
#
#time_since_last_dose represents the number of hours since
#you last took some cough syrup. For every hour it's been,
#you're allowed to have one dose.
#
#If it's nighttime (is_nighttime), then you may double
#your dose since you won't be taking any until morning.
#
#However, if you've taken something cross-reactive
#(took_something_cross_reactive), then you should not take
#any cough syrup.
#
#Write a program that will print how large a dose of cough
#syrup to take.
#
#HINT: Remember, if you try to multiply a number times a
#boolean, Python treats False as 0 and True as 1. There are
#other ways to do this, though.


#Add your code here!


dose_day = (time_since_last_dose * dosage) * (not is_nighttime) * (not took_something_cross_reactive)

dose_night = (time_since_last_dose * dosage * 2) * (is_nighttime) * (not took_something_cross_reactive)

print(dose_day + dose_night)
#######################################################

#There are a lot of different ways to do this problem.
#However, we're going to focus on the one that can be done
#using only the principles we've used so far.
#
#To start with, let's calculate what the normal dose would
#be:

total_dose = dosage * time_since_last_dose

#Now the tricky part: we want to double it if is_nighttime
#is True. Later we'll learn about if statements, which can
#be used to resolve this, but there's a way around that
#now. If we try to multiply by a boolean, Python treats
#False as 0 and True as 1. We want to multiply by 1 if
#is_nighttime is False, and 2 if it's True. So, we just
#add one to it, then multiply by it!

total_dose *= is_nighttime + 1

#Now we want to set the dosage to 0 if
#took_something_cross_reactive is True. Our easiest way
#to do this is to apply the not operator, then multiply:
#if took_something_cross_reactive was True, then not
#will make it False, which means it will be 0 when
#multiplying:

total_dose *= not took_something_cross_reactive

#There are lots of other ways this could be done,
#though.

print(total_dose)

