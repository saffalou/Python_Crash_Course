# the while loop runs as long as, or while, a certain condition is true.

current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

message = ""
while message != 'quit':
    message = input(prompt)
# we only output the message if it is not 'quit'
    if message != 'quit':
        print(message)

