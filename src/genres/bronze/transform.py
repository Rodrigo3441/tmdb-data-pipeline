import pandas as pd
import requests

def run(raw_data: requests.Response) -> dict:
    raw_data = raw_data.json()
    raw_data = pd.json_normalize(raw_data, record_path='genres')

    return {
        'genres': raw_data
    }