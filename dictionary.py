alien_0 = {"color":"green", "points":5}

new_points = alien_0["points"]

print(f"you earned: {new_points} points")

alien_0["x_position"] = 0
alien_0["y_position"] = 25
print(alien_0)

# Starting with an empty dictionary

alien_1 = {}

alien_1["color"] = "red"
alien_0["points"] = 10
print(alien_1)

# Modify a value in a dictionary

alien_1["color"] = "yellow"
print(f"this alien is now {alien_1['color']}")

# Modifying a dictionary -advanced

alien_0["speed"] = "fast"
print(f"\nThe original position of the alien is: {alien_0['x_position']}")

if alien_0["speed"] == "slow":
    x_increment = 1
if alien_0["speed"] == "medium":
    x_increment = 2
else:
    # The speed is fast here
    x_increment = 3

# The new position of the alien
alien_0["x_position"] = alien_0["x_position"] + x_increment

print(f"The new postion of the aliens is: {alien_0['x_position']}")

# Deleting a value form the alien

print(f"\nbefore deleitn points: \n{alien_0}")
del alien_0["points"]
print(f"after deleting the points: \n{alien_0}")

# Long format of a dictionary

favorite_language = {
    "jen": "python",
    "sarah": "c",
    "edward": "rust",
    "phil": "python",
}

print(f"\nSarah's favorite language is: {favorite_language['sarah'].title()}")

# Using the get method to 

point_value = alien_0.get("points")
print(point_value)