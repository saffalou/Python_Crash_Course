# The keys() method is useful when you don’t need to work with all of the values in a dictionary.
# This for loop tells Python to pull all the keys from the dictionary lunch_menu and 
# assign them one at a time to the variable name menu_item.
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

print('our menu has the following items avaialable for order today:')
for menu_item in lunch_menu.keys():
    print(f'{menu_item.title()}  : $ {lunch_menu[menu_item]:.2f}')


# Looping through the keys is actually the default behavior when looping through a dictionary, 
# so this code would have exactly the same output if .keys() wasn’t included.

print('our menu has the following items avaialable for order today:')
for menu_item in lunch_menu:
    print(f'{menu_item.title()}  : $ {lunch_menu[menu_item]:.2f}')


# accessing specific keys in a dictionary

roast_lamb = 10.00
roast_pork = 12.00  
roast_beef = 15.00
schnitzel = 8.00
chicken_parma = 9.00
lamb_chops = 12.00

specials_menu = ['roast lamb', 'lamb chops']

carvery_menu = {
    'roast lamb': roast_lamb,
    'roast pork': roast_pork,
    'roast beef': roast_beef,
    'schnitzel': schnitzel,
    'chicken parma': chicken_parma,
    'lamb chops': lamb_chops,
    }

for menu_item in carvery_menu:
    if menu_item in specials_menu:
        print(f"Special Deal: {menu_item.title()} - ${carvery_menu[menu_item]:.2f}")
    else:
        print(f"{menu_item.title()} - ${carvery_menu[menu_item]:.2f}")   # .2f rounds up to 2 decimal places

for menu_item in carvery_menu.keys():
    if 'roast chicken' not in menu_item:
        print("Sorry, we don't have roast chicken.")
        exit()