# Consider a game featuring aliens that can have different colors and point values. This simple dictionary stores information about a particular alien:

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print(alien_0)

# A dictionary in Python is a collection of key-value pairs. 
# Each key is connected to a value, and you can use a key to access the value associated with that key. 
# A key’s value can be a number, a string, a list, or even another dictionary. 
# In fact, you can use any object that you can create in Python as a value in a dictionary. 
# In Python, a dictionary is wrapped in braces ({}) with a series of key-value pairs inside the braces
# A key-value pair is a set of values associated with each other. 
# When you provide a key, Python returns the value associated with that key. 
# Every key is connected to its value by a colon, and individual key-value pairs are separated by commas. 
# You can store as many key-value pairs as you want in a dictionary.

# now we add new items to the dictionary
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)


#starting weith an empty dictionary
alien_0 = {}

alien_0['color'] = 'blue'
alien_0['points'] = 15

print(alien_0)

# To modify a value in a dictionary, give the name of the dictionary 
# with the key in square brackets and then the new value you want associated with that key.

alien_0['color'] = 'bright red'
print(alien_0)

alien_0['points'] = 35
print(alien_0)

print(f'The alien is {alien_0['color']}')

alien_0['color'] = 'azure'
print(f'The alien has changed and is now {alien_0['color']}')


alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print(f"Original position: {alien_0['x_position']}")

# Move the alien to the right.
# Determine how far to move the alien based on its current speed. 

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

#now we can see the increment applied to the x_position in the dictionary
print(f"New position: {alien_0['x_position']}")   # new position = 2


# change the dictionary to update speed
alien_0['speed'] = 'fast'

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien.
    x_increment = 3

# The new position is the old position plus the increment.
alien_0['x_position'] = alien_0['x_position'] + x_increment

#now we can see the increment applied to the x_position in the dictionary
print(f"New position: {alien_0['x_position']}")  # new position = 5 (2 + 3)

# and we can see the x_position value in the dictionary. Has gone from 0 to 2 to 5
print(alien_0)


# Removing key-value pairs
#use the del statement to remove a key-value pair from a dictionary
# if we want to delete points

alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

print(alien_0)

del alien_0['points']

print(alien_0['color'])
# the following print line will give an error because we are trying to call a key that does not exist in the dictionary
#print(alien_0['points'])

#the dictionary is now a single key pair
print(alien_0)