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


# 6-5. Rivers: Make a dictionary containing three major rivers and the country each river runs through. 
# One key-value pair might be 'nile': 'egypt'. 
# Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
# Use a loop to print the name of each river included in the dictionary. 
# Use a loop to print the name of each country included in the dictionary.

rivers = {
    'Nile': 'Egypt',
    'Amazon': 'Brazil, Peru, Colombia',
    'Yangtze': 'China',
}

for river, country in rivers.items():
    print(f"The {river} runs through {country}.")


for river in rivers.keys():
    print(river)


for country in rivers.values():
    print(country)

# Polling: Use the code in favorite_languages.py (page 96). 
# Make a list of people who should take the favorite languages poll. 
# Include some names that are already in the dictionary and some that are not. 
# Loop through the list of people who should take the poll. 
# If they have already taken the poll, print a message thanking them for responding. 
# If they have not yet taken the poll, print a message inviting them to take the poll.

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'david': 'c++',
    'james': 'c++',
    'leon': 'python',
    'sophie': 'rust',
    }

poll_completed = ['sarah', 'phil', 'sophie']
# loop through the list of people who should take the poll
for people in favorite_languages.keys():
    print(f"Dear {people.title()}, we have sent you a poll we would like you to complete..")
print('\n')

# now let's allow for poll completion and non-completion
for people in favorite_languages.keys():
    if people in poll_completed:
        print(f"Thank you for completing our poll {people.title()}!")
    else:
        print(f"Dear {people.title()} we recently sent you a poll for completion. We would really appreciate if you could complete it.")




