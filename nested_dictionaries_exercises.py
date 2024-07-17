
# Exercixe 6.7: People
people = []

person =  {
     "first_name": "nic",
    "last_name": "nevin",
    "age": 32,
    "city": "boston",
}

people.append(person)

person = {
     "first_name": "josh",
    "last_name": "turner",
    "age": 60,
    "city": "amsterdam",
}

people.append(person)

person = {
    "first_name": "srah",
    "last_name": "ashley",
    "age": 19,
    "city": "virginia",
}

people.append(person)

for person in people:
    print(f"\nMy name is: {person["first_name"]} {person["last_name"]}")
    print(f"\tI am {person["age"]} years old.")
    print(f"\tI am from {person["city"].title()}")




# Exercise 6.8: Pets

pets = {
    "shimma": {
        "animal": "cat",
        "owner": "flora",
    },
    "lassi": {
        "animal": "dog",
        "owner": "jhon",
    },
    "parroty": {
        "animal": "parrot",
        "owner": "nic",
    },
}

for pet, pet_information in pets.items():
    print(f"\nThe pet's name is: {pet.title()}")
    print(f"\tThe pet is a: {pet_information["animal"]}")
    print(f"\tThe owner is: {pet_information["owner"].title()}")


# Exercice 6.9: Favorite places

favorite_places = {
    "sam": ["hawaii", "mexico"],
    "tan": ["bali", "india", "japan"],
    "don": ["sri lanka", "italy"],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()} likes to visit:")
    for place in places:
        print(f"\t{place.title()}")

#Exercise 6.9: Favorite number

favorite_numers = {
    "jim": [5],
    "kim": [17, 35, 95],
    "ted": [1000000, 1],
}

for name, numbers in favorite_numers.items():
    if len(numbers) > 1:
        print(f"\n{name.title()}'s favorite numbers are:")
    else:
        print(f"\n{name.title()}'s favorite number is:")
    for number in numbers:
        print(f"-{number}")

# Exercise 6.11: Cities

cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
        },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
        },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
        }
    }

print("\nCities information:")
for city, city_details in cities.items():
    city = city.title()
    country = city_details["country"].title()
    population = city_details["population"]
    nearby_mountains = city_details["nearby mountains"]
    print(f"-{city} is in {country}. It has a population of {population} and"
            f" the {nearby_mountains} mountain nearby.")
