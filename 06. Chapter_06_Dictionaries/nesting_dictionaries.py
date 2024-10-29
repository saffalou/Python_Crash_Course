# Sometimes you’ll want to store multiple dictionaries in a list, 
# or a list of items as a value in a dictionary. 
# This is called nesting. 
# You can nest dictionaries inside a list, a list of items inside a dictionary, or even a dictionary inside another dictionary.

# A list of dictionaries
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# Make an empty list for storing aliens.
aliens = []

# Make 30 green aliens.
for alien_number in range(30):
     new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
     aliens.append(new_alien)

# Show the first 5 aliens.
for alien in aliens[:5]:
    print(alien)
print(".........")

# Show how many aliens have been created.
print(f"Total number of aliens: {len(aliens)}")



#we can modify the above to introduce new aliens with different colors and speeds
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

for alien in aliens[:5]:
    print(alien)
print(".........")
    

#or we can modify further
for alien in aliens[:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

for alien in aliens[:5]:
    print(alien)
print(".........")