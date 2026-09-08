# def display_name(*args):
#    for arg in args:
#       print(arg, end=" ")

# display_name("Dr.", "Spongebob", "Harold", "Squarepants", "III")

def print_address(**kwargs):
    for key, value in kwargs.items(): # keys or values or items(for both) + ()
        print(f"{key}: {value}")


print_address(street="228 Fake St.",
              city="New Delhi",
              state="Tree",
              zip="733773")