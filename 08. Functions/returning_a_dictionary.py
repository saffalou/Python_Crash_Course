# A function can return any kind of value you need it to, 
# including more complicated data structures like lists and dictionaries.




# The function build_person() takes in a first and last name, 
# and puts these values into a dictionary. 
# The value of first_name is stored with the key 'first', 
# and the value of last_name is stored with the key 'last'. 
# Then, the entire dictionary representing the person is returned. 
# The return value is printed with the original two pieces of textual 
# information now stored in a dictionary:


def build_person(first_name, last_name):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    return person

musician = build_person('jimi', 'hendrix')
print(musician)



# You can easily extend this function to accept optional values like a 
# middle name, an age, an occupation, or any other information 
# you want to store about a person. For example, 
# the following change allows you to store a person’s age as well:

def build_person(first_name, last_name, age=None):
    """Return a dictionary of information about a person."""
    person = {'first': first_name, 'last': last_name}
    if age:
        person['age'] = age
    return person

musician = build_person('jimi', 'hendrix', age=27)
print(musician)

# We add a new optional parameter age to the function definition and assign 
# the parameter the special value None, which is used when a variable has 
# no specific value assigned to it. 
# You can think of None as a placeholder value. 
# In conditional tests, None evaluates to False. 
# If the function call includes a value for age, 
# that value is stored in the dictionary.

