from database import connection
from src.movies.bronze import extract
from src.movies.bronze import transform
from src.movies.bronze import load
import logging
import time

# page limits for the api
MAX_PAGES = 500

def run():

    start_time = time.perf_counter()

    pages_loaded = 0
    pages_failed = 0

    # logging for the bronze layer
    logger = logging.getLogger()

    # the database engine for connection and operations
    engine = connection.get_connection()

    logger.info('Starting loading the data')

    for page in range(1, MAX_PAGES+1):
        data_was_loaded = False

        raw_data = extract.run(page)
        cleaned_data = transform.run(raw_data)
        print(page)
        
        data_was_loaded = load.execute(engine, cleaned_data, 'bronze')

        if (data_was_loaded):
            pages_loaded += 1
            logger.info(f'Loaded page {page} into the database successfully.')
        else:
            pages_failed += 1
            logger.error(f'Failed to load the page {page} into the database')


    logger.info('Movie data loaded into the database successfully.')

    end_time = time.perf_counter()
    total_time = end_time - start_time

    logger.info(f'{'Total Time':.<40} {total_time:.2f} sec')
    logger.info(f'{'Total loaded pages':.<40} {pages_loaded} pages')
    logger.info(f'{'Total failed pages':.<40} {pages_failed} pages')

    
