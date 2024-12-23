# 8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the text of a message that should be printed on the shirt. 
# The function should print a sentence summarizing the size of the shirt and the message printed on it. 
# Call the function once using positional arguments to make a shirt. 
# Call the function a second time using keyword arguments. 

def make_shirt(shirt_size, message):
        
        return f"\nYou have ordered Shirt size: '{shirt_size}' with Message: '{message}'"
            

Dave_shirt = make_shirt("large", "This is my Tshirt message")

Deb_shirt = make_shirt("small", "Merry Christmas")


print(Dave_shirt)

print(Deb_shirt)


# 8-4. Large Shirts: Modify the make_shirt() function so that shirts are large by default with a message that reads I love Python. 

# Make a large shirt and a medium shirt with the default message, and a shirt of any size with a different message. 
def make_shirts(shirt_size = "large", message = "I love Python"):
        
        return f"\nYou have ordered Shirt size: '{shirt_size}' with Message: '{message}'"

Peter_shirt = make_shirts()

Mary_shirt = make_shirts('medium')

Bruce_shirt = make_shirts('small', 'Python for the win')

Leon_shirt = make_shirts(message = "Python with keyword arguments", shirt_size = 'Extra Large')

print(Peter_shirt)

print(Mary_shirt)

print(Bruce_shirt)

print(Leon_shirt)


# 8-5. Cities: Write a function called describe_city() that accepts the name of a city and its country. 
# The function should print a simple sentence, such as Reykjavik is in Iceland. 
# Give the parameter for the country a default value. 
# Call your function for three different cities, at least one of which is not in the default country.

def describe_city(city, country = "Australia"):
        
        return f"You requested city '{city}' which is part of '{country}'"


question_1 = describe_city('Melbourne')

question_2 = describe_city('London', 'England')

question_3 = describe_city(country = "Thailand", city = "Bangkok")


print(question_1)

print(question_2)

print(question_3)