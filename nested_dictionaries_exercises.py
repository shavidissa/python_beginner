
# Exercixe 6.7: People
people = {
    "nic345": {
        "first_name": "nic",
        "last_name": "nevin",
        "age": 32,
        "city": "boston",
    },
    "joshturner": {
        "first_name": "josh",
        "last_name": "turner",
        "age": 60,
        "city": "amsterdam",
    },
    "sarahnewmon": {
        "first_name": "srah",
        "last_name": "ashley",
        "age": 19,
        "city": "virginia",
    },
}

for person, person_details in people.items():
    print(f"\nHello {person}")
    print(f"- Full name: {person_details["first_name"].title()}" 
            f"{person_details["last_name"].title()}")
    print(f"- Age: {person_details["age"]}")
    print(f"- City: {person_details["city"].title()}")
