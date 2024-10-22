age = 19

if age < 4:
    print("entry is free for you")

elif age < 18:
    print("entry is $25 for you")

else:
    print("entry is $40 for you \n")

# or we could do it this way

age = 19
if age < 4:
    price = 0
elif age < 18:
    price = 25
else:
    price = 40
print(f"Your admission cost is ${price}.")


#add a seniors pricing option
age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age <65:
    price = 40
else:
    price = 20
print(f"Your admission cost is ${price}.")

# python does not have to have an else block, the else block is optional
# we can sue elif instead
# With this change, every block of code must pass a specific test in order to be executed. 
# The else block is a catchall statement. 
# It matches any condition that wasn’t matched by a specific if or elif test, 
# and that can sometimes include invalid or even malicious data

age = 65
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age <65:
    price = 40
elif age >= 65:  
    price = 20
print(f"Your admission cost is ${price}.")

