# original menu tuple
menu = ("Coffee", "Croissants", "Quiche", "Sandwiches", "Muffins")

for food in menu:
    print(f'This is the original cafe menu: {food}')

# we can update the menu items by replacing the original menutuple
menu = ("Coffee", "Croissants", "Quiche", "Sandwiches",
        "Muffins", "Scones", "Cakes", "Pastries")

for food in menu:
    print(f'This is the new cafe menu with new options!: {food}')
