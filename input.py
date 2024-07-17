#prompt = "If you tell us your name we can personalize your meesage."
#prompt += "\nWhat's your name? "

#name = input(prompt)
#print(f"Hello {name.title()}")

# Working with numbers using int()

#age = input("How old are you? ")
#age = int(age)
#print(age >=18)

# Modulo operator
# modulo operator tells you how many times a number fits in another number

modulo_check = 35 % 6
print(modulo_check)

# check if a number given is even or odd.

number = input("Enter a number and we will tell you if it is even or odd: ")
#convert number to an integer because input retunrs a string.
number = int(number)

if number % 2 == 0:
    print(f"The number {number} is even")
elif number % 2 > 0:
    print(f"The number {number} is odd.")