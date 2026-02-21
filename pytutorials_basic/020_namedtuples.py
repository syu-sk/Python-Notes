from collections import namedtuple
#namedtuples are lightweight objects (just like regular tuples) but are more readable

colours = (400, 450, 500, 570, 600, 700)
#anyone looking at the code would not know the significance of the numbers
#of course, there are ways to circumvent this via dictionaries etc. but what if there was a reason that tuples must be used (eg. for its immutability)

'''Making namedtuples'''

Colour = namedtuple('Colour', ['violet', 'blue', 'green', 'yellow', 'orange', 'red'])
#syntax: variable = namedtuple(name, [named values])

rainbow_colours = Colour(400, 450, 500, 570, 600, 700)

print (rainbow_colours[0])
print (rainbow_colours.violet)
#adds functionality to tuples, allowing one to assign values a name. makes it clearer for other viewers
#notice its similarity to classes? maybe namedtuples are a way to create a class without much functionality when needed