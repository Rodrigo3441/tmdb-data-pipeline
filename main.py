from src.movies import main_bronze
from src.movies import main_silver
from src.genres import main_bronze as genres_main_bronze
from src.genres import main_silver as genres_main_silver
from src.gold import main_gold
from utils import logging_config
import logging

logger = logging.getLogger()

def main():
    logger.info('Starting the ETL Pipeline')

    logger.info('Executing Bronze Layer')
    # main_bronze.run()
    # genres_main_bronze.run()

    logger.info('Executing Silver Layer')
    # main_silver.run()
    # genres_main_silver.run()

    logger.info('Executing Gold Layer')
    main_gold.run()
   


if __name__ == "__main__":
    main()