# Python refers to values that cannot change as immutable
# an immutable list is called a tuple.

# A tuple looks just like a list, except 
# you use parentheses instead of square brackets. 
# Once you define a tuple, you can access individual elements by using each item’s index, just as you would for a list.

dimensions = (50, 10)

print(dimensions[0])
print(dimensions[1])  
#calculate the dimensions 
print(dimensions[0] * dimensions[1])

# if we try to change a dimension, it will throw an error "TypeError: 'tuple' object does not support item assignment"
# dimensions[0] = 100 (uncomment to see the error)

# if the above is done as a list instead of a tuple, we can change the list

sides = [50, 10]

print(sides[0] * sides[1])

sides[0] = 100

# no error and the list has been updated (check the print of dimensions)
print(sides[0] * sides[1])


# to loop through a tuple
for dimension in dimensions:
    print(dimension)

    #or
dimension_of_land = [sides for sides in dimensions]

print(dimension_of_land)









