import tweepy


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


def post_tweet(tweet_message):
    # Fill in the values noted in previous step here
    cfg = {
        "consumer_key": "CQ...",
        "consumer_secret":
            "Nn...",
        "access_token": "75...",
        "access_token_secret": "xY..."
    }

    api = get_api(cfg)
    status = api.update_status(status=tweet_message)
