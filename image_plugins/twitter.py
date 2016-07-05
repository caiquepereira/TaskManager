import tweepy


def get_api(cfg):
    auth = tweepy.OAuthHandler(cfg['consumer_key'], cfg['consumer_secret'])
    auth.set_access_token(cfg['access_token'], cfg['access_token_secret'])
    return tweepy.API(auth)


def main():
    # Fill in the values noted in previous step here
    cfg = {
        "consumer_key": "CQSfwVC8fWrMJY....",
        "consumer_secret": "Nnt2MlnIcL4iwRgrrJWys8p5zNMdH....",
        "access_token": "750323357007155200-m3Gm9ufFxQ...",
        "access_token_secret": "xYDUYUssr3BYxnhARCID1KH4cR..."
    }

    api = get_api(cfg)

    import time
    datetime = time.strftime("%c")
    tweet = datetime
    status = api.update_status(status=tweet)
    # Yes, tweet is called 'status' rather confusing

if __name__ == "__main__":
    main()
