"""
Functionality to actually go check hashes and do io on json. 

SPECIFICATION OF JSON FILE:

a list (uh, array) of url dicts (uh, objects), each representing a single url to monitor. Each url has the following fields:

'url': the actual url to monitor,
'name': a name to give to the url. Must be unique.

NOTE: 'name' will be tweeted out, along with a sha256 hash of the file (64 characters), and some spaces so it needs to be short.
Maximum length: 40 characters.

This file will be modified automatically by the program. It can initially be blank and minitrue will help you create one. 

filename: targets.json

"""
import json, hash
from copy import deepcopy

# instead of weird counter architecture, each json just needs a version field that will be added to.

def __exten(url):
    return url.rpartition(".")[2]

def __filename(exten, name, version_number):
    if exten in ["html", "htm", "json", "csv", "txt"]:
        return ''.join(name.split()) + str(version_number) + "." + exten + ".bin"  # identify text files that get binary-ified.
    else:
        return ''.join(name.split()) + str(version_number) + "." + exten


def __check_url(target):
    # get url, check hash vs hash of saved file, and if new set changed bit and add a second version (or an nth version if versions field already exists).  If not new, just return orig with last checked added.
    pass

def __initiate_url(target):
    url = target["url"]
    name = target["name"]
    exten = __exten(url)
    version = 1
    filename = __filename(exten, name, 1)
    hash.fetch_and_save(url, filename)
    h = hash.hashfile(filename)
    if exten in ["html", "htm", "json", "csv", "txt"]:
        text = True
    else:
        text = False
    return {"url": url, "name": name, "version": version, "filename": filename, "hash": h, "text": text}

def load_targets(filename):
    with open(filename) as t:
        targets = json.loads(t.read())

def check_targets(targetlist):
    changelist = []
    newlist = []
    for target in targetlist:
        if target["saved"]:
            target = __check_url(target)
            if target["justchanged"]:
                changelist.append(deepcopy(target))
                target["justchanged"] = False
        else:
            target = __initiate_url(target)
            newlist.append(deepcopy(target))
    return (targetlist, changelist, newlist)
# then I need to call check_targets, save the targetlist, tweet out based on changelist and newlist.

