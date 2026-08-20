# TMDB Data Pipeline

An end-to-end data engineering project that extracts movie data from the TMDB API, processes it using a Medallion Architecture, and loads it into SQL Server.

## Overview

This project started as an exercise to practice consuming REST APIs and evolved into a small data engineering pipeline.

The pipeline extracts movie-related data from TMDB and processes it through three layers:

* **Bronze** — raw data extracted from the API
* **Silver** — cleaned and transformed data
* **Gold** — analytics-ready data

## Pipeline

```text
TMDB API
    ↓
Extraction
    ↓
Bronze
    ↓
Silver
    ↓
Gold
```

API data is extracted in batches and progressively loaded into SQL Server rather than keeping the entire dataset in memory.

## Technologies

* Python
* pandas
* Requests
* SQLAlchemy
* SQL Server
* TMDB API

## Current Goals

* Extract paginated movie data from the TMDB API
* Implement batch-based ingestion
* Store raw data in the Bronze layer
* Clean and normalize data in the Silver layer
* Build analytics-ready datasets in the Gold layer
* Handle multiple movie-related resources such as movies and genres

## Project Status

🚧 **In development**

The Bronze ingestion pipeline is currently being implemented. Additional transformations, data modeling, error handling, and pipeline improvements will be added as the project evolves.
