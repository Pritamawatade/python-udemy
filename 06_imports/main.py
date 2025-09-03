# one way of importing
import recipe.flavors  # all import

print(recipe.flavors.demo_chai())
print(recipe.flavors.ginger_chai())

from recipe.flavors import demo_chai, ginger_chai # named import
from recipe.flavors import * # importing all methods, YOU SHOULD AVOID IT.

print(ginger_chai())
print(demo_chai())


# relative import

from .recipe.flavors import demo_chai # you should avoide it
# from ..05_function. use double .. to go one directory back 