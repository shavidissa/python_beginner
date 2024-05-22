for i in range (6):
    print(i)


even_numbers = list(range(0,6,2))
print(even_numbers)

squares = []
for value in range (1,11):
    squares.append(value**2)

print(squares)


digits = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(min(digits))
print(max(digits))
print(sum(digits))

## List Comprehension

squares_list = [value**2 for value in range(1,11)]
print(squares)