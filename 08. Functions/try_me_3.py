# 8-6. City Names: Write a function called city_country() that takes in the name of a city and its country. 
# The function should return a string formatted like this: "Santiago, Chile" 
# Call your function with at least three city-country pairs, and print the values that are returned. 
 
def city_country(city, country):
    return f"{city}, {country}"

where_in_the_world = city_country('Melbourne', "Australia")

where_in_the_world_2 = city_country('Christchurch', "New Zealand")

where_in_the_world_3 = city_country('Nandi', "Fiji")

print(where_in_the_world)

print(where_in_the_world_2)

print(where_in_the_world_3)

  
 
 
# 8-7. Album: Write a function called make_album() that builds a dictionary describing a music album. 
# The function should take in an artist name and an album title, and it should return a dictionary containing these two pieces of information. 
# Use the function to make three dictionaries representing different albums. 
# Print each return value to show that the dictionaries are storing the album information correctly. 
# Use None to add an optional parameter to make_album() that allows you to store the number of songs on an album. 
# If the calling line includes a value for the number of songs, add that value to the album’s dictionary. 
# Make at least one new function call that includes the number of songs on an album. 
 


def make_album(artist_name, artist_title, songs = None):
   music_album = {
    'artist': artist_name, 
    'album': artist_title, 
    'number_of_songs':songs
}
#    music_album.update(make_album)

   return music_album


add_album_1 = make_album("John Fogarty", "Old Man Down The Road")

add_album_2 = make_album("Dolly Parton", "9 to 5", '12')

add_album_3 = make_album("KISS", "KISS Alive II")

print(add_album_1)

print(add_album_2)

print(add_album_3)

 

# 8-8. User Albums: Start with your program from Exercise 8-7. 
# Write a while loop that allows users to enter an album’s artist and title. 
# Once you have that information, call make_album() with the user’s input and print the dictionary that’s created. 
# Be sure to include a quit value in the while loop.


def make_album(artist, title, tracks=0):
    """Build a dictionary containing information about an album."""
    album_dict = {
        'artist': artist.title(),
        'title': title.title(),
        }
    if tracks:
        album_dict['tracks'] = tracks
    return album_dict


# Prepare the prompts.
title_prompt = "\nWhat album are you thinking of? "
artist_prompt = "Who's the artist? "

# Let the user know how to quit.
print("Enter 'quit' at any time to stop.")

while True:
    title = input(title_prompt)
    if title == 'quit':
        break
    
    artist = input(artist_prompt)
    if artist == 'quit':
        break

    album = make_album(artist, title)
    print(album)


print("\nThanks for responding!")

