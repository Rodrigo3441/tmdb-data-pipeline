from database import connection
from src import silver_extract
from src.movies.silver import transform
from src import load
import logging
import time

def run():
    start_time = time.perf_counter()

    # logging for the silver layer
    logger = logging.getLogger()

    # the database engine for connection and operations
    engine = connection.get_connection()

    logger.info('Starting loading the data')

    logger.info('Extracting the bronze data')
    bronze_data = silver_extract.execute(engine, 'bronze', 'movies')

    logger.info('Transforming the bronze data')
    silver_data = transform.run(bronze_data['movies'])

    logger.info('Loading the silver data into the database')
    data_was_loaded = load.execute(engine, silver_data, 'silver')

    if data_was_loaded:
        logger.info('Movie and Movie Genres data loaded into the silver layer successfully.')
        
    else:
        logger.error('Failed to load the data into the database')

    end_time = time.perf_counter()
    total_time = end_time - start_time

    logger.info(f'{'Total Time':.<40} {total_time:.2f} sec')
