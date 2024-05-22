for i in range(1,21):
    print(i)

one_million = list(range(1, 1000001))

print((f"max value is:{max(one_million)}"))
print(f"min value is:{min(one_million)}")
print(f"the sum is:{sum(one_million)}")

# Odd number

odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

# Miltiples of three

multiples_of_threes = []

for number in range(3,31,3):
    multiples_of_threes.append(number)

print(multiples_of_threes)

# Cubes

cubes = []

for cube in range(1, 11):
    cubes.append(cube**3)

print(cubes)

new_cubes = [new_cube**3 for new_cube in range(1, 11)]
print(new_cubes)