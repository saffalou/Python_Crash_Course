#6-1. Person: Use a dictionary to store information about a person you know. 
# Store their first name, last name, age, and the city in which they live. 
# You should have keys such as first_name, last_name, age, and city. 
# Print each piece of information stored in your dictionary.

person = {
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York',}

print(person)
print(person['first_name'])
print(person['last_name'])  
print(person['age'])
print(person['city'])



#this approach allows us to iterate through the dictionary and print out both key and value
for key, value in person.items():
    print(f"{key} :{value}")


#Favorite Numbers: Use a dictionary to store people’s favorite numbers. 
# Think of five names, and use them as keys in your dictionary. 
# Think of a favorite number for each person, and store each as a value in your dictionary. 
# Print each person’s name and their favorite number.

numbers = {
    'Jenny': 1, 
    'John': 2, 
    'Joe': 3, 
    'Jack': 4, 
    'Jill': 5,}

print(numbers['Jenny'])
print(numbers['John'])
print(numbers['Joe'])
print(numbers['Jack'])
print(numbers['Jill'])

#this approach allows us to iterate through the dictionary and print out both key and value
for key, value in numbers.items():
    print(f"{key} : {value}")


# 3. Glossary: A Python dictionary can be used to model an actual dictionary. 
# However, to avoid confusion, let’s call it a glossary. 
# Think of five programming words you’ve learned about in the previous chapters. 
# Use these words as the keys in your glossary, and store their meanings as values. 
# Print each word and its meaning as neatly formatted output. 
# You might print the word followed by a colon and then its meaning, 
# or print the word on one line and then print its meaning indented on a second line. 
# Use the newline character (\n) to insert a blank line between each word-meaning pair in your output.

words_meanings = {
    'variable': 
    'a named container for data',
    'function': 
    'a piece of code that performs a specific task',
    'if statement': 
    'a control structure that allows you to execute a block of code based on a condition',
    'list': 
    'a collection of items in a particular order',
    'dictionary': 
    'a collection of key-value pairs',
    }


for word, meaning in words_meanings.items():
    print(f"{word} : {meaning} \n")