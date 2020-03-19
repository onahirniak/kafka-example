import logging
import logging.config

from config import KafkaConfig, ProducerConfig, TwitterConfig
from scheduler import Scheduler
from twitter_producer import TwitterProducer

def main():
    logging.config.fileConfig(fname='../logging.conf', disable_existing_loggers=False)

    logger = logging.getLogger('Producer.Main')

    logger.debug('Starting producer.')

    producer = TwitterProducer(ProducerConfig())

    Scheduler.run(30, producer.produce)

    logger.debug('Shutdown producer.')
    		
main()
