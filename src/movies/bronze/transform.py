import requests
import pandas as pd

def run(raw_data: requests.Response) -> dict:
    cleaned_data = raw_data.json()

    # keep only the result columns for the dataframe
    cleaned_data = pd.json_normalize(cleaned_data, record_path=['results'])

    # formats the genre_ids object to string
    cleaned_data['genre_ids'] = cleaned_data['genre_ids'].astype('str')

    return {
        'movies': cleaned_data
    }