import twitter

# initialize the api
api = twitter.Api(consumer_key=CONSUMER_KEY,
                    consumer_secret=CONSUMER_SECRET,
                    access_token_key=ACCESS_TOKEN_KEY,
                    access_token_secret=ACCESS_TOKEN_SECRET,
                    tweet_mode='extended') # get the full 280 char tweet

# return the text of the last tweet from a given account
def last_tweet(user):
    t = api.GetUserTimeline(screen_name=user, count=1)
    tweet = t[0].AsDict()
    return tweet['full_text']

# posts a message to the account associated with the API key
def post_tweet(msg):
    api.PostUpdate(msg)
