"""
Named and unnamed arguments in Python functions
Named arguments have a name with an equal sign
Unnamed arguments receive only the argument (value)
"""

# function definition
def sum(x, y):
    print(f'{x=} {y=}', '|', 'x + y', x + y)


# execute the function
sum(1, 2)
sum(y=2, x=1)
