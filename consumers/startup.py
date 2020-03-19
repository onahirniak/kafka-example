import logging
import logging.config

from telegram_consumer import TelegramConsumer
from config import ConsumerConfig

def main():
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

    logger = logging.getLogger('TelegramConsumer.Main')
    
    logger.debug('Starting consumer.')

    consumer = TelegramConsumer(ConsumerConfig())

    consumer.consume();
    
    logger.debug('Shutdown consumer.')

main()