# 5-3. Alien Colors #1: 
# Imagine an alien was just shot down in a game. Create a variable called alien_color and assign it a value of 'green', 'yellow', or 'red'. 
# Write an if statement to test whether the alien’s color is green. 
# If it is, print a message that the player just earned 5 points. 
# Write one version of this program that passes the if test and another that fails. (The version that fails will have no output.)

# alien_color = 'green'
alien_color = 'yellow'

if alien_color == 'green':
    print("You just shot down a green alient. You just earned 5 points!")


# 5-4. Alien Colors #2: 
# Choose a color for an alien as you did in Exercise 5-3, and write an if-else chain. 
# If the alien’s color is green, print a statement that the player just earned 5 points for shooting the alien. 
# If the alien’s color isn’t green, print a statement that the player just earned 10 points. 
# Write one version of this program that runs the if block and another that runs the else block.

alien = 'green'
#alien = 'yellow'
if alien == 'green':
    print("You just shot down a green alient. You just earned 5 points!")
else:
    print("You just shot down a red alient. You just earned 10 points!")

# 5-5. Alien Colors #3: 
# Turn your if-else chain from Exercise 5-4 into an if-elif-else chain. 
# If the alien is green, print a message that the player earned 5 points. 
# If the alien is yellow, print a message that the player earned 10 points. 
# If the alien is red, print a message that the player earned 15 points.

#alien = 'green'
#alien = 'yellow'
alien = 'red'
if alien == 'green':
    print("You just shot down a green alient. You just earned 5 points!")

elif alien == 'yellow':
    print("You just shot down a red alient. You just earned 10 points!")

else:
    print("You just shot down a red alient. You just earned 15 points!")


alien_1 = 'yellow'
alien_2 = 'green'
alien_3 = 'blue'
alien_4 = 'red'
if alien_1 == 'green':
    print("You just shot down a green alien. You just earned 5 points!")

elif alien_2 == 'yellow':
    print("You just shot down a red alien. You just earned 10 points!")

elif alien_3 == 'red':
    print("You just shot down a red alien. You just earned 15 points!")

elif alien_1 =='yellow' and alien_2 =='green' and alien_3 == 'blue' and alien_4 == 'red':
    print("You just shot down all the aliens in the secret combination. You just earned 1500 points!")

# 5-6. Stages of Life: 
# Write an if-elif-else chain that determines a person’s stage of life. 
# Set a value for the variable age, and then: 
# If the person is less than 2 years old, print a message that the person is a baby. 
# If the person is at least 2 years old but less than 4, print a message that the person is a toddler. 
# If the person is at least 4 years old but less than 13, print a message that the person is a kid. 
# If the person is at least 13 years old but less than 20, print a message that the person is a teenager. 
# If the person is at least 20 years old but less than 65, print a message that the person is an adult. 
# If the person is age 65 or older, print a message that the person is an elder.

age = 66
if age < 2:
    print("This person is a baby.")
elif age >= 2 and age < 4:
    print("This person is a toddler.")
elif age >= 4 and age < 13:
    print("This person is a kid.")
elif age >= 13 and age < 20:
    print("This person is a teenager.")
elif age >=20 and age < 65:
    print("This person is an adult.")
else:
    print("This person is an elder.")

# 5-7. Favorite Fruit: 
# Make a list of your favorite fruits, and then write a series of independent if statements that check for certain fruits in your list. 
# Make a list of your three favorite fruits and call it favorite_fruits. 
# Write five if statements. Each should check whether a certain kind of fruit is in your list. 
# If the fruit is in your list, the if block should print a statement, such as You really like bananas!

favorite_fruits = ['apple', 'banana', 'pineapple']
fruit = 'banana'
fruit_1 = 'pear'
fruit_2 = 'apple'
fruit_3 = 'mango'
fruit_4 = 'pineapple'

if fruit in favorite_fruits:
    print(f"You really like {fruit}!")

if fruit not in favorite_fruits:
    print(f"I know you like {fruit} but we are all out of them!")

if fruit_1 in favorite_fruits:
    print(f"You really like {fruit_1}!")

if fruit_1 not in favorite_fruits:
    print(f"I know you like {fruit_1} but we are all out of them!")

if fruit_2 in favorite_fruits:
    print(f"You really like {fruit_2}!")

if fruit_2 not in favorite_fruits:
    print(f"I know you like {fruit_2} but we are all out of them!")

if fruit_3 in favorite_fruits:  
    print(f"You really like {fruit_3}!")

if fruit_3 not in favorite_fruits:
    print(f"I know you like {fruit_3} but we are all out of them!")

if fruit_4 in favorite_fruits:  
    print(f"You really like {fruit_4}!")

if fruit_4 not in favorite_fruits:  
    print(f"I know you like {fruit_4} but we are all out of them!")



