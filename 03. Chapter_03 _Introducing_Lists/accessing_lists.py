# A list is a collection of items in a particular order.
# In Python, square brackets ([]) indicate a list, and individual elements in the list are separated by commas.


bicycles = ['trek', 'cannondale', 'redline', 'specialized']
# If you ask Python to print a list, Python returns its representation of the list, including the square brackets:
print(bicycles)

# Lists are ordered collections, so you can access any element in a list by telling Python the position, or index, of the item desired.
# Note how the value is returned without the square brackets
print(bicycles[0])
print(bicycles[1])
print(bicycles[2])
print(bicycles[3])

# We can also apply formatting to lists
print(bicycles[0].title())

#If you want to access the last item in the list, you can use the index -1
print(bicycles[-1].title())

# or the second last item
print(bicycles[-2].title())
# This syntax is quite useful, because you’ll often want to access the last items in a list without knowing exactly how long the list is. 
# This convention extends to other negative index values as well. 
# The index -2 returns the second item from the end of the list, the index -3 returns the third item from the end, and so forth.

# Combining list items into output
print(f'My first bicycle was a {bicycles[0].title()} and then I upgraded to a {bicycles[-1].title()}')


names = ['harry', 'hermione', 'ron', 'ginny', 'luna', 'dobby']

print(names[0]) #Harry
print(names[1]) #Hermione
print(names[2]) #Ron
print(names[3]) #Ginny
print(names[4]) #Luna
print(names[5]) #Dobby
print('\n')

print((f'Hello {names[0].title()}!'))   #Hello Harry!
print((f'Hello {names[1].title()}!'))   #Hello Hermione!
print((f'Hello {names[2].title()}!'))   #Hello Ron!
print((f'Hello {names[3].title()}!'))   #Hello Ginny!
print((f'Hello {names[4].title()}!'))   #Hello Luna!
print((f'Hello {names[5].title()}!'))   #Hello Dobby!
print('\n')


# Looping through a list (this is not in chapter 3 stuff)

for name in names:
    print(f'Hello and welcome {name.title()}!')
