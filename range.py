#for i in range(6):
    #print(i)



squares = []

# Get the list of the first ten numbers
for number in range(1,11):
    squares.append(number**2)

print(squares)

numbers = list(range(1,11))
print(max(numbers))

print(min(numbers))

print(sum( numbers))

#list compressions

new_square = [new_value**2 for new_value in range(1,11)]
print(new_square)


