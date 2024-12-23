# 7-8. Deli: Make a list called sandwich_orders and fill it with the names of various sandwiches. 
# Then make an empty list called finished_sandwiches. 
# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. 
# As each sandwich is made, move it to the list of finished sandwiches. 
# After all the sandwiches have been made, print a message listing each sandwich that was made.

sandwich_orders = ["BLT", "Club", "Reuben", "Grilled Cheese", "Turkey", "Ham and Cheese"]

sandwiches_made = []

for sandwich in sandwich_orders:
    print(f'Your {sandwich} has been made and is ready for collection')
    sandwiches_made.append(sandwich)

print(f'We made the following sandwiches: {sandwiches_made} today')

# 7-9. No Pastrami: Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
# Add code near the beginning of your program to print a message saying the deli has run out of pastrami, 
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders. 
# Make sure no pastrami sandwiches end up in finished_sandwiches.


sandwich_orders_1 = ["BLT", "Club", "Pastrami","Reuben", "Grilled Cheese", "Pastrami","Turkey", "Ham and Cheese", "Pastrami"]

sandwiches_made_1 = []

x = 0

for sandwich in sandwich_orders_1:
    
    if sandwich == "Pastrami":        
        print(f'\nSorry we are out of pastrami, we will not be able to make any more pastrami sandwiches')
        sandwich_orders_1.remove(sandwich)
        x +=1
    else:
        print(f'\nYour {sandwich} has been made and is ready for collection')
        sandwiches_made_1.append(sandwich)

print(f'\nWe made the following sandwiches: {sandwiches_made} today')

print(f"\nPastrami sandwiches have been removed from the list so we couldn't make {x} sandwich orders today" )


# 7-10. Dream Vacation: Write a program that polls users about their dream vacation. 
# Write a prompt similar to If you could visit one place in the world, where would you go? 
# Include a block of code that prints the results of the poll.

dream_location = []

while True:
    vacation = input('Where is your dream vacation destination?: ').title()

    dream_location.append(vacation)
    
    

    enough = input('Do you want to enter another destination, enter "yes" or "no": ').title()
    
    if enough.lower() != "no":
        print(f"Adding {vacation} to your dream vacation list")
        
        
    else:
        print(f"Your dream vacation list will be ready in 15 minutes with the following destinations: {dream_location}")
        break

    
    
