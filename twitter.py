"""
Hyper-simplified functionality to post to twitter (using tweepy library).

Requires json file with twitter creds.
    Fields:
    'consumer_key',
    'consumer_secret
    'access_token',
    'access_secret',
    which are all in the order given in the twitter dev page
    (see tutorial: https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app)

twitter_poster is a factory-type function that spits out a function to post to twitter given by creds and return a dict string with
    Fields:
    "date": POST DATE STRING IN ISO FORMAT,
    "url": URL TO TWEET,
    "account": TWITTER SCREENNAME,
    "id": TWITTER ID (INT),
    "text": TEXT OF TWEET

example:
make_post = twitter_poster("my twitter_creds.json")
post = make_post("testing, 1 2 3")
print(post)

"""

import tweepy, json

def twitter_poster(tcreds):
    """Pass me a dict with twitter creds.

    Returns:
    a function to call to post to the given twitter account and get dict with relevant info

    """
    auth = tweepy.OAuthHandler(tcreds["consumer_key"], tcreds["consumer_secret"])
    auth.set_access_token(tcreds["access_token"], tcreds["access_secret"])
    twitter = tweepy.API(auth)
    print("created credentials")
    def post_tweet(text):
        sobj = twitter.update_status(text)
        print("posted tweet")
        url = "https://twitter.com/" + sobj.user.screen_name + "/status/" + str(sobj.id)
        return {"text": sobj.text, "id": sobj.id, "date": sobj.created_at.isoformat(), "account": sobj.user.screen_name, "url": url}
    return post_tweet

