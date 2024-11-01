def make_shirt(size = "large", message = "I love Python"):
    """Display the information"""
    print(f"The {size} shirt size has the following message: {message}")


make_shirt("medium")
make_shirt()
make_shirt("small", "Aloha")

def describe_cities(city, country = "Sri Lanka"):
    """Add function code"""
    print(f"{city.title()} is in {country.title()}")

describe_cities("colombo")
describe_cities("San Diego", "USA")
describe_cities("Galle")


def city_country(city, country):
    return_value = f"{city.title()}, {country.title()}"
    return return_value

while True:

    print("\nPlease type city and country:")
    print("(enter 'q' at any time to quit)")

    city_name = input("Enter city")
    if city_name == "q":
        break

    country_name = input("Enter country name")
    if country_name == "q":
        break
    
    answer = city_country(city_name, country_name)
    print(answer)



