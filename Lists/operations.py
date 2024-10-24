# ADD, INSERT, DELETE

fav_movies = ['Sandlot', 'The Lego Movie', 'Dune']

print(len(fav_movies)) # finding the length of the list

# ADDING AN ITEM TO THE LIST (APPEND)

fav_movies.append("Iron Man") # This adds the item to the end of the list

print(len(fav_movies))
print(fav_movies)

# ADDING AN ITEM (INSERT)

fav_movies.insert(1, "Spiderman")
print(fav_movies)
 
# REMOVING AN ITEM

del(fav_movies[2])
print(fav_movies)