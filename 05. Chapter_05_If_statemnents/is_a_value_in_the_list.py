pizza_toppings = ["Pepperoni", "Mushrooms", "Extra Cheese", "Bacon", "Olives"]

if "Pepperoni" and "Pineapple"in pizza_toppings:
    print("Pepperoni and Pineapple is in the list of toppings")

else:
    print("Pepperoni and Pineapple are not in the list of toppings")


request_1 = "Pineapple"
request_2 = "Mushrooms"

# check if request topping 2 is in list of pizza toppings.
# if not in list return this to user
if  request_1 in pizza_toppings and request_2 not in pizza_toppings:
    print(f"We don't offer {request_2} in the list of toppings")

# check if request topping 1 is in list of pizza toppings.
# if not in list return this to user
elif request_1 not in pizza_toppings and request_2 in pizza_toppings:
    print(f"We don't offer {request_1} in the list of toppings")

# if both requested toppings are in list of pizza toppings, return this message to user
else:
    request_1 in pizza_toppings and request_2 in pizza_toppings
    print(f"{request_1} and {request_2} are in the list of available toppings")


sunny = True
cloudy = False
rainy = False

# this loop is not testing all possible combinations of sunny, cloudy, and rainy
if sunny and not cloudy and not rainy:
    print('Today will be clear skies, sunny and no rain')

elif sunny and cloudy and not rainy:
    print('Today will be cloudy, sunny and no rain')

elif sunny and not cloudy and rainy:
    print('Today will be sunny, cloudy and rain')

elif not sunny and cloudy and not rainy:
    print('Today will be cloudy, cloudy and no rain')

else:
    print('Today will be cloudy, cloudy and rain')

