import pandas as pd
import ast

def run(df: pd.DataFrame) -> pd.DataFrame:

    # replace null values with 'n/a'
    df['backdrop_path'] = df['backdrop_path'].fillna('n/a')

    # standardization for the language code to uppercase
    df['original_language'] = df['original_language'].apply(str.upper)

    # replace data quality issues with 'n/a'
    df['original_title'] = df['original_title'].case_when(
        caselist=[
            (
                (
                    (df['original_title'].str.startswith('?') &
                    df['original_title'].str.endswith('?')) |
                    (df['original_title'].str.startswith('?')),
                    'n/a'
                )
            )
        ]
    )   
    df['original_title'] = df['original_title'].str.replace('?', '')

    # replace empty strings with 'n/a'
    df['overview'] = df['overview'].apply(str.strip)
    df['overview'] = df['overview'].case_when(
        caselist=[
            (
                (
                    df['overview'].str.len() == 0,
                    'n/a'
                )
            )
        ]
    )

    # replace null values with 'n/a'
    df['poster_path'] = df['poster_path'].case_when(
        caselist=[
            (
                (
                    df['poster_path'].isna(),
                    'n/a'
                )
            )
        ]
    )

    # convert string date values to properly datetime type
    df['release_date'] = pd.to_datetime(df['release_date'], errors='coerce', format='%Y-%m-%d')

    # derives a new dataframe for the movie genres (1:n)
    movie_genres = []

    # iterates through all the movies
    for i in range(0, len(df)):
        genre_ids = df['genre_ids'].iloc[i]

        # convert a literal array string to a list
        genre_ids = ast.literal_eval(genre_ids)

        # for each month, iterates through its genres categories
        for genre_id in genre_ids:
            # append for the same movie all its genres
            movie_genres.append(
                {
                    'movie_id': df['id'].iloc[i],
                    'genre_id': genre_id
                }
            )

    # drop the old genre_ids column
    df = df.drop(columns=['genre_ids'])

    movie_genres = pd.DataFrame(movie_genres)

    return {
        'movies': df,
        'movies_genres': movie_genres
    }