# this loop will use title case for all but BMW which requires uppercase
cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())

# Conditional Tests
# At the heart of every if statement is an expression that can be evaluated as True or False 
# and is called a conditional test. 
# Python uses the values True and False to decide whether the code in an if statement should be executed. 
# If a conditional test evaluates to True, Python executes the code following the if statement. 
# If the test evaluates to False, Python ignores the code following the if statement.


# Testing whether a Value is True or False
#checking for equality
country = 'Japan'

if country == "Japan":
        print(f'Yes, we know about {country.title()}!') 
        
else:
        print(f"We don't know anything about {country.title()}!")

countries = ["France", "Japan", "Australia", "Brazil", "South Africa"]     
destination = "Japan"

if destination in countries:
        print(f'Yes, we know about {destination.title()} and can help you travel there!')
else:
        print(f"We don't know anything about {destination.title()}!")   


car = 'Audi'
car.lower() == 'audi'

if car.lower() == 'audi':
      print(f'Yes, we have an {car} in stock!')

# checking for inequality
pizza_topping = "Pepperoni"

if pizza_topping != 'Pepperoni':
    print(f'No pepperoni for this pizza!')
else:
    print(f'Plenty of pepperoni on this one!')




    