# 6-7. People: Start with the program you wrote for Exercise 6-1 (page 98). 
# Make two new dictionaries representing different people, and store all three dictionaries in a list called people. 
# Loop through your list of people. As you loop through the list, print everything you know about each person.

person = { 'jdoe':{
    'first_name': 'John',
    'last_name': 'Doe',
    'age': 30,
    'city': 'New York',
    },

    'lwatts':{
    'first_name': 'Lisa',
    'last_name': 'Watts',
    'age': 35,
    'city': 'San Francisco',
    },
    'mdodds':{
    'first_name': 'Michelle',
    'last_name': 'Dodds',
    'age': 40,
    'city': 'New York',}

}

#for key, value in person.items():
 #   print(f"\t First name: {key}")
  #  print(f"\t Value: {value}")

for key, value in person.items():
    fullname = f"\t Full name: {value['first_name']} {value['last_name']}"
    age = f"\t Age: {value['age']}"
    city = f"\t City: {value['city']}"

    #can print it this way and have each element on a new line
    print(f"{fullname}")
    print(f"{age}")
    print(f"{city}")

    #or can do it this way and have each element on a new line
    print(f"\n{fullname}\n{age}\n{city}\n")


# 6-8. Pets: Make several dictionaries, where each dictionary represents a different pet. 
# In each dictionary, include the kind of animal and the owner’s name. 
# Store these dictionaries in a list called pets. Next, loop through your list and as you do, print everything you know about each pet.


pets = {

    'fluffy':{
        'animal': 'cat',
        'owner': 'tammy townhouse',
},

    'fido':{
        'animal': 'dog',
        'owner': 'jimmy jawbone',
},

    'nemo':{
        'animal': 'fish',
        'owner': 'disney pixar',
},

}

for key, value in pets.items():
    print(f"\nPet's name: {key.title()}")
    print(f"Animal: {value['animal'].title()}")
    print(f"Owner: {value['owner'].title()}")


# or which will produce the same output as the above

for key, value in pets.items():
    print(f"\nPet name: {key.title()}\nAnimal type: {value['animal'].title()}\nOwners name: {value['owner'].title()}")


# 6-9. Favorite Places: Make a dictionary called favorite_places. 
# Think of three names to use as keys in the dictionary, and store one to three favorite places for each person. 
# To make this exercise a bit more interesting, ask some friends to name a few of their favorite places. 
# Loop through the dictionary, and print each person’s name and their favorite places.

favorite_place =  {
    'joe': ['new york', 'california', 'los angeles'],
    
    'sarah': ['beijing', 'shanghai', 'hong kong'],

    'james': ['melbourne', 'sydney', 'brisbane'],

    }

for key, value in favorite_place.items():
    print(f"\n{key.title()}'s favorite places are:")
    for place in value:
        print(f"\t{place.title()}")

# 6-10. Favorite Numbers: Modify your program from Exercise 6-2 (page 98) so each person can have more than one favorite number. 
# Then print each person’s name along with their favorite numbers.
numbers = {
    'Jenny': [1, 5],
    'John': [2, 9],
    'Joe': [3, 7],
    'Jack': [4, 6],
    'Jill': [5, 8],
    }

for key, value in numbers.items():
    print(f"\n{key.title()}'s favorite numbers are:")
    for number in value:
        print(f"\t{number}")


# 6-11. Cities: Make a dictionary called cities. 
# Use the names of three cities as keys in your dictionary. 
# Create a dictionary of information about each city and include the country that the city is in, its approximate population, and one fact about that city. 
# The keys for each city’s dictionary should be something like country, population, and fact. 
# Print the name of each city and all of the information you have stored about it.

cities = {

    'new york':{
        'country': 'america',
        'population': 80000000,
        'fact': 'the big apple',

    },

    'los angeles':{
        'country': 'america',
        'population': 70000000, 
        'fact': 'the city of angels',
    },

    'tokyo':{
        'country': 'japan',
        'population': 100000000,
        'fact': 'the land of the rising sun',
    }
}

for key, value in cities.items():
    print(f"\nCity: {key.title()}")
    for k, v in value.items():
# this will print out the fact as a title if the key is fact
# otherwise it will just print the value (no title as it is integer)
        print(f"{k.title()}: {v.title() if k == 'fact' else v}")
