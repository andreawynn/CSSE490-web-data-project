import tweepy

consumerKey = 'jzbDBNIjFjdd6WGuDVqnOzJga'
consumerSecret = 'xea1fCuSMYOXEk96MhFMU3aDac8rkJETBbOtk4tCU8QwHwPRnB'
accessToken = '1246952734185656323-OToMkUAzLLCz1rAjzQth6kJP9k5guY'
accessTokenSecret = '8s65E6nGAB4GHVeEZT7YmRgdQUYpPTtXA7FLXUpcNrQQX'


class TwitterStreamListener(tweepy.streaming.StreamListener):
    ''' Handles data received from the stream. '''

    @staticmethod
    def search_tweets(num_tweets, search_word):
        '''
        Takes in the number of tweets to return and the search word to look for in tweets
        @:returns a list of tuples, with the second element of the tuple being the text of
            the tweet and the first element being a list of all hashtags associated with
            the tweet
        '''
        if search_word[0] != '#':
            search_word = '#' + search_word

        # listener = TwitterStreamListener()
        auth = tweepy.OAuthHandler(consumerKey, consumerSecret)
        auth.set_access_token(accessToken, accessTokenSecret)
        api = tweepy.API(auth, wait_on_rate_limit=True,
                         wait_on_rate_limit_notify=True)

        tweets = tweepy.Cursor(api.search, q=search_word, lang="en", tweet_mode='extended').items(num_tweets)
        tweet_list = [tweet for tweet in tweets]

        # for tweet in tweet_list:
        #     text = ""
        #     try:
        #         text = tweet.retweeted_status.full_text
        #     except AttributeError:  # Not a Retweet
        #         text = tweet.full_text

        return_data = [(tweet.full_text, [hashtag['text'] for hashtag in tweet.entities['hashtags']]) for tweet in tweet_list]

        return return_data
