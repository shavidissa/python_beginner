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

# making arguments optional

def get_formatted_name(first_name, last_name, middle_name=""):
    """Information about the name"""

    if middle_name:
    # Python interprey non empty strings as true
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        full_name = f"{first_name}  {last_name}"
    return full_name

musician = get_formatted_name("john", "hooker", "lee")
print(musician)

musician = get_formatted_name("taylor", "swift")
print(musician)

# Returning a dictionary
# None can be thought of as a pace holder value

def build_person(first_name, last_name, age=None):
    """Insert person information"""
    person = {"first": first_name, "last": last_name}
    if age:
        person["age"] = age
    return person

musician = build_person("jimi", "Lopex", 27)
print(f"dictionary return: {musician}")

# using a fucntion in a loop

def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# an infinite loop
while True:
    print("\nPlease enter your full name:")
    print("(Enter `q` at any time to quit)")

    f_name = input("Enter your first name: ")
    if f_name == "q":
        break

    l_name = input("Enter your last name: ")
    if l_name =="q":
        break

    formatted_name = get_formatted_name(f_name, l_name)
    print(f"Your full name is: {formatted_name}")