# A for loop is effective for looping through a list, but you shouldn’t modify a list inside a for loop 
# because Python will have trouble keeping track of the items in the list. 
# To modify a list as you work through it, use a while loop. 
# Using while loops with lists and dictionaries allows you to collect, store, and organize lots of input to examine and report on later.

# Start with users that need to be verified,
#  and an empty list to hold confirmed users.
unconfirmed_users = ['alice', 'brian', 'candace']
confirmed_users = []

# Verify each user until there are no more unconfirmed users.
#  Move each verified user into the list of confirmed users.
while unconfirmed_users:
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

# Display all confirmed users.
print("\nThe following users have been confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())

#add this to confirm that we have processed all unconfirmed users
print(f'\nWe have the following unconfirmed users {unconfirmed_users}')


# removing all  duplicates from a list using while loop

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat', 'goldfish', 'dog', 'dog']

print(f'Before removing dogs from the list: {pets}')

while 'dog' in pets:
    pets.remove('dog')

print(f'After removing dogs from the list: {pets}') 

# remember if we did using remove() we would only remove the first instance in the list and would need to re-execute until all instances removed
# as example

counter = 0 
for cat in pets:
    if cat == 'cat':
        counter += 1
print(f'\nThere are {counter} cats in the list') #prints 3 as there are 3 instances of cat in the list (counter)


pets.remove('cat')

print(f'\nAfter removing cat from the list: {pets} we only have 1 less instance in the list') # this because .remove() doesn't iterate through the list

counter = 0 
for cat in pets:
    if cat == 'cat':
        counter += 1
print(f'\nThere are {counter} cats in the list') #prints 2 as there are 2 instances of cat in the list