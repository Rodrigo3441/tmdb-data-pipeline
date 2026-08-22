# Silver Layer — Data Catalog

The Silver layer contains cleaned, standardized, and normalized data derived from the Bronze layer.

## `silver.movies`

Contains cleaned and standardized movie information.

| Column              | Data Type       | Description                                                             |
| ------------------- | --------------- | ----------------------------------------------------------------------- |
| `id`                | `BIGINT`        | Unique identifier of the movie provided by TMDB.                        |
| `adult`             | `BIT`           | Indicates whether the movie is classified as adult content.             |
| `backdrop_path`     | `VARCHAR`       | Relative path to the backdrop image; missing values are standardized.   |
| `title`             | `VARCHAR`       | Display title of the movie.                                             |
| `original_language` | `VARCHAR`       | Standardized uppercase code representing the movie's original language. |
| `original_title`    | `VARCHAR`       | Original movie title with identified invalid values cleaned.            |
| `overview`          | `VARCHAR`       | Movie synopsis with empty or missing values standardized.               |
| `popularity`        | `FLOAT`         | TMDB popularity score for the movie.                                    |
| `poster_path`       | `VARCHAR`       | Relative path to the poster image; missing values are standardized.     |
| `release_date`      | `DATETIME` | Movie release date converted to a proper date representation.           |
| `softcore`          | `BIT`           | Indicates the softcore classification value returned by the source.     |
| `video`             | `BIT`           | Indicates whether a video is associated with the movie record.          |
| `vote_average`      | `FLOAT`         | Average user rating for the movie.                                      |
| `vote_count`        | `BIGINT`        | Number of votes used to calculate the movie's average rating.           |

## `silver.movies_genres`

Bridge table representing the relationship between movies and their genres. The raw `genre_ids` list from Bronze is normalized into individual records in this table.

| Column     | Data Type | Description                                        |
| ---------- | --------- | -------------------------------------------------- |
| `movie_id` | `BIGINT`  | Identifier of the movie associated with the genre. |
| `genre_id` | `BIGINT`  | Identifier of a genre associated with the movie.   |

## `silver.genres`

Contains the genre reference data available for use by the normalized movie-genre relationship.

| Column | Data Type | Description                                      |
| ------ | --------- | ------------------------------------------------ |
| `id`   | `BIGINT`  | Unique identifier of the genre provided by TMDB. |
| `name` | `VARCHAR` | Name of the movie genre.                         |
