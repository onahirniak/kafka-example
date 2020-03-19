import twitter
import json
import logging

class TwitterAdapter():
    def __init__(self, config):
        self.api = twitter.Api(consumer_key=config.key,
                      consumer_secret=config.secret,
                      access_token_key=config.token_key,
                      access_token_secret=config.token_secret)

        self.config = config

    def get_tweets(self):
        timeline = self.api.GetUserTimeline(screen_name=self.config.target_user)
        return [tweet.text for tweet in timeline]
