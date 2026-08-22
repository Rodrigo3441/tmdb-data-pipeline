# Bronze Layer — Data Catalog

The Bronze layer contains raw data extracted from the TMDB API. Data in this layer is kept as close as possible to its original source representation, with only minimal transformations required for storage.

## `bronze.movies`

Contains raw movie data extracted from the TMDB API.

| Column              | Data Type | Description                                                         |
| ------------------- | --------- | ------------------------------------------------------------------- |
| `id`                | `BIGINT`  | Unique identifier of the movie provided by TMDB.                    |
| `adult`             | `BIT`     | Indicates whether the movie is classified as adult content.         |
| `backdrop_path`     | `VARCHAR` | Relative path to the movie's backdrop image.                        |
| `genre_ids`         | `VARCHAR` | Raw list of genre identifiers associated with the movie.            |
| `title`             | `VARCHAR` | Display title of the movie.                                         |
| `original_language` | `VARCHAR` | Original language code of the movie.                                |
| `original_title`    | `VARCHAR` | Movie title in its original language.                               |
| `overview`          | `VARCHAR` | Short description or synopsis of the movie.                         |
| `popularity`        | `FLOAT`   | TMDB popularity score for the movie.                                |
| `poster_path`       | `VARCHAR` | Relative path to the movie's poster image.                          |
| `release_date`      | `VARCHAR` | Movie release date as received from the API.                        |
| `softcore`          | `BIT`     | Indicates the softcore classification value returned by the source. |
| `video`             | `BIT`     | Indicates whether a video is associated with the movie record.      |
| `vote_average`      | `FLOAT`   | Average user rating for the movie.                                  |
| `vote_count`        | `BIGINT`  | Number of votes used to calculate the movie's average rating.       |

## `bronze.genres`

Contains the genre reference data extracted from the TMDB API.

| Column | Data Type | Description                                      |
| ------ | --------- | ------------------------------------------------ |
| `id`   | `BIGINT`  | Unique identifier of the genre provided by TMDB. |
| `name` | `VARCHAR` | Name of the movie genre.                         |
