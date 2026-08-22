from src.gold import extract
from src.gold import transform
from src import load
from database import connection
import logging
import time

def run():

    start_time = time.perf_counter()
    
    # logging for the bronze layer
    logger = logging.getLogger()

    # the database engine for connection and operations
    engine = connection.get_connection()

    logger.info('Starting loading the gold data')
    silver_data = extract.execute(engine, 'silver')
    gold_data = transform.run(silver_data)
    data_was_loaded = load.execute(engine, gold_data, 'gold')

    if data_was_loaded:
        logger.info(f'Loaded gold data into the database successfully.')
    else:
        logger.error(f'Failed to load the gold data into the database')

    end_time = time.perf_counter()
    total_time = end_time - start_time

    logger.info(f'{'Total Time':.<40} {total_time:.2f} sec')
    
