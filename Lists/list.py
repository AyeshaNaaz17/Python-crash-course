# list
mixed_list = ['notebooks', 'toys', 4, True]

# List slicing
amazon_cart = ['notebooks', 'toys', 'sunglasses', 'grapes']

amazon_cart[0] = 'laptop'
new_cart = amazon_cart[:] # copying the list
# new_cart = amazon_cart (equating the amazon_cart's list, changes made in any of them will affect both the list)
new_cart[0] = 'gum'
print(new_cart)
print(amazon_cart)