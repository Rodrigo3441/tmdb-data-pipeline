from src import api_interface as movieApi
import requests
import pandas as pd

def run(page: int) -> requests.Response:
    moviedb = movieApi.TheMovieDatabase() 
    return moviedb.return_movie_page(page)


def return_total_pages() -> int:
    moviedb = movieApi.TheMovieDatabase()
    total_pages = moviedb.return_total_pages()
    return total_pages