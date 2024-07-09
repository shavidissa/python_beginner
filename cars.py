cars = ['bmw', 'audi', 'toyota', 'subaru']
#Changes the order permanently
print(f"This is the original list:\n{cars}")

cars.sort()
print("\nThis is the permanently sorted list:")
print(cars)

cars = ['bmw', 'audi', 'toyota', 'subaru']
print(f"\nThis is temporarily sorted list:\n{sorted(cars)}")
print(f"\nThis is the original list:\n{cars}")

# Sorting with capiutal letter is more complex. Not covered here.

# Reversing the order of a list. This is permanent. But you can use the reverse method again to turn it around.

cars.reverse()
print(f"\ncars in reverse order:\n{cars}")
cars.reverse()
print(f"\nCars back in the original order:\n{cars}")

# Finding the length of a list using len()

print(f"\nThe number of cars in the list: {len(cars)}")
