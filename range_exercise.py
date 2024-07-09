for number in range(1,21):
    print(number)


million = list(range(1,1000001))
# print(million)
print(f"The min value is: {min(million)}")
print(f"The max value is: {max(million)}")
print(f"The sum of the value is: {sum(million)}")

for odd_number in range(1, 20, 2):
    print(odd_number)

for multiple_of_three in range (3, 30):
    if (multiple_of_three%3) == 0:
        print(f"I am a miltipe of 3: {multiple_of_three}")

cubes = []
for cube_number in range(1,10):
    cube = cube_number ** 3
    cubes.append(cube)
print(cubes)

cubes_updated = [num3 ** 3 for num3 in range(1, 10)]
for cube_updated in cubes_updated:
    print(cube_updated)

