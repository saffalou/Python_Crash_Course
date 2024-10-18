#list slicing
#To make a slice, you specify the index of the first and last elements you want to work with. 
# As with the range() function, Python stops one item before the second index you specify. 
# To output the first three elements in a list, you would request indices 0 through 3, 
# which would return elements 0, 1, and 2.

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])

#If you omit the first index, Python starts at the beginning of the list. 
# If you omit the second index, Python goes through the list to the end. 
# This is similar to the range() function, except that it doesn’t include the end value.
print(players[:3])   #same as print(players[0:3])
print(players[:])    #same as print(players[0:5])
print(players[2:])   #same as print(players[2:5])

#This prints the names of the last three players 
# and will continue to work as the list of players changes in size.
# or you can use a negative number
print(players[-3:])  

# you cal add a third parameter to specify the step size
# the step size is how many items you want to skip between each output
print(players[0:5:2])   


# looping through lists with for loop

for player in players[1:5]:
    print(player.title())
    
for player in players[:5]:
    print(f'{player.title()} is players in the tournament')

print('Welcome to all players')
print('\n')

for player in players[0:4]:
    print(f'{player.title()} is playing on day 1 of the tournament')

print('Good luck to all players on day 1 of the tournament')

