# Often, you’ll want to start with an existing list and make an entirely new list based on the first one.

fruits_in_stock = ['Mango', 'Pineapple', 'Papaya', 'Guava', 'Passionfruit', 'Kiwi', 'Dragon Fruit', 'Rambutan', 'Mangosteen', 'Starfruit']
new_fruits = fruits_in_stock[:]
print(new_fruits)

print(len(fruits_in_stock))
print(len(new_fruits))


print(fruits_in_stock[1:5])

new_fruits.append('Longnang')
new_fruits.append('Lychee')
new_fruits.append('Watermelon')
print(new_fruits)

# we can see that the new fruits have been added only to the new_fruits list. fruits_in_stock is unchanged.
print(len(fruits_in_stock))
print(len(new_fruits))

my_favourite_fruits = new_fruits[0:14:3]
print(my_favourite_fruits)

# and we can combine lists using +
all_fruits = fruits_in_stock + new_fruits
print(all_fruits)

list_1 = [fruit for fruit in fruits_in_stock]
print(list_1)
print('\n')

list_2 = [fruit for fruit in all_fruits]
print(f'This is a list of all fruit in the shop {list_2}')