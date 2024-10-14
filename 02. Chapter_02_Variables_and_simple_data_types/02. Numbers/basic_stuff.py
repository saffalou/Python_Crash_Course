int_1 = 10
int_2 = 5
int_3 = 8
int_4 = 3
int_5 = 2

#floats
dec_1 = 0.5
dec_2 = 0.25
dec_3 = 0.33224
dec_4 = 0.123
dec_5 = 0.2
dec_6 = 0.1
dec_7 = 2.0


print(int_1 + int_2)
print(int_2*int_5)
print(int_3/int_5)
print(int_1 %3)

print(dec_1 + dec_3)

print(int_1 * dec_3)

print(dec_5 + dec_6)

#dividing any 2 numbers always results in a float
#Python defaults to a float in any operation that uses a float, even if the output is a whole number.

print(int_1 / int_5)

#mixing an integer and a float will result in a float
print(int_1 + dec_5)
print(int_5 + dec_7)
print(int_5 + int_5) # same value but is not output as float like line above

#can use underscores to help make long numbers more readable. This does not impact how python uses the value
long_num_1 = 10000
long_num_2 = 10_000
print(long_num_1)
print(long_num_2)
print(long_num_1 + long_num_2)