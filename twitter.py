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

import tweepy
import json
from copy import deepcopy

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

def load_tweetlog():
	try:
		with open("tweetlog.json", 'r') as tl:
			tweetlog = json.load(tl)
	except FileNotFoundError:
		tweetlog = []
	return tweetlog

def load_tweetcreds():
	"""
	I'm perfectly happy with this just throwing if there are no 
	twitter creds.  Maybe for next version there can be 
	some kind of functionality to run with a no-twitter mode that 
	just dumps hashes to printable form to disk. 
	"""
	with open("twittercreds.json") as tc:
		creds = json.load(tc)
	return creds

def tweet_new_targets(newlist, tweetfn, tweetlog):
	log = deepcopy(tweetlog)
	for n in newlist:
		tweet = "Watching: " + n["uuid"] + " hash: " + n["hash"] + "."
		response = tweetfn(tweet)
		response["uuid"] = n["uuid"]
		response["hash"] = n["hash"] # just to facilitate searching
		log.append(response)
	return log

def tweet_changed_targets(changed, tweetfn, tweetlog):
	log = deepcopy(tweetlog)
	for c in changed:
		tweet = "CHANGED! " + c["uuid"] + " new hash: " + c["hash"] + "."
		response = tweetfn(tweet)
		response["uuid"] = c["uuid"]
		response["hash"] = c["hash"] # just to facilitate searching
		log.append(response)
	return log

def tweet_all(checked):
	"""
	Steps:
	1.  Load tweetlog and tweet creds
	2.  Generate and log tweets for changed files
	3.  Generate and log tweets for new files
	4.  Save tweetlog 
	"""
	tweetlog = load_tweetlog()
	creds = load_tweetcreds()
	post_tweet = twitter.twitter_poster(creds)
	tweetlog = tweet_new_targets(checked["additions"], post_tweet, tweetlog)
	tweetlog = tweet_changed_targets(checked["changes"], post_tweet, tweetlog)
	with open('tweetlog.json', "w") as tl:
		json.dump(tweetlog, tl, sort_keys = True, indent = 4)

