
# Decorator: A function that wraps another function to extend 
# its behavior without modifying the original function's source code

def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("*You add sprinkles 🎊*")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("*You add fudge 🍮*")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

while True: # True = keep asking until the user behaves
    flavor_input = input("Which flavor do u wanna have?: ")

    if not flavor_input.isdigit():
        get_ice_cream(flavor_input)
    else:
        print("Is that really a flavor?")