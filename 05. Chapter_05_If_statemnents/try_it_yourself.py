# 5.1 conditional tests
# car = 'subaru'
#print("Is car == 'subaru'? I predict True.")
#print(car == 'subaru')
#print("\nIs car == 'audi'? I predict False.")
# print(car == 'audi')




car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')


fruit = 'apple'
print("Is fruit == apple? I predict True.")
print(fruit == 'apple')

print("Is fruit == apple? I predict False.")
print(fruit == 'orange')


string_1 = 'abc'
string_2 = 'def'
string_3= 'abc'
string_4 = 'abcdef'


print(string_1 == string_2, 'this is false')  #false
print(string_1 == string_3, 'this is true')  #true
print(string_1 == string_4, 'this is false')  #false
print(string_4 == string_1 + string_2, 'this is true')  #true


num_1 = 11
num_2 = 20
num_3 = 10
num_4 = 20
num_5 = 200

print(num_1 < num_2, 'this is true')  #true
print(num_1 == num_3, 'this is true')  #true
print(num_1 > num_4, 'this is false')  #false

print(num_1*2 == num_2, 'this is true')  #true
print(num_1*num_2 == num_5, 'this is true')  #true

if num_1*num_2 == num_5:
    print(f'the value of {num_1}*{num_2} is {num_5}')
else:
    print(f'this is false. The value of {num_1}*{num_2} is not {num_5} but {num_1*num_2}')