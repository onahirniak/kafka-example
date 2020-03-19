import telegram

import logging
class TelegramAdapter():
    def __init__(self, config):
        self.bot = telegram.Bot(config.token)
        self.config = config
        self.logger = logging.getLogger("TelegramAdapter")

    def send(self, message):
        try:
            self.bot.send_message(self.config.target_chat, message)
        except:
            self.logger.error('Error during send message')
        