items = ["Orange", "Computer", "Pineapple", "Space", "Helicopter", "Coffee", "Book", "Chair", "Guitar", "Snow", "Bicycle", "Whale", "Piano", "Telescope", "Football", "Microscope", "Kite", "Library", "Restaurant", "Banjo"]
#Sorting a List Permanently with the sort() Method

items.sort()    #sorts a list permanently
print(items)

items.sort(reverse=True)  #sorts a list permanently in reverse
print(items)



car_models = ["Mustang", "Corolla", "F-150", "Civic", "Challenger", "Altima", "Silverado", "Camry", "Accord", "Fusion", "Explorer", "Taurus", "Malibu", "Impala", "Charger", "Sentra", "Focus", "Grand Cherokee", "Wrangler", "Maxima"]

print(car_models)
print(sorted(car_models))   #sorts a list temporarily
print(car_models)

print(sorted(car_models, reverse=True))   #sorts a list temporarily in reverse


#or
reverse_car_sort = sorted(car_models, reverse=True)
print(reverse_car_sort)