from src import api_interface as movieApi
import requests

def run() -> requests.Response:
    moviedb = movieApi.TheMovieDB_genres() 
    return moviedb.return_genre_data()