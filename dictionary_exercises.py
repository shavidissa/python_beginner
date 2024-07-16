# Exercise 6.1: Person

person = {
    "first_name": "nic",
    "last_name": "nevin",
    "age": 32,
    "city": "boston",
}

print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

#Exercise 6.2: Favorite number

favorite_numers = {
    "jim": 5,
    "kim": 17,
    "ted": 1000000,
}

for person in favorite_numers:
    print(f"{person}'s favorite number is {favorite_numers.get(person, "no such person")} ")

# Excercise 6.3  :Glossary

shavi_dictionary = {
    "else": "The else block is a catch all statement. If you have a condition" 
            + "to match, finish with an elif. This way you know the code runs" 
            + " under the correct conditions.",
    "tuples": "A list that cannot change or an immutable list is called a tuple."
                + "Just like a list but you use parantheses ().Tuples are defined"
                + "using the trailing comma (,). If you only have one element" 
                + "in the tuple, make sure to add a comma after that value to"
                + "say that it is a tuple.",
    "sort method": "Looping through a disctionars in a particaulr order using"
                    + "the sort method."
}

for word in shavi_dictionary:
    print(f"\n{word}: \n{shavi_dictionary[word]}\n")

# Exercise 6.4: Glossary 2
# Looping through a dictionary.
# The item mthod get the key value pairs in a dictionary.

print("Lopping through a dictionary.\n")
for word, meaning in shavi_dictionary.items():
    print(f"\n{word}:")
    print(f"{meaning}")

# Execersice 6.5: Rivers

rivers = {
    "niles": "egypt",
    "mahaweli": "sri lanka",
    "amazon river": "south america",
}

for river, country in rivers.items():
    print(f"The {river.title()} flows through {country.title()}.")

print("\nPrinte each river alphabetically")
for river in sorted(rivers.keys()):
    print(river.title())

print("\nCountries that have rivers")
for country in set(rivers.values()):
    print(country.title())

# Exercise 6.6: Polling

favorite_language = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

people_to_take_the_poll = ["shavi", "dom", "edward", "phil"]

for person in favorite_language.keys():
    print(f"Hi {person},")

    if person in people_to_take_the_poll:
        print("Thank you for taking the poll!")
    else:
        print("Please take the poll!")




