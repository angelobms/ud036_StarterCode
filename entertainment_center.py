# -*- coding: utf-8 -*-
import fresh_tomatoes
import media
import requests
import json

# OMBb API Key
key = 'OMBD_API_KEY'

movies = []
movie_favories = [
    ['Iron Man', 'byQpcN78UjQ'],
    ['The Incredible Hulk', 'xbqNb2PFKKA'],
    ['Iron Man 2', 'oOzuBOefL8I'],
    ['Thor', 'JOddp-nlNvQ'],
    ['Captain America: The First Avenger', '6y3oHJnfnjU'],
    ['The Avengers', 'eOrNdBpGMv8'],
    ['Iron Man 3', 'f_h95mEd4TI'],
    ['Thor: The Dark World', 'npvJ9FTgZbM'],
    ['Captain America: The Winter Soldier', 'tbayiPxkUMM'],
    ['Guardians of the Galaxy', 'd96cjJhvlMA'],
    ['Avengers: Age of Ultron', 'tmeOjFno6Do'],
    ['Ant-Man', 'QfOZWGLT1JM'],
    ['Captain America: Civil War', 'dKrVegVI0Us'],
    ['Doctor Strange', 'HSzx-zryEgM'],
    ['Guardians of the Galaxy Vol. 2', 'dW1BIid8Osg'],
    ['Spider-Man: Homecoming', 'U0D3AOldjMU'],
    ['Black Panther', 'xjDjIWPwcPU'],
    ['Avengers: Infinity War', '6ZfuNTqbHE8&t=7s'],
    ['Ant-Man and the Wasp', 'UUkn-enk2RU']
    ]

# Scrolls through the list of favorite videos
for i in range(len(movie_favories)):
    try:
        # Aassigns the variable req data of obtained film through OMDb API
        req = requests.get('http://www.omdbapi.com/?t=' +
                           movie_favories[i][0] + '&type=movie&apikey=' + key)

        # Decoding JSON
        resp = json.loads(req.text)

        # Instance of Movie class
        movie = media.Movie(
            resp['Title'],
            resp['Runtime'],
            resp['Plot'],
            resp['Year'],
            resp['Director'],
            resp['Genre'],
            resp['Rated'],
            resp['Poster'],
            "https://www.youtube.com/watch?v=" + movie_favories[i][1]
            )

        # Adds the movie in the movie list
        movies.append(movie)
    except Exception as e:
        print('connection error', e)

fresh_tomatoes.open_movies_page(movies)
