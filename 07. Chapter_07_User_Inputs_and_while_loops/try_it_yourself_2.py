# 7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value.
# As they enter each topping, print a message saying you’ll add that topping to their pizza.

toppings = input('What topping do you want on your pizza? Enter "quit" when you have added all required toppings: ')
requested_toppings = []

while toppings != "quit":
        print(f"Adding {toppings} to your pizza")
        requested_toppings.append(toppings)
        toppings = input('What topping do you want on your pizza? Enter "quit" when you have added all required toppings: ')
        if toppings == "quit":
            print(f"Your pizza will be ready in 15 minutes with the following toppings: {requested_toppings}")


 
# 7-5. Movie Tickets: A movie theater charges different ticket prices depending on a person’s age. 
# If a person is under the age of 3, the ticket is free; if they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. 
# Write a loop in which you ask users their age, and then tell them the cost of their movie ticket. 

age = int(input("How old are you?: "))
under_3 = 'free'
from_3_to_12 = '$10'
over_12 = '$15'

if age < 3:
    print(f'Your ticket is {under_3}')
elif age >= 3 and age <= 12:
    print(f'Your ticket cost is {from_3_to_12}')
else:
    print(f'Your ticket cost is {over_12}')



# 7-6. Three Exits: Write different versions of either Exercise 7-4 or 7-5 that do each of the following at least once: 
# Use a conditional test in the while statement to stop the loop. 
# Use an active variable to control how long the loop runs. Use a break statement to exit the loop when the user enters a 'quit' value. 
# 
age = int(input("How old are you? "))
under_3 = 'free'
from_3_to_12 = '$10'
over_12 = '$15'
temperature = 90                                           # we will issue 2 tickets at a price and then we will issue a free ice cream and a cold drink because the temperature is greater than 100
while temperature < 100:                      
        if age < 3:
         print(f'Your ticket is {under_3}')
        elif age >= 3 and age <= 12:
         print(f'Your ticket cost is {from_3_to_12}')
        else:
         print(f'Your ticket cost is {over_12}')
        temperature += 9                                    # the numer of times we run the while loop depends on this increment.
if temperature >= 100:
           print(f'Your ticket is free and you get a free ice cream and cold drink')


#adding break into the loop
while True:
    consent = input("Do you want to continue and buy a ticket? Enter yes or no: ")
    if consent.lower() == "no":
        print("OK, have a nice day and we'll see you back here soon")
        break
    else:
        age = int(input("How old are you?: "))
        under_3 = 'free'
        from_3_to_12 = '$10'
        over_12 = '$15'

        if age < 3:
            print(f'Your ticket is {under_3}')
        elif age >= 3 and age <= 12:
            print(f'Your ticket cost is {from_3_to_12}')
        else:
            print(f'Your ticket cost is {over_12}')
            break

                                        






# 
# 
# 7-7. Infinity: Write a loop that never ends, and run it. (To end the loop, press CTRL-C or close the window displaying the output.)
# as there is no increment in the loop the variable will always be less than 12 making this an infinite loop
#remarking this out unless it needs to be run
#num = 10
#while num < 12:
 #   print(num)