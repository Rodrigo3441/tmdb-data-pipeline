from database import connection
from src.genres.bronze import extract
from src.genres.bronze import transform
from src import load
import logging
import time

def run():

    start_time = time.perf_counter()

    # logging for the bronze layer
    logger = logging.getLogger()

    # the database engine for connection and operations
    engine = connection.get_connection()

    logger.info('Starting loading the genres data')

    raw_data = extract.run()
    cleaned_data = transform.run(raw_data)
    data_was_loaded = load.execute(engine, cleaned_data, 'bronze')

    if data_was_loaded:
        logger.info(f'Loaded genres data into the database successfully.')
    else:
        logger.error(f'Failed to load the genres data into the database')

    end_time = time.perf_counter()
    total_time = end_time - start_time

    logger.info(f'{'Total Time':.<40} {total_time:.2f} sec')

    
