players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("The first three items in the list are:")
print(players[:3])

print("\nThree items from the middle of the list are:")
print(players[1:4])

print("\nThe last three items of the list are:")
print(players[-3:])

## looping through a slice

print("\nHere are the first three players in my team:")
for player in players[:3]:
    print(player.title())

## Coying lists

my_foods = ['pizza', 'falafel', 'carrot cake']
my_friends_food = my_foods[:]

my_foods.append("cannoli")


print("\nmy favorite food are:")
print(my_foods)

print("\nmy firends favoirte food are:")
print(my_friends_food)


my_pizza = ["cheese", "dragon", "hawaian"]

