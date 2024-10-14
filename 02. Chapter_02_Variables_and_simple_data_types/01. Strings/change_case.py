#manipulate strings

name = 'Elton hercules john'

print(name.lower()) #lowercase
print(name.upper()) #uppercase
print(name.title()) #capitalize the first letter of each word

first_name = 'Michael'
surname = 'Mouse'
full_name = f'{first_name} {surname}'
new_name = 'Ada Average'
# use formatting methods in the variable
full_name_tweak = f'{first_name.lower()} {surname.upper()}'
print(first_name.lower())
print(surname.upper())
print(full_name.title())
#can use this to add a new line between output lines
print('\n')

#or can do it this way
print(new_name.title(),'\n')

#use an f string to target the case to each field
print(f'The next person in queue is {first_name.title()} {surname.upper()}')
print('\n')

print('The name will print as lower case first name and upper case surname: ' + full_name_tweak, '\n')

#Add tabs to output (can be combined with newline)
print('\t' + full_name_tweak +'\n')   #check the output. This output starts one tab to the right compared to the line below
print(full_name_tweak)