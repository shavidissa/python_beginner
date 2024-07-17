# Exercise 7.1: Rental cars

car_type = input("What typy of rental car do you like? ")
print(f"Let me see if I can find you a {car_type}.")

# Exercise 7.2: Restaurant seating

number_of_guests = input("\nHow many people are in your dinner group? ")
number_of_guests = int(number_of_guests)

if number_of_guests < 8:
    print("Thank you! Your table is ready for you.")
else:
    print("I am sorry! You need to wait till your table is ready.")

# Exercise 7.2: Restaurant seating

user_number = input("\nEnter a number: ")
user_number = int(user_number)

if user_number % 10 == 0:
    print(f"The number {user_number} is a multiple of 10")
else:
    print(f"The number {user_number} is nota multiple of 10")