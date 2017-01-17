# minitrue

**Catch Donald Trump Tampering with Public Data** 

Status: alpha, but ready to go.  People to test, and outright use, needed!

![example](screenshot.png?raw=true "example")

## What is it? 

Python scripts to monitor public data and prove that it's been changed.

The idea: suppose Donald Trump goes full 1984 and tampers with government data.  For example, modifying climate data to conceal evidence of human generated climate change. That's bad. Wouldn't you like to catch him? minitrue can help.

minitrue will take a list of URLS that you give it.  Then it will go to those URLs, save their contents to disk, and tweet out a (sha256) hash of the contents. 

Then suppose Trump (or some evil corporation, or whomever's data you want to monitor) changes it.  The next time minitrue runs (you should set it to run every day), it'll see that the hash has changed, and it will tweet out the fact of the change. 

Because you posted the original hash on Twitter, and Twitter maintains a record of dates posted and doesn't allow editing, you can reasonably well prove that the file existed in its original form on the date you originally posted it. Take that evidence, plus the two files, and go wild---media, lawsuits, whatever your little citizen-of-a-goddamn-democracy-no-matter-what-Donald-Trump-thinks heart desires. 

The second nasty trick: the tweets never contain the name or description of the document being monitored. (A unique id is assigned to make it easier to correlate them later.)  So nobody can tell just from reading your Twitter which documents you are monitoring.  

The more people who use it, the more threatening it is: the ultimate idea is to deter document tampering by making it impossible to know which documents are being watched---to create a digital [panopticon](https://www.ucl.ac.uk/Bentham-Project/who/panopticon) to keep Donald Trump/whomever else in line.

## Requirements

- Python 3.5+

- the tweepy library (`pip install tweepy`)

- a twitter account with developer access set up

## How to Use

1.  Clone or download this repo, and put it somewhere where it will be able to run from.

2.  Make addurl.py and minitrue.py executable (`chmod +x`).  Optionally add appropriate shebangs, rename those two files, etc. (don't rename any of the others). 

3.  Run addurl.py to create a list of urls to monitor. 

4.  Store your twitter developer credentials in a file called "twittercreds.json" in the same directory. Format fields are 'consumer_key', 'consumer_secret', 'access_token', and 'access_secret', which are all in the order given in the twitter dev page. Digitalocean has [a helpful tutorial for getting this part set up](https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app).

5.  Set minitrue.py to run at regular intervals (I suggest daily) using a cron job, or launchd on mac.

## Caveats

Twitter is a third party whom I obviously don't control.  They might decide that running this violates their rules, or they might decide to do something crazy like permit editing. Or they might get compromised by the NSA. I recommend periodically taking the data minitrue generates (it's called "target.json") and using other means to prove that it existed in a given form on a given date too. Possibilities include everything from the old-fashioned "put in a securely sealed envelope and mail to yourself to generate a postmark," to sending through other reliable corporate servers (perhaps taking advantage of e-mail timestamping?), to fancy stuff like posting in blockchain transactions. 

I'm not a security person. This is the best I can do, but other ideas for forensic verification of data at URLs would be appreciated.

Right now, no measures are being taken to conceal the fact that requests for URLs are coming from this script.  This should change.

It's probably best to keep this on something that's on a lot---I'm going to be running it from a cheap VPS, personally.

## Future Steps, Help Requests

This should be good to go (by the end of the day, after I do a little testing and squash the inevitable bugs in the two modules I just created from my ipad without running them at all).  But right now you kind of need to be pretty skilled to run it.  So that's top priority to change.  

In rough order of priority, here is what needs to happen next:

1. Setup scripts, or even GUI interface (!??!) and a frozen distributable executable (also proper oauth for twitter), to allow non-technical people to set up.  

2.  Windows compatibility (if it doesn't already exist.  I don't even know.). 

3.  Some attempts to conceal web traffic coming from minitrue. (This could mean anything from user-agent switching, to randomizing request times, to adding noise requests to unmonitored documents, to tor or other ip concealment, to all of the above.)

4.  Additional date verification methods beyond just posting to Twitter (especially blockchain-ey things). 

5. If this gets popular enough to be worthwhile, funding for a hosted platform to set up and run monitors (preferably offshore, like in Switzerland) with a web interface. 

Pull requests are greatly appreciated for these priorities or for anything else that might make this more secure or effective. 
