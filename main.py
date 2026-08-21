from src.movies import main_bronze
from utils import logging_config
import logging

logger = logging.getLogger()

def main():
    logger.info('Starting the ETL Pipeline')

    logger.info('Executing Bronze Layer')
    # main_bronze.run()
   


if __name__ == "__main__":
    main()