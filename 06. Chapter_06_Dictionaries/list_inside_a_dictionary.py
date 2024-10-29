# Rather than putting a dictionary inside a list, it’s sometimes useful to put a list inside a dictionary. 
# For example, consider how you might describe a pizza that someone is ordering. 
# If you were to use only a list, all you could really store is a list of the pizza's toppings. 
# With a dictionary, you can store the pizza's name, the toppings, and other information about the pizza.

# Store information about a pizza being ordered.
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
    }

# Summarize the order.
print(f"You ordered a {pizza['crust']}-crust pizza "
    "with the following toppings:")

for topping in pizza['toppings']:
    print(f"\t{topping}")

# You can nest a list inside a dictionary anytime you want more than one value to be associated with a single key in a dictionary.

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
# this refines our output. Grammer is now correct based on number of languages
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite languages are:")
    else: 
        print(f"\n{name.title()}'s favorite language is:")
    for language in languages:
        print(f"\t{language.title()}")



