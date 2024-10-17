#list comprehension structure
# begin with a descriptive name for the list, such as squares. 
# open a set of square brackets and define the expression for the values you want to store in the new list. 
# In this example the expression is value**2, which raises the value to the second power. 
# Then, write a for loop to generate the numbers you want to feed into the expression, and close the square brackets. 
# The for loop in this example is for value in range(1, 11), which feeds the values 1 through 10 into the expression value**2. 
# Note that no colon is used at the end of the for statement.

# squares = [value**2 for value in range(1, 11)]
# print(squares)

#Create an identical list from the first list using list comprehension
lst1=[1,2,3,4,5]
lst2 = [number for number in lst1]
print(lst2)

#or, more direct way
lst2_a = [value+1 for value in range(0, 5)]   
print(lst2_a)

# Create a list from the elements of a range from 1200 to 2000 with steps of 130, using list comprehension.
rng = [value for value in range(1200, 2001, 130)]
print(rng)

# Use list comprehension to contruct a new list but add 6 to each item.
start_list = [44,54,64,74,104]
plus_6 = [num +6 for num in start_list]
print(plus_6)

# Generate a list of characters from a string
chars = [char for char in 'hello world']
print(chars)

alphabet_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
alphabet_upper = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

#lowercase letters
alpha_upper = [alpha.upper()for alpha in alphabet_lower]
print(alpha_upper)

#uppercase letters
alpha_lower = [alpha.lower()for alpha in alphabet_upper]
print(alpha_lower)