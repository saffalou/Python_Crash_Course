# When writing a function, you can define a default value for each parameter. If an argument for a parameter is provided in the function call, Python uses the argument value. If not, it uses the parameter’s default value. So when you define a default value for a parameter, you can exclude the corresponding argument you’d usually write in the function call. Using default values can simplify your function calls and clarify the ways your functions are typically used.

def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet(pet_name='willie')


# here I provide a value for animal_type and it overrides the default value
describe_pet(pet_name = 'Buzz', animal_type = 'Horse')


# Note that the order of the parameters in the function definition had to be changed. 
# Because the default value makes it unnecessary to specify a type of animal as an argument, 
# the only argument left in the function call is the pet’s name. Python still interprets this as a positional argument, 
# so if the function is called with just a pet’s name, that argument will match up with the first parameter 
# listed in the function’s definition. This is the reason the first parameter needs to be pet_name.

# When you use default values, any parameter with a default value needs to be listed after all the parameters that don’t have default values. 
# This allows Python to continue interpreting positional arguments correctly.


