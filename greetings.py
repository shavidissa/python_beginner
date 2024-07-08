friends = ["Aksha", "Asma", "Shamara", "Shalom", "Clivanka", "Dilshani"]

print(f"Confrimed attendance: {friends[0]}")
print(f"Confrimed attendance: {friends[1]}")
print(f"Declined attendance: {friends[3]}")
friends[3] = "Anjana"

for friend in friends:
    print(f"New list- confirmed attendance: {friend}")

print("Hi friends, we found a bigger table.")

## Small table again

print("Hi friedns only 2 people can be invited now")

for friend in friends:
    if len(friends) > 1:
        print(len(friends))
        friend_univnited = friends.pop()
        print(f"Hi {friend_univnited}, I am sorry to cancel the invite due to logistic issues.")
        friends.clear()
    else:
        print("Guest list is now" + str(len(friends))+ ".")

for friend in friends:
    print(f"hello {friend} you are invited to the party")


del friends[0]
del friends[0]
del friends[0]
print(friends)
    



