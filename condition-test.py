car = "Subaru"

if car.lower() == "subaru":
    print("Is car == 'subaru'? I predict True.")

# Using "or" and "in" keywords
if 21 or 19 in range(1,21):
    print("I am 21 or 19!")
else:
    print("21 not in the range.")

# Using "and" and "not in" keywords
if 5 and 6 not in range(1,21):
    print("I am not in the range!")
else:
    print("I am 5 and 6.")


age = 12
if age < 4:
   price = 0
elif age < 18:
    price = 25
elif age <65:
    price = 40
elif age >=65:
    price = 20

print(f"\nyour admission cost is: {price}")

# The else block is a catch all statement. If you have a condition to match
# finish with an elif. This way you know the code runs under the correct 
# conditions.

# If you want to check multiple conditions in the code use if statements for the
# statements.

pizza_toppings = ["extra cheese", "green peppers", "pepperoni"]

for topping in pizza_toppings:
    if topping == "green peppers":
        print("Sorry we are out of green peppers")
    else:
        print(f"Adding you topping: {topping}")\

# Checking if list is empty
# If the name of a list statement is used with an if statement, Python returns 
# true if it has atleast one iteam. If the lsit is empty, Python returns false.

pizza_toppings = []

if pizza_toppings:
    for topping in pizza_toppings:
        print(f"\nAdding your topping: {topping}")
else:
    print("\nDo you want a plain pizza?")