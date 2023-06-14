start_hour = 3
start_minute = 48
length = 172

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Let's try something trickier! The variables above represent
#the start time for a run as well as the length of the run
#in minutes. The original values, for example, show a run
#that started at 3:48 and lasted 172 minutes.
#
#Add some code below that will print the time at which the
#run will end, using normal formatting (e.g. 6:40 for the
#original data above). To do this, you'll need to somehow
#find both the hours and minutes of the new time, convert
#both to strings, and add those to the colon ":" to print
#the time.
#
#You may assume that the length of the run will never cross
#12:59 (e.g. you don't have to worry about going from
#12:59 to 1:00 or 23:59 to 0:00). You also don't need to
#worry about the lack of 0 in front of single-digit minute
#counts (e.g. it's fine to show 5:07 as 5:7).


#Add your code here!

start_hour_in_min = start_hour * 60
#print(start_hour_in_min)
add_start_hour_and_min = start_hour_in_min + start_minute
#print(add_start_hour_and_min)
add_length = add_start_hour_and_min + length
#print(add_length)

end_hour = add_length // 60
#print(end_hour)
end_min = add_length - (end_hour*60)
#print(end_min)

print(str(end_hour)+':'+str(end_min))

################################################


end_hour = start_hour + (length // 60)

#Then, we can add the remainder to the initial number of
#minutes:

end_minute = start_minute + (length % 60)

#Now we're done, right? Not quite. It's possible that enough
#minutes were just added to start_minute to tick over to
#another hour again: for example, a 172 minute run starting
#at 3:48 will end with a minute value of 100. 5:100 isn't
#a real time, though -- it should be 6:40!
#
#So what do we do? Let's add end_minute // 60 to end_hour
#again. This will give the number of complete hours held by
#end_minute:

end_hour += end_minute // 60

#If end_minute is less than 60, then end_minute // 60 will
#return 0, and end_hour will be unchanged.
#
#Finally, let's see end_minute equal to its own remainder
#when divided by 60:

end_minute = end_minute % 60

#If end_minute was less than 60, this will return the value
#of end_minute and leave the time unchanged.
#
#Finally, we print:

print(str(end_hour) + ":" + str(end_minute))
####################################################


total_minutes = length

#Then, we add to it the number of minutes since midnight.
#That's 60 times the number of hours plus the number of
#minutes:

total_minutes += (start_hour * 60) + start_minute

#Now, we perform floor division to find the total number of
#hours in total_minutes:

end_hour = total_minutes // 60

#And modulus to find the total number of leftover minutes
#after accounting for the hours:

end_minute = total_minutes % 60

#Finally, we print:

print(str(end_hour) + ":" + str(end_minute))

