mystery_string = "ABCDE"

#If the goal is to convert the string above into the string
#"ABCDE.ABCDE.ABCDE.???", we need to note in what order the
#operations should be performed.

#The period is repeated along with the original string, so
#we want to start off by adding a period to the original
#string:

mystery_string += "."

#mystery_string is now "ABCDE." That should be repeated three
#times:

mystery_string *= 3

#Finally, we want to add three exclamation points. However,
#we can't create a new string longer than one character. So,
#we create a one-character string and multiply it by three,
#and add it to mystery_string:

mystery_string += "?" * 3
print(mystery_string)

#We could also do this all in one line if we wanted to: --

