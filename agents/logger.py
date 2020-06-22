import logging


FORMAT = '%(asctime)-15s %(message)s'
logging.basicConfig(format=FORMAT, filename='simulation.log', level=logging.INFO)
logger = logging.getLogger()


def message(string):
    logger.info(string)

