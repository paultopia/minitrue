#!/usr/bin/env python3

import json
try:
	with open('targets.json', 'r') as tf:
		targets = json.load(tf)
except FileNotFoundError:
	targets = []

def format_url(url):
	if url.partition(':')[0] not in ['http', 'https']:
		return 'http://' + url
	return url

addnew = 'y'
while addnew == 'y':
	newurl = format_url(input('URL of new target: ')).strip()
	newname = input('Name of new target: ').strip()
	targets.append({'name': newname, 'url': newurl})
	addnew = input('Would you like to add another URL? (y/n): ').lower()

with open('targets.json', 'w') as tf:
	json.dump(targets, tf, sort_keys = True, indent = 4)
print('Done!')
