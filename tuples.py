# a list that cannot change or an immutable list is called a tuple
# Just like a list but you use parantheses ().

dimensions = (200, 50)
print(dimensions[0])
print(dimensions[1])

# Tuples are dfined using the trailing comma (,). 
# If you only hav one element in the tuple, make sure to add a comma after that 
# value to say that it is a tuple.

# Looping through the values in a tuple
print("\nOrginal dimensions")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nNew dimensions")
for dimension in dimensions:
    print(dimension)
