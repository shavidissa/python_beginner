locations = ["switzerland", "italy", "hawaii", "sri lanka", "japan"]
print(f"This are the palces I like to visit:\n{locations}")

print(f"\nThis is temp sorted list of places:\n{sorted(locations)}")

print(f"\nThis is the 0riginal order of the list:\n{locations}")

print(f"\nThis is the temp list in reverse order:\n{sorted(locations, reverse=True)}")

locations.reverse()
print(f"\n The reverse order of the list:\n{locations}")

locations.reverse()
print(f"\n Back to the original order of the list:\n{locations}")

locations.sort()
print(f"\n Permanently sort list alphabetically:\n{locations}")

locations.sort(reverse=True)
print(f"\n Permanently sort list in reverse-alphabetical order:\n{locations}")