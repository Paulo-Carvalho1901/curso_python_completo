"""
Named and unnamed arguments in Python functions
Named arguments have a name with an equal sign
Unnamed arguments receive only the argument (value)
"""

# function definition
def sum(x, y, z):
    print(f'{x=} {y=} {z=}', '|', 'x + y + z', x + y + z)


# execute the function
sum(1, 2, 3) # unnamed arguments (positional)
sum(y=2, z=3, x=1) # named arguments
sum(1, 2, z=5)