# The if-elif-else chain is powerful, but it’s only appropriate to use when you just need one test to pass. 
# As soon as Python finds one test that passes, it skips the rest of the tests. 
# This behavior is beneficial, because it’s efficient and allows you to test for one specific condition. 
# However, sometimes it’s important to check all conditions of interest. 
# In this case, you should use a series of simple if statements with no elif or else blocks. 
# This technique makes sense when more than one condition could be True, 
# and you want to act on every condition that is True.


requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")

if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")

if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")


# In summary, if you want only one block of code to run, use an if-elif-else chain. 
# If more than one block of code needs to run, use a series of independent if statements.


