afl_teams = ["Collingwood Magpies", "Geelong Cats", "Richmond Tigers", "West Coast Eagles", "Essendon Bombers", "Carlton Blues", "Adelaide Crows", "Sydney Swans"]

#create a temporary variable (team) that is associated with the afl_teams list
#python will loop through the list until all list entries have been covered
#keep in mind that the set of steps is repeated once for each item in the list,

#The colon at the end of a for statement tells Python to interpret the next line as the start of a loop.

for team in afl_teams:
    print(team)


magicians = ["David Copperfield", "Harry Houdini", "Criss Angel", "Penn and Teller", "Derren Brown"]

for magician in magicians:
    print(magician.title() + ", that was a great trick!")
    print("I can't wait to see your next trick, " + magician.title() + ".\n")

#Any lines of code after the for loop that are not indented are executed once without repetition.

singers = ["Adele", "Beyoncé", "Taylor Swift", "Lady Gaga", "Britney Spears"]

for singer in singers:
    #thi is inside the loop so will print for each list item
    print('That was an amazing performance ' + singer +'\n')

#this is outside the loop so will print only once
print('Thanks to you all for being such awesome performers!')