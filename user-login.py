users = ["admin", "kim", "nic", "sam"]

if users:
    for user in users:
        if user == "admin":
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {user}, thank you for logging in again.")
else:
    print("We need to find new users!")


# Exercise 5.10 - Checking username

current_users = ["jim", "kim", "tim", "SAM", "pam"]
new_users = ["steph", "nic", "Sam", "kim", "ned"]

# Convert current user to lower case
current_users_lower = [user.lower() for user in current_users]

# This above is a list comprehension. A much shorter way of writing the 
# following code.

#formatted_current_users = []

#for current_user in current_users:
#    formatted_current_users.append(current_user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"This username {new_user} is already taken. Please enter a new username")
    else:
        print(f"This username {new_user} is available")


# Exercise 5.11 Ordinal numbers

number_list = list(range(1,10))

for number in number_list:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(f"{number}th")

