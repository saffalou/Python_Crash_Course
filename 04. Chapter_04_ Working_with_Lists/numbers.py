#range  function
# the last value printed out will be end of range value - 1
#The range() function causes Python to start counting at the first value you give it, and it stops when it reaches the second value you give it
for value in range(1, 21):
    print(value)

# notice how the output starts at 0 when no start value is given
for numbers in range(10):
        print(numbers)

# using the range function to create a list of numbers
#When you wrap list() around a call to the range() function, the output will be a list of numbers.
number_list = list(range(1, 16))
print(number_list)

#manipulating how we use a range function
# we can use the step value to tell the range function how big of steps to take between each number
# if we don't provide a step value, it will default to 1
# range(1, 21, 2) will print out all the odd numbers between 1 and 20. The tird parameter is the "step" size
odd_numbers = list(range(1, 21, 2))
print(odd_numbers)


#creating a list of squares
squares = []
for value in range(1, 11):
    square = value**2
    squares.append(square)
print(squares)

#some siomple manipulation of numbers in list
number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(min(number_list))
print(max(number_list))
print(sum(number_list))
print(len(number_list))