from dynaconf import settings

class ConsumerConfig(object):
    def __init__(self):
        self.kafka = KafkaConfig()
        self.telegram = TelegramConfig()

class KafkaConfig(object):
    def __init__(self):
        self.topic = settings.KAFKA_TOPIC
        self.endpoint = settings.KAFKA_ENDPOINT
        self.group = settings.KAFKA_GROUP

class TelegramConfig(object):
    def __init__(self):
        self.token = settings.TELEGRAM_BOT_API_KEY
        self.target_chat = settings.TELEGRAM_BOT_TARGET_CHAT