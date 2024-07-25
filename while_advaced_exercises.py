#Exercise 7.8 - Deli

sandwich_order = ["tuna", "pastrami", "chicken", "pastrami", "egg", "pastrami", "salmon"]
finished_sandwiches = []

#Exercise 7.9 - No Pastrami
while "pastrami" in sandwich_order:
    sandwich_order.remove("pastrami")

while sandwich_order:
    sandwich = sandwich_order.pop()
    finished_sandwiches.append(sandwich)
    print(f"I made your {sandwich} sandwich.")

print("\nThe following sandwiches were made:")
for finished_sandwich in finished_sandwiches:
    print(f"- {finished_sandwich.title()} sandwich")

#Exercise 7.10 - Dream vacation

poll_results = {}
poll_active = True
number = 0

while poll_active:
    number += 1
    user = "user" + str(number)
    destination = input("\nIf you could visit one place in the world, where"
                        "would you go? ")
    poll_results[user] = destination

    repeat = input("Do you have another user who wnats to answe -  yes/no: ")
    if repeat == "no":
        poll_active = False

print("--The dream destinations are----")
for destination in poll_results.values():
    print(f"- {destination}")


