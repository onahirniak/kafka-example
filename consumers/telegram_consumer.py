from kafka import KafkaConsumer
import json
from telegram_adapter import TelegramAdapter

class TelegramConsumer():
    def __init__(self, config):
        self.consumer = KafkaConsumer(config.kafka.topic,
                        group_id=config.kafka.group,
                        value_deserializer=lambda m: json.loads(m.decode('utf-8')),
                        bootstrap_servers=[config.kafka.endpoint])
        self.adapter = TelegramAdapter(config.telegram)
        self.config = config

    def consume(self):
        for message in self.consumer: 
            self.adapter.send(message.value)


