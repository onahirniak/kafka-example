import json

from kafka import KafkaProducer
from kafka.errors import KafkaError

from twitter_adapter import TwitterAdapter

class TwitterProducer():
	def __init__(self, config):		
		self.producer = KafkaProducer(
			value_serializer=lambda m: json.dumps(m).encode('utf-8'),
			bootstrap_servers=[config.kafka.endpoint])
		self.adapter = TwitterAdapter(config.twitter) 	
		self.config = config

	def produce(self):
		tweets = self.adapter.get_tweets()

		for tweet in tweets: 
			self.producer.send(self.config.kafka.topic, tweet)