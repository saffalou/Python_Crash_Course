# this is the same code as in positional_arguments.py
# however now we explicitly tell python what parameter we are passing
# passing the parameters in a different oprder is now not a problem

def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    print(f"\nI have a {animal_type}.")
    print(f"My {animal_type}'s name is {pet_name.title()}.")

describe_pet('hamster', 'harry')

describe_pet('beagle', 'Lou')

# wrong parameter order is a problem
describe_pet('harry', 'hamster')

# the changed parameter order doesn't matter as we are using keyword arguments
describe_pet(pet_name = 'harry', animal_type = 'hamster')

# and passing the parameter values in the same order is also fine
describe_pet(animal_type = 'hamster', pet_name = 'harry')