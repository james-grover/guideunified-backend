import os
import guidebox

os.environ.get('PORT','8080')
os.environ.get('IP','0.0.0.0')

guidebox.api_key = "b1ec95c5594c7d0ac4dc871755150a46e6bc54b4"
movies = guidebox.Movie.list()
print (movies)