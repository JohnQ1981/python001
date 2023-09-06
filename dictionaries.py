# Dictionaries are basically Key-Valued Pairs where list consist of Index Value Pairs
movie = {
    "title": "Rock",
    "reviews": 10526,
    "imdb" : 8.5,
    'runtime' : '3h',
    'year' : 2001,
    'rating' : 'R'
 }

print(movie['title'])
print("*"*40)
#print(movie.get(1,2))
print(type(movie))
for c in movie:
    print(f"{c} -- {movie[c]} ")
print("*"*40)
stuff = {True: "LOL", 45: "Hello"}
print(stuff[45])
print(stuff[True])

stuff[True] = 'HAHA'
print(stuff[True])

stuff['rating'] = "PG"
#stuff['rating'] = "PG" keys must be unique within dictionary

print(stuff)