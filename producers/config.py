from dynaconf import settings

class ProducerConfig(object):
    def __init__(self):
        self.kafka = KafkaConfig()
        self.twitter = TwitterConfig()

class TwitterConfig(object):
    def __init__(self):
        self.key = settings.TWITTER_KEY
        self.secret = settings.TWITTER_SECRET
        self.token_key = settings.TWITTER_TOKEN_KEY
        self.token_secret = settings.TWITTER_TOKEN_SECRET
        self.target_user = settings.TWITTER_TARGET_USER

class KafkaConfig(object):
    def __init__(self):
        self.topic = settings.KAFKA_TOPIC
        self.endpoint = settings.KAFKA_ENDPOINT