numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

for number in numbers:
    print(number)

print(list(range(1, 21)))

# 1 to 100 using range
number_list = list(range(1, 101))
print(number_list)

# 1 to 100 using a list without range
numbers_long = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

#both sets of print produce the same output
print(min(number_list))
print(max(number_list))
print(sum(number_list))

print(min(numbers_long))
print(max(numbers_long))
print(sum(numbers_long))


odd_numbers = list(range(1, 51, 2))
for odd_num in odd_numbers:
    print(odd_num)

threes = list(range(3, 31, 3))
for three in threes:
    print(three)

cubes = list(range(1, 11))
for cube in cubes:
   print(cube**3)
   
#the above  as a list comprehension approach
cube_comp = [x**3 for x in range(1, 11)]
print(cube_comp)