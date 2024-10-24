# You can loop through all of a dictionary’s key-value pairs, through its keys, or through its values.

# Looping Through All Key-Value Pairs
# You can loop through all of a dictionary’s key-value pairs, by using a for loop with two variables. 
# The first variable is the key, and the second variable is the value.

user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
    }

for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

# To write a for loop for a dictionary, you create names for the two variables 
# that will hold the key and value in each key-value pair. 
# You can choose any names you want for these two variables.

pizza_cost = 5.00
hamburger_cost = 6.35
fries_cost = 2.00
soda_cost = 1.00
water_cost = 0.75

lunch_menu ={
    'pizza':  pizza_cost,
    'hamburger': hamburger_cost,
    'fries': fries_cost,
    'soda': soda_cost,
    'water': water_cost,
    }

for key, value in lunch_menu.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")   
