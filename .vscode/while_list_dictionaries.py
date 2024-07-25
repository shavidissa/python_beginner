# Move items from one list to another using the while loop

uncomfirmed_users = ["sarah", "kim", "tim", "tom"]
confirmed_users = []

while uncomfirmed_users:
    user = uncomfirmed_users.pop()
    confirmed_users.append(user)

print(f"\nThe following users are confirmed:")
for confirmed_user in confirmed_users:
    print(confirmed_user.title())


# Remove all instance of a list

pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']
print(pets)

while "cat" in pets:
    pets.remove("cat")

print(pets)

#Filling input values into a dictionary

responses = {}
poling_active = True

while poling_active:

    name = input("What's your name? ")
    response = input("what mountain would you like to climb? ")

    responses[name] = response

    # Checking if someone else wnats to answer
    repeat = input("Would you like to let another person respond? (yes/no)")
    if repeat == "no":
        poling_active = False

print(responses)

# Showing the polling results
print("\n--------------Poll Results------------------")
for name, response in responses.items():
    print(f"{name.title()} wants to climb {response.title()}")
    

