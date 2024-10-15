# Store the locations in a list.  Make sure the list is not in alphabetical order
places = ["Paris, France", "Tokyo, Japan", "New York City, USA", "Rio de Janeiro, Brazil", "Cape Town, South Africa"]

#Print your list in its original order. Don’t worry about printing the list neatly; just print it as a raw Python list
print(places)

#Use sorted() to print your list in alphabetical order without modifying the actual list
print(sorted(places))

#Show that your list is still in its original order by printing it
print(places)

#Use sorted() to print your list in reverse-alphabetical order without changing the order of the original list
print(sorted(places, reverse=True))

#Show that your list is still in its original order by printing it again
print(places)

#Use sort() to change your list so it’s stored in alphabetical order
places.sort()

# Print the list to show that its order has been changed
print(places)

#Use sort() to change your list so it’s stored in reverse-alphabetical order
places.sort(reverse=True)
#Print the list to show that its order has changed
print(places)

print(len(places))

# creating an index error
print(places[4])    #this is a valid index

#
places.remove("Paris, France")  # removing a record is going to shrink the index by 1
print(places[4])    # this is no longer a valid index and will throw a "list out of range" error