# The input() function pauses your program and waits for the user to enter some text. 
# Once Python receives the user’s input, it assigns that input to a variable to make it convenient for you to work with.

message = input("Tell me something, and I will repeat it back to you: ")
print(message)


name = input("Please enter your name: ")
print(f"\nHello, {name}!")



# Using int() to accept numerical input


# When you use the input() function, Python interprets everything the user enters as a string. 
# Consider the following interpreter session, which asks for the user’s age:
age = input("How old are you? ")
print(age)

# if all we need is s tring value the above is fine.
# But if we need an integer value we need to use int() function


age = input("How old are you? ")
age = int(age)

if age >= 18:
    print("You are eligible to vote.")
else:
    print("You are not eligible to vote.")


height = input("How tall are you, in inches? ")
height = int(height)

if height >= 48:
    print("\nYou're tall enough to ride!")
else:
    print("\nYou'll be able to ride when you're a little older.")

