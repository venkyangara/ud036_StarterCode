#!/usr/bin/python
import fresh_tomatoes
import media

# An object for Avatar movie
avatar = media.Movie(
    'Avatar',
    """A man strives to become one the alien species,
    with it he face\'s major crisis""",
    'https://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg',
    'https://www.youtube.com/watch?v=5PSNL1qE6VY'
)

# An object for Avengers movie
avengers = media.Movie(
    'Avengers: Infinity Wars',
    'Avenger\'s now face the mighty thanos',
    'https://upload.wikimedia.org/wikipedia/en/f/f9/TheAvengers2012Poster.jpg',
    'https://www.youtube.com/watch?v=QwievZ1Tx-8'
)

# An object for Avaitor movie
avaitor = media.Movie(
    'The Aviator',
    """Based on the 1993 non-fiction book Howard Hughes:
     The Secret Life by Charles Higham""",
    'https://images-na.ssl-images-amazon.com/images/I/41ls3VZ1vyL.jpg',
    'https://www.youtube.com/watch?v=FebPJlmgldE'
)

# An object for Incredebels movie
incredebels = media.Movie(
    'Incredibles 2',
    'Hero are illegal, and when Incredebels fight back to change the opnion.',
    'https://upload.wikimedia.org/wikipedia/en/2/27/The_Incredibles_2.jpg',
    'https://www.youtube.com/watch?v=i5qOzqD9Rms'
)

# An object for Shutter Island movie
shutter_island = media.Movie(
    'Shutter Island',
    'Two us marshals go to investigate a missing patient from an aslyum',
    'https://upload.wikimedia.org/wikipedia/en/7/76/Shutterislandposter.jpg',
    'https://www.youtube.com/watch?v=5iaYLCiq5RM'
)

# An object for The Great Gatsby movie
great_gatsby = media.Movie(
    'The Great Gatsby',
    'A war vetran becomes friends with millionair Gatsby',
    'https://images-na.ssl-images-amazon.com/images/I/51RQEOe3IVL.jpg',
    'https://www.youtube.com/watch?v=rARN6agiW7o'
)

# Creating a list with all the movie objects.
movies = [avatar, avengers, avaitor, incredebels, shutter_island, great_gatsby]
# Let's now call open movies page that spits a html page with the movies list.
fresh_tomatoes.open_movies_page(movies)
