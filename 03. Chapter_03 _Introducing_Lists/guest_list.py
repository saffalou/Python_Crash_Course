guest_list = ['Slash', 'Tommy', 'Randy', 'Santana']


print(f'Hello {guest_list[0]}, I would like to invite you to dinner.')

print(f'Hello {guest_list[1]}, I would like to invite you to dinner.')

print(f'Hello {guest_list[2]}, I would like to invite you to dinner.')

print(f'Hello {guest_list[3]}, I would like to invite you to dinner.')

amended_list = guest_list.pop(1)
print(f'{amended_list} can not make it to dinner.')

guest_list.insert(1, 'Spyder')

print(f'Hello {guest_list[0]}, I would like to invite you to dinner.')

print(f'Hello {guest_list[1]}, I would like to invite you to dinner.')

print(f'Hello {guest_list[2]}, I would like to invite you to dinner.')

print(f'Hello {guest_list[3]}, I would like to invite you to dinner.')
print('\n')

guest_list.insert(0, 'Jay Jay')
guest_list.insert(3, 'Joan')
guest_list.insert(-1, 'Rick')

print(f'Hello {guest_list[0]}, I now have a really big dining table so would like you to come and join my dinner party.')

print(f'Hello {guest_list[1]}, I now have a really big table so would like you to come and join my dinner party.')

print(f'Hello {guest_list[2]}, I now have a really big table so would like you to come and join my dinner party.')

print(f'Hello {guest_list[3]}, I now have a really big table so would like you to come and join my dinner party.')

print(f'Hello {guest_list[4]}, I now have a really big table so would like you to come and join my dinner party.')

print(f'Hello {guest_list[5]}, I now have a really big table so would like you to come and join my dinner party.')

print(guest_list)
print(amended_list)


pop_1 = guest_list.pop(0)
print(f"{pop_1} this really sucks but the furniture delivery is going to be late and I won't have my new dining table. We'll have dinner at some other time")

pop_2 = guest_list.pop(1)
print(f"{pop_2} this really sucks but the furniture delivery is going to be late and I won't have my new dining table. We'll have dinner at some other time")
pop_3 = guest_list.pop(2)
print(f"{pop_3} this really sucks but the furniture delivery is going to be late and I won't have my new dining table. We'll have dinner at some other time")
pop_4 = guest_list.pop(3)
print(f"{pop_4} this really sucks but the furniture delivery is going to be late and I won't have my new table. We'll have dinner at some other time")

print(f'Hey {guest_list[0]} things got weird with the furniture but the dinner party is still on')

print(f'Hey {guest_list[1]} things got weird with the furniture but the dinner party is still on')

print(guest_list)

del guest_list[0]   #deletes a guest from list
del guest_list[1]   #deletes a guest from list
guest_list.remove('Joan') #removes a guest from list

print(guest_list)    #retruns an empty list as all guests haveb been removed from list
