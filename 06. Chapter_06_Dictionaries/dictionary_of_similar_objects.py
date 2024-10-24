# You can also use a dictionary to store one kind of information about many objects. 
# For example, say you want to poll a number of people and ask them what their favorite programming language is. 
# A dictionary is useful for storing the results of a simple poll, like this:

#create the dictionary
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }
# create variable to store specific information
language = favorite_languages['sarah'].title()

print(f"Sarah's favorite language is {language}.")


# The keys are people's names, and the values are their favorite languages.


#using get to avoid an error

alien_0 = {'color': 'green', 'points': 5}



del alien_0['points']

print(alien_0['color'])
# the following print line will give an error because we are trying to call a key that does not exist in the dictionary
#print(alien_0['points'])


# but we can do this to avoid the error
# The get() method requires a key as a first argument. As a second optional argument, you can pass the value to be returned if the key doesn’t exist:

alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']                                            # points key has been deleted from dictionary
point_value=alien_0.get('points', 'No point value assigned.')
print(point_value)


# if the points key exists, the points will be passed back
alien_0 = {'color': 'green', 'points': 5}
#del alien_0['points']                                        # points key hasn't been deleted from dictionary
point_value=alien_0.get('points', 'No point value assigned.')
print(point_value)

# If you leave out the second argument in the call to get() and the key doesn’t exist, 
# Python will return the value None. 
# The special value None means “no value exists.” 
# This is not an error: it’s a special value meant to indicate the absence of a value.

alien_0 = {'color': 'green', 'points': 5}
del alien_0['points']                                            # points key has been deleted from dictionary
point_value=alien_0.get('points')                  #key defined but no second argument so Python returns "None"
print(point_value)

