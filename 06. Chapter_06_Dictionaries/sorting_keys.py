# Looping through a dictionary returns the items in the same order they were inserted. 
# Sometimes, though, you’ll want to loop through a dictionary in a different order. 
# One way to do this is to sort the keys as they’re returned in the for loop. 
# You can use the sorted() function to get a copy of the keys in order:

people = {
    'Xena': 'Perth', 
    'Caroline': 'Perth',
    'Dave': 'Brisbane',
    'Eve': 'Perth',
    'Frank': 'Melbourne',
    'Grace': 'Sydney',
     'Alice': 'Melbourne',
    'Bob': 'Sydney',
}

#The sorted() function returns a list of keys in alphabetical order,
for name in sorted(people.keys()):
    print(f"{name} lives in {people[name]}")

# This for statement is like other for statements, 
# except that we’ve wrapped the sorted() function around the dictionary.keys() method.


# we can loop through the dictionary and pull only the values from the dictionary
print('We have people living in locations around Australia. Here is a list of the locations:')
for name in people.values():
    print(name.title())

# the above pulls all values and doesn't look for duplicates.
# we can use the set() function to get a unique set of values
#sets are in curly braces so look like a dictionary but sets aren't in key-value pairs
set = []
for name in set(people.values()):
    print(f'\n' + name.title())
  

