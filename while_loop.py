current_number = 1
while current_number <= 5:
    print(current_number)
    current_number += 1


prompt = "\nEnter a message here and I will repeat it."
prompt += "\nEnter `quit` to end the program."

# Adding a flad to check if all the conditions are true before moving to the 
# while loop.

active = True

while active:
    message = input(prompt)
    if message == "quit":
        active =  False
    else:
        print(message)