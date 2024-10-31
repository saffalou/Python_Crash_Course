# you can use the continue statement to return to the beginning of the loop, based on the result of a conditional test.

current_number = 0
while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
# we will only print numbers that satisfy the modulo test and are less than 10
    print(current_number)

