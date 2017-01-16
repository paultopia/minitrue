import tweepy, json

def twitter_poster(json_creds):
    """Pass me a json file with twitter creds.
    Fields:
    'consumer_key',
    'consumer_secret
    'access_token',
    'access_secret',
    which are all in the order given in the twitter dev page
    (see tutorial: https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app)

    Returns:
    a function to call to post to the given twitter account.

    the function just posts a string and returns a json string of the form:
    {"date": POST DATE STRING IN ISO FORMAT,
    "url": URL TO TWEET,
    "account": TWITTER SCREENNAME,
    "id": TWITTER ID (INT),
    "text": TEXT OF TWEET}
    """
    with open(json_creds) as tj:
        tcreds = json.loads(tj.read())
    auth = tweepy.OAuthHandler(tcreds["consumer_key"], tcreds["consumer_secret"])
    auth.set_access_token(tcreds["access_token"], tcreds["access_secret"])
    twitter = tweepy.API(auth)
    def post_tweet(text):
        sobj = twitter.update_status(text)
        url = "https://twitter.com/" + sobj.user.screen_name + "/status/" + str(sobj.id)
        return json.dumps({"text": sobj.text, "id": sobj.id, "date": sobj.created_at.isoformat(), "account": sobj.user.screen_name, "url": url})
    return post_tweet

# example:
# make_post = twitter_poster("my twitter_creds.json")
# post = make_post("testing, 1 2 3")
# print(post)
