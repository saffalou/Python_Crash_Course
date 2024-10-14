# To change an element, use the name of the list followed by the index of the element you want to change, and then provide the new value you want that item to have.

names = ['Harry', 'Hermione', 'Ron', 'Ginny', 'Luna', 'Dobby']
print(names)
print(names[5])  #Dobby

names[5] = 'Hagrid'  #change Dobby to Hagrid
print(names)

names[3] = 'Cedric'  #change Ginny to Cedric
print(names)

print(names[5])    #Hagrid

names.append('Ogre')  #add to the end of the list
print(names)


#build a list using append
fruit_bowl = []
print(fruit_bowl)
fruit_bowl.append('banana')
print(fruit_bowl)
fruit_bowl.append('apple')
print(fruit_bowl)
fruit_bowl.append('orange')
print(fruit_bowl)
fruit_bowl.append('grapes')
print(fruit_bowl)
fruit_bowl.append('pineapple')
print(fruit_bowl)


#inserting data into a specific position in the list
fruit_bowl.insert(2, 'pear')  #pear is added to the list and will appear bewfore orange
print(fruit_bowl)
print('\n')

#removing items from a list
print(fruit_bowl)
fruit_bowl.remove('apple')  #apple is removed from the list
print(fruit_bowl)
print('\n')


#using pop() to remove an item from the list
#.pop() allows us to remove an item from a list but also retain that item in a variable for later use
# you either pop from the end of the list "pop()" or from a specific position "pop(index_position)"
print(f'The fruit bowl contains {fruit_bowl}')  #the original list is printed before the pop() is performed (the original list is not modified in this fruit_bowl)
popped_fruit = fruit_bowl.pop()  #the last item in the list is removed
print(f'The fruit bowl now contains {fruit_bowl} because {popped_fruit} was removed from the list')
print(popped_fruit)


animals = ['cat', 'dog', 'rabbit', 'guinea pig', 'snake', 'lizard', 'penguin', 'parrot']
# remove from a list by position
print(animals)

out_of_stock =animals.pop(4)    #snake is removeds from list
print(f'{out_of_stock} is out of stock') #snake is printed out of stock (snake is out_of_stock)
print(animals)

#remove by name (when you don't know the position of the iktem to be removed)
#by using a vriable for the removed  animal I can keep track of what was removed and access it later
print(animals)
removed_animal = 'lizard'
animals.remove(removed_animal)
print(animals)
print(removed_animal)

