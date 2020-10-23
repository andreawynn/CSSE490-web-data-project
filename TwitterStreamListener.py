import tweepy

consumerKey = 'jzbDBNIjFjdd6WGuDVqnOzJga'
consumerSecret = 'xea1fCuSMYOXEk96MhFMU3aDac8rkJETBbOtk4tCU8QwHwPRnB'
accessToken = '1246952734185656323-OToMkUAzLLCz1rAjzQth6kJP9k5guY'
accessTokenSecret = '8s65E6nGAB4GHVeEZT7YmRgdQUYpPTtXA7FLXUpcNrQQX'


class TwitterStreamListener(tweepy.streaming.StreamListener):
    ''' Handles data received from the stream. '''

    def on_status(self, tweet):
        # print(status.id)
        print(tweet.user.name)
        print(tweet.text)
        return True

    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True  # To continue listening

    def on_timeout(self):
        print('Timeout...')
        return True  # To continue listening

    def search_tweets(self, tweet_number, tweet_data):
        if tweet_data[0] != '#':
            tweet_data = '#' + tweet_data

        # listener = TwitterStreamListener()
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)

        for tweet in api.search(q=tweet_data, lang="en", rpp=tweet_number):
            print(f"{tweet.user.name}\n{tweet.text}\n\n")