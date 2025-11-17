# MR 2nd args and kwargs notes

"""def hello(name, age):
    return f"Hello {name}! You are {age}!"

print(hello(19, "treyson"))"""
# positional arguments, *args, keyword arguments, **kwargs
def hello( *names, last):
    for name in names:
        print(f"Hello {name} {last}")

hello( "Alex", "katie", "Andrew", "Vienna", "LaRose", "Tia", "Treyson", "Xavier", "Jake", last = "Larose")
