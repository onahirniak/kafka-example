import logging
import logging.config
from scheduler import Scheduler
from twitter_adapter import TwitterAdapter, TwitterConfig

def produce():
	config = TwitterConfig()
	config.key = ""
	config.secret = ""
	config.token_key = ""
	config.token_secret = ""

	twitter = TwitterAdapter(config) 	
	tweets = twitter.get_tweets("S_a_s_h_k_a_");

	print(tweets)

def main():
	logging.config.fileConfig(fname='../logging.conf', disable_existing_loggers=False)

	# Get the logger specified in the file
	logger = logging.getLogger('Producer.Main')

	logging.debug('Starting producer.')

	scheduler = Scheduler()

	scheduler.run(30, produce)

	logging.debug('Shutdown producer.')
    		

main()


