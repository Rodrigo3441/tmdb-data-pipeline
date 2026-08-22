from src import api_interface as movieApi
import requests

def run(page: int) -> requests.Response:
    moviedb = movieApi.TheMovieDB_movies() 
    return moviedb.return_movie_page(page)