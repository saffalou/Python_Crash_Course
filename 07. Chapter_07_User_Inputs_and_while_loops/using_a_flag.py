# For a program that should run only as long as many conditions are true, 
# you can define one variable that determines whether or not the entire program is active. 
# This variable, called a flag, acts as a signal to the program. 
# We can write our programs so they run while the flag is set to True and stop running when any of several events sets the value of the flag to False.

prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# add in a flag
active = True
while active:
    message = input(prompt)
    

    if message == 'quit':
        active = False
#added this line just to see that when "quit" is entered the flag changes to False
        print(active)      #uncomment to see the active status as false
    else:
        print(message)
#added this line just to see that when "quit" is not entered the flag changes to True        
#       print(active)     #uncomment to see the active status as true


