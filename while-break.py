prompt = "\nPlease enter the name of a city you visited: "
prompt += "\n(Enter `quit` when you are finished.)"

# A loop that start siwth while True runs forever unless it reaches a 
# break statement.
while True:
    city = input(prompt)

    if city == "quit":
        #You can use a brealk anwhere. 
        # Example: for loops that run through a dictionary.
        break
    else:
        print(f"I would love to visit {city.title()}")


# Using the contine loop
# printing only the odd numbers

current_numer = 0
while current_numer < 10:
    current_numer += 1
    if current_numer % 2 == 0:
        continue
    print(current_numer)

