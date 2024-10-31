import random

# 7-1. Rental Car: Write a program that asks the user what kind of rental car they would like. Print a message about that car, such as “Let me see if I can find you a Subaru.” 
car_model = input('What model of car are you looking for?: ')
car_color = random.choice(['red', 'blue', 'green', 'black', 'white', 'yellow'])

print(f'Let me see if I can find you a {car_model}. I think we have a {car_color} one out in the back lot!')


# 7-2. Restaurant Seating: Write a program that asks the user how many people are in their dinner group. 
# If the answer is more than eight, print a message saying they’ll have to wait for a table. 
# Otherwise, report that their table is ready. 

diners = int(input('How many diners are there? Please enter a whole number value: '))

if diners > 8:
    print('You have to wait for a table.')
else:
    print('Your table is ready.')

# 7-3. Multiples of Ten: Ask the user for a number, and then report whether the number is a multiple of 10 or not.

number = input('Please enter a number between 1 and 1000 and I will tell you if it is a multiple of 10: ')

if int(number) % 10 == 0:
    print(f'{number} is a multiple of 10.')
else:
    print(f'{number} is not a multiple of 10.')
