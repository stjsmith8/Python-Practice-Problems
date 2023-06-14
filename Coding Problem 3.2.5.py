team_1 = "Georgia Tech"
team_1_score = 28
team_2 = "Georgia"
team_2_score = 27

team_1 = "Georgia Tech"
team_1_score = 28
team_2 = "Georgia"
team_2_score = 28

#You may modify the lines of code above, but don't move them!
#When you Submit your code, we'll change these lines to
#assign different values to the variables.

#Above we've created four variables: two team names and two
#scores. A team wins if their score is greater than the other
#team's score.
#
#Add to the code below. To print a messages like these
#depending on the values:
#
# - If one team beat the other, print:
#     "[winner] beat [loser] by [margin]"
# - If neither team won, print:
#     "[team_1] played [team_2] and it was a tie"
#
#For example, with the original values in this code, you
#should print "Georgia Tech beat Georgia by 1"
#
#Hint: to make this easier, create three variables: winner,
#loser, and margin. Then, find their values before worrying
#about printing the final message.


#Add your code here!


if team_1_score > team_2_score:
    winner = team_1
    loser = team_2
    margin = team_1_score - team_2_score
    print(winner, "beat", loser, "by", margin)
elif team_2_score > team_1_score:
    winner = team_2
    loser = team_1
    margin = team_2_score - team_1_score
    print(winner, "beat", loser, "by", margin)
else:
    print(team_1, "played", team_2, "and it was a tie")
 
    
###############################################################

#What we actually print is based on the which team's score
#is greater and what the margin of victory is. So, the first
#thing we might want to do is identify who is the winner and
#who is the loser:

if team_1_score > team_2_score:
    winner = team_1
    loser = team_2
    margin = team_2_score - team_1_score
else:
    winner = team_2
    loser = team_1
    margin = team_2_score - team_1_score

#Here, we're labeling a team as the 'winner' even if the game
#was tied: we'll take care of that in the next conditional.
#Now, we want to print one message if the score was tied, and
#a different one if it wasn't:

if margin == 0:
    print(team_1, "played", team_2, "and it was a tie")
else:
    print(winner, "beat", loser, "by", margin)

#Notice we're using Python's comma syntax for print statements
#here. That's why we don't have to convert margin to an
#integer. We could also rewrite that last print statement like
#this:
#
#print(winner + " beat " + loser + " by " + str(margin))
#
#Or like this:
#
#print("{0} beat {1} by {2}".format(winner, loser, str(margin)))
