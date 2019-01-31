import twitter
import json
import logging

def log(func):
    def wrapper(*args, **kwargs):
        func_str = func.__name__
        args_str = ', '.join(args)
        
        logger = logging.getLogger(func_str);
        logger.info(func_str)
        
        return func(*args, **kwargs)
    return wrapper

class TwitterConfig():
    pass

class TwitterAdapter():
    def __init__(self, config):
        self.api = twitter.Api(consumer_key=config.key,
                      consumer_secret=config.secret,
                      access_token_key=config.token_key,
                      access_token_secret=config.token_secret)

        self.logger = logging.getLogger("TwitterAdapter")

    @log
    def get_tweets(self, user_id):
        timeline = self.api.GetUserTimeline(user_id)
        self.logger.debug("Request")
        return timeline
