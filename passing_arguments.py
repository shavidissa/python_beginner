#psotional arguments
# when you pass arguemtns to a function and they are taken in the order that was provided.
# order is key in positional arguments

def describe_pet(animal_type, animal_name):
    """Display information about a pet"""
    print(f"The animal is a {animal_type.lower()}.")
    print(f"It's name is {animal_name.title()}.")

describe_pet("dog", "Nigel")
describe_pet("cat", "Shumai")

# keyword arguments
# you pass the value to the function as key-value pairs

describe_pet(animal_type="bird", animal_name="Tweetiya")

# adding a default value. Example to the varianle animal_type
# when using default values, you need to add the variable with the default value
# needs to be listed after the varialbsles that don't ahve default values.This
# allows Python to continue interpreting positional arguments correctly.

def describe_pet(pet_name, animal_type="dog"):
    """Display information about a pet"""
    print(f"\nThis is a {animal_type}.")
    print(f"It's name is {pet_name.title()}.")

describe_pet(pet_name="Willie")