import packages.shopping_cart
# or
from packages.shopping_cart import buy
# to include a package, there must be __init__.py file for python interpreter  to know it's a package
print(packages.shopping_cart.buy('mango'))
print(buy('Watermelon'))