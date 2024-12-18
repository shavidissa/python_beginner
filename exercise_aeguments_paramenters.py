# Exercise 1
def display_message():
    message = "Hello this function prints a message"
    print(message)

display_message()

# Exercise 2
def favorite_book(title):
    print(f"One of my favorite books is {title.title()}.")

favorite_book("Alice in Wonderland")

# Exercise 3

def make_shirt(size, print_message):
    """Display information about the shirt"""
    print(f"\nYour ordered a {size} shirt, and it has the message" 
          + f" {print_message}")

make_shirt("medium", "I want to become a small")
make_shirt(size="large", print_message="Buhahaha")

# Exercise 4

def make_shirt(print_message="I love Python", size="Large"):
    """Display information about the shirt"""
    print(f"\nYour ordered a {size} shirt, and it has the message" 
          + f" {print_message}")
    
make_shirt()
make_shirt(size="medium")
make_shirt("Anything you said", "small")

# Exercise 5

def describe_city(name, country="Sri Lanka"):
    """Display information about the city"""
    print(f"{name.title()} is in {country.title()}")

describe_city("seattle", "USA")
describe_city("Colombo")
describe_city("GALLE")

# Exercise 6

def city_country(city, country):
    "Display the information"
    return f"{city.title()}, {country.title()}"
    


print("\nExercise 6")
answer = city_country("colombo", "Sri Lanka")
print(answer)

answer = city_country("seattle", "USA")
print(answer)

answer = city_country("sydney", "Australia")
print(answer)

# Exercise 7 and 8

def make_album(artist_name, album_title, no_of_songs = None):
    "Display the information"
    
    music_album_dict = {
        "artist": artist_name.title(), 
        "album": album_title.title()
        }

    if no_of_songs:
        music_album["tracks"] = no_of_songs
    return music_album

while True:
    artist = input("Enter the artist's name. \n Print q to quit: ")
    if artist == "q":
        break
    
    album_name = input("Enter the title of the album. \n Print q to quit: ")
    if album_name == "q":
        break
        
    
    album = make_album(artist, album_name)

#album = make_album("sabrina", "please please")
#print(album)

#album = make_album("Komaliye", "BnS", 34)
#print(album)

#album = make_album("Kelle", "Yohani")
print(album)
