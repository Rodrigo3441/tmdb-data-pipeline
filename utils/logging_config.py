import logging

# logging configuration
logging.basicConfig(
        filename='logs/pipeline.log', 
        level=logging.INFO,
        format='%(asctime)s | %(levelname)-8s | %(message)-50s | %(filename)s:%(lineno)d',
        datefmt='%Y-%m-%d %H:%M:%S'
)