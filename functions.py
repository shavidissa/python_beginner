#Functions are written to perform a particular task. 
# You can keep calling the funtion without writing the code over and over again.

def greet_users():
    # A docstring explains what the function does.
    """Display a simple message"""
    print("hello")


greet_users()

# Advanced funtion where you need to pass a value when calling the function.

def greet_usersname(username):
    """Display a simple message"""
    print(f"\nHello {username.title()}")

greet_usersname("jesse")