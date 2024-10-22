# If the list is empty, we’ll prompt the user and make sure they want a plain pizza. 
# If the list is not empty, we’ll build the pizza

# When the name of a list is used in an if statement, Python returns True 
# if the list contains at least one item; an empty list evaluates to False.

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
    print("\nFinished making your pizza!")
else:
    print("Are you sure you want a plain pizza?")

