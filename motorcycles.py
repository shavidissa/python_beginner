motorcycles = ['honda', 'yamaha', 'suzuki']
print(motorcycles)

motorcycles[0] = 'ducati'
print(motorcycles)

motorcycles.append("honda")
print(motorcycles)

motorcycles.insert(0, "harley-davidson")
print(f"inserted list: {motorcycles}")

del motorcycles[0]
print(motorcycles)


# Remove a value from a list but doesn not delve the value entirely. So you can keep using the value.

last_owned = motorcycles.pop()
print(motorcycles)
print(f"The last motorcycle I owned is a: {last_owned}")
motorcycles.append(last_owned)

#Use pop with an index
second_bike = motorcycles.pop(1)
print(f"The second bike I oned was a: {second_bike}")
print(motorcycles)
motorcycles.append(second_bike)


# Removing items: if you only know the value in a list. The remove method deletes only the first occurance of the value from a list
motorcycles.remove("ducati")
print(motorcycles)
