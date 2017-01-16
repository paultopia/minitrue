"""
Core namespace.  Handles: 
1.  Call out to hashio to check hashes, save log, and return results
2.  Load tweetlog and tweet creds
3.  Generate and log tweets for changed files
4.  Generate and log tweets for new files
4.  Save tweetlog 
"""

import hash, hashio, twitter, json
from copy import deepcopy

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
		tweet = "CHANGED! " + n["uuid"] + " new hash: " + n["hash"] + "."
		response = tweetfn(tweet)
		response["uuid"] = n["uuid"]
		response["hash"] = n["hash"] # just to facilitate searching
		log.append(response)
	return log

if __name__ == "__main__":
	checked = hashio.check_from_file("targets.json")
	tweetlog = load_tweetlog()
	creds = load_tweetcreds()
	post_tweet = twitter.twitter_poster(creds)
	tweetlog = tweet_new_targets(checked["additions"], post_tweet, tweetlog)
	tweetlog = tweet_changed_targets(checked["changes"], post_tweet, tweetlog)
	with open('tweetlog.json', "w") as tl:
		json.dump(tweetlog, tl, sort_keys = True, indent = 4)