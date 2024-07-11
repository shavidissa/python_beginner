alien_color = "green"

# The statement whcih pass
if alien_color == "green":
    print("You just earned 5 points!")

# The statement which fails
if alien_color == "red":
    print("this is a red alien")

# For the if block to run
if alien_color == "green":
    print("if block - You earned 5 piints!")
else:
    print("else block - You earned 10 points!")

# for the else bock to run
if alien_color == "red":
    print("if block - You earned 5 piints!")
else:
    print("else block - You earned 10 points!")

# if-elif-else block - version 1

if alien_color == "green":
    print("if green block - You earned 5 piints!")
elif alien_color == "red":
    print("elif red block - You earned 10 points!")
elif alien_color == "yellow":
     print("elif  yellow block - You earned 15 points!")

# if-elif-else block - version 2 

alien_color = "red"

if alien_color == "green":
    print("if green block - You earned 5 piints!")
elif alien_color == "red":
    print("elif red block - You earned 10 points!")
elif alien_color == "yellow":
     print("elif  yellow block - You earned 15 points!")

# if-elif-else block - version 3 

alien_color = "yellow"

if alien_color == "green":
    print("if green block - You earned 5 piints!")
elif alien_color == "red":
    print("elif red block - You earned 10 points!")
elif alien_color == "yellow":
     print("elif yellow block - You earned 15 points!")

# Stages of life

age = 30

if age < 2:
    print("You are a baby")
elif age < 4:
    print("You are a toddler")
elif age < 13:
    print("You are a kid")
elif age < 20:
    print("You are a teenager")
elif age < 65:
    print("You are an adult")
elif age >=65:
    print("You are a wise being")

# Favorite fruits 

favorite_fruits = ["guava", "durian", "mangusteen", "rambutan", "mango"]

if "guava" in favorite_fruits:
    print("I love guava")
if "durian" in favorite_fruits:
    print("I love durian")
if "mangusteen" in favorite_fruits:
    print("I love mangusteen")
if "rambutan" and "raspberry" in favorite_fruits:
    print("I love fruits that start with r")
if "mango" or "mangusteen" in favorite_fruits:
    print("I love fruits that start with m")