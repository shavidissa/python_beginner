# Exercise 7.1: Rental cars

car_type = input("What typy of rental car do you like? ")
print(f"Let me see if I can find you a {car_type}.")

# Exercise 7.2: Restaurant seating

number_of_guests = input("\nHow many people are in your dinner group? ")
number_of_guests = int(number_of_guests)

if number_of_guests <= 8:
    print("Thank you! Your table is ready for you.")
else:
    print("I am sorry! You need to wait till your table is ready.")

# Exercise 7.2: Multiples of 10

user_number = input("\nEnter a number: ")
user_number = int(user_number)

if user_number % 10 == 0:
    print(f"The number {user_number} is a multiple of 10")
else:
    print(f"The number {user_number} is not a multiple of 10")

# Exercise 7.4: Pizza toppings

prompt = "\nEnter a pizza topping: "
prompt += "\n(Enter `quit` to finish your order)"

while True:
    topping = input(prompt)
    if topping == "quit":
        break
    else:
        print(f"Added the topping {topping} to your pizza.")


# Exercise 7.4: Movie tickets

age = input("\nHow old are you? ")
age = int(age)
active = True

while active:
    if age >=3 and age < 12:
        print("\nThe ticket costs 10 dollars.")
        active = False
    elif age > 12:
        print("\nThe ticket costs 15 dollars.")
        active = False
    else:
        print("You enter for free")
        active = False

# Exercise 7.4: Movie tickets - Options 2
print("-----Option 2 --------------")
age = input("\nHow old are you? ")
age = int(age)


while True:
    if age >=3 and age < 12:
        print("\nThe ticket costs 10 dollars.")
        break
    elif age > 12:
        print("\nThe ticket costs 15 dollars.")
        break
    else:
        print("You enter for free")
        break