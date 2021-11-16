import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def loggerTest():
    logger.info('Hi')


if __name__ == '__main__':
    logger.info('hi')
    logger.error('warning')
