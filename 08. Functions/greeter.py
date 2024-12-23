# This example shows the simplest structure of a function. 
# The first line uses the keyword def to inform Python that you’re defining a function. 
# This is the function definition, which tells Python the name of the function and, if applicable, what kind of information the function needs to do its job. 
# The parentheses hold that information. In this case, the name of the function is greet_user(), 
# and it needs no information to do its job, so its parentheses are empty. (Even so, the parentheses are required.) 
# Finally, the definition ends in a colon. Any indented lines that follow def greet_user(): make up the body of the function. 
# The text on the second line is a comment called a docstring, which describes what the function does. 
# When Python generates documentation for the functions in your programs, it looks for a string immediately after the function's definition. 
# These strings are usually enclosed in triple quotes, which lets you write multiple lines.

#The line print("Hello!") is the only line of actual code in the body of this function, 
# so greet_user() has just one job: print("Hello!"). When you want to use this function, you have to call it. 
# A function call tells Python to execute the code in the function. 
# To call a function, you write the name of the function, followed by any necessary information in parentheses. 
# Because no information is needed here, calling our function is as simple as entering greet_user().


def greet_user():
    """Display a simple greeting."""
    print("Hello!")

greet_user()




# we can make this example a bit more complex by adeding a user name as an argument to the function.

def greet_user(name):
    """Display a personalized greeting."""
    print(f"Hello, {name}!")

greet_user("Pedro")  # This will print "Hello, Pedro!"

greet_user('Sarah')  # This will print "Hello, Sarah!"

greet_user('John')  # This will print "Hello, John!"