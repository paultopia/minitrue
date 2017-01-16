"""
Functionality to actually go check hashes and do io on json. 

SPECIFICATION OF JSON FILE:

a list (uh, array) of url dicts (uh, objects), each representing a single url to monitor. Each url has the following fields:

'url': the actual url to monitor,
'name': a name to give to the url. Must be unique.

NOTE: 'name' will be tweeted out, along with a sha256 hash of the file (64 characters), and some spaces so it needs to be short.
Recommended maximum length: 50 characters.

This file will be modified automatically by the program. It can initially be blank and minitrue will help you create one. 

filename: targets.json

"""
import json, hash
from copy import deepcopy


# I'll need a counter for new filenames.
def infinite_range(n):
    while True:
        yield n
        n+= 1

def __check_url(target):
    # get url, check hash vs hash of saved file, and if new set changed bit and add a second version (or an nth version if versions field already exists).  If not new, just return orig with last checked added.
    pass

def __initiate_url(target):
    # get url, save filename, date added, and hash. tweet out the name and hash.
    pass

def load_targets(filename):
    with open(filename) as t:
        targets = json.loads(t.read())

def check_targets(targetlist):
    changelist = []
    for target in targetlist:
        if target["saved"]:
            target = __check_url(target)
            if target["justchanged"]:
                changelist.append(target.deepcopy())
                target["justchanged"] = False
        else:
            target = __initiate_url(target)
    return (targetlist, changelist)
