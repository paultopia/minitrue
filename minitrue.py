#!/usr/bin/env python3

import hashio
from twitter import tweet_all
from hasharchive import hx_all

if __name__ == "__main__":
	checked = hashio.check_from_file("targets.json")
	tweet_all(checked)
	hx_all(checked["targets"])

