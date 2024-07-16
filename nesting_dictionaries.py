#Create several alien dictionaries and pass it on to an aliens list.

alien_0 = {"color": "green", "points": 5,}
alien_1 = {"color": "yellow", "points": 10,}
alien_2 = {"color": "red", "points": 15,}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)


# Create a list of 30 aliens using the range function. and then printing them.

aliens = []

# make 30 green aliens
for alien_number in range(30):
    new_alien = {"color": "green", "points": 5,}
    aliens.append(new_alien)

# print the first 5 aliens.
print("\nThe first five aliens")
print(aliens[:5])

# Using a loop to print the first 5 aliens

print("\nFirst 5 aliens using a for loop")
for alien in aliens[:5]:
    print(alien)

# Number of aliens that were created.
print(f"The number of aliens: {len(aliens)}")

# change the first 3 aleins in the list

for alien in aliens[:3]:
    if alien["color"] == "green":
        alien["color"] = "yellow"
        alien["speed"] = "medium"
        alien["points"] = 10
    elif alien["color"] == "yellow":
        alien["color"] = "red"
        alien["speed"] = "fast"
        alien["points"] = 15

for alien in aliens[:5]:
    print(alien)

# a list in a dictionary

pizza = {
    "curst": "thick",
    "toppings": ["mushrooms", "extra-cheese"],
}

#summarizing the order

print(f"\nYou orders a {pizza['curst']}-crust pizza"
      "and the following toppings:")

for topping in pizza["toppings"]:
    print(f"- {topping}")

# favorite language

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    }

for name, languages in favorite_languages.items():
    if len(languages) > 1:
        print(f"\n{name.title()}'s favorite langaues are:")
    else:
        print(f"\n{name.title()}'s favorite language is:")
    for language in languages:
        print(f"\t{language}")
    
# A dictionary in a dictionary

users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
        },
    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
        },
    }

for username, user_information in users.items():
    print(f"\nUsername: {username}")
    full_name = f"{user_information["first"]} {user_information["last"]}"
    location = user_information["location"]

    print(f"\tFull name:{full_name.title()}")
    print(f"\tLocations: {location.title()}")