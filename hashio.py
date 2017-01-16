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
import json, hash, datetime
from copy import deepcopy

def __exten(url):
    return url.rpartition(".")[2]

def __filename(exten, name, version_number):
    if exten in ["html", "htm", "json", "csv", "txt"]:
        return ''.join(name.split()) + str(version_number) + "." + exten + ".bin"  # identify text files that get binary-ified.
    else:
        return ''.join(name.split()) + str(version_number) + "." + exten

def __handle_changes(target, new_hash, prior_check):
    t = deepcopy(target)
    # bump version
    old_version = t["version"]
    version = t["version"] + 1
    t["version"] = version
    # bump filename
    old_filename = t["filename"]
    url = t["url"]
    name = t["name"]
    exten = __exten(url)
    new_filename = __filename(exten, name, t["version"])
    hash.fetch_and_save(url, new_filename) # save new file (assumes no additional change between first check and second which would be pretty unlikely)
    t["filename"] = new_filename
    # bump hash
    old_hash = t["hash"]
    t["hash"] = new_hash
    supplanted_date = t["last_checked"]
    if "change_history" not in t:
        t["change_history"] = []
    t["change_history"].append({"version": old_version, "filename": old_filename, "hash": old_hash, "last_seen": prior_check, "supplanted": supplanted_date})
    return t

def __check_url(target):
    """get url, check hash vs hash of saved file, and if new set changed bit and add a second version (or an nth version if versions field already exists).  If not new, just return orig with last checked added."""
    t = deepcopy(target)
    timestamp = datetime.datetime.now().isoformat()
    old_hash = t["hash"]
    new_hash = hash.fetch_and_hash(t["url"])
    prior_check = t["last_checked"]
    t["last_checked"] = timestamp
    if old_hash == new_hash:
        t["justchanged"] = False
        return t
    else:
        t["justchanged"] = True
        return __handle_changes(t, new_hash, prior_check)

def __initiate_url(target):
    t = deepcopy(target)
    timestamp = datetime.datetime.now().isoformat()
    url = t["url"]
    name = t["name"]
    exten = __exten(url)
    version = 1
    filename = __filename(exten, name, 1)
    hash.fetch_and_save(url, filename)
    h = hash.hashfile(filename)
    if exten in ["html", "htm", "json", "csv", "txt"]:
        textfile = True
    else:
        textfile = False
    return {"url": url, "name": name, "version": version, "filename": filename, "hash": h, "textfile": textfile, "added": timestamp, "last_checked": timestamp}

def __check_targets(targetlist):
    new_targets = []
    changes = []
    additions = []
    for target in targetlist:
        t = deepcopy(target)
        if "added" in t:
            t = __check_url(t)
            if t["justchanged"]:
                t["justchanged"] = False
                changes.append(t)
        else:
            t = __initiate_url(t)
            additions.append(t)
        new_targets.append(t)
    return {"targets": new_targets, "changes": changes, "additions": additions}

def check_from_file(targetfile):
    """
    takes json file with targets. checks. saves updated json file. returns a dict of check results where (additions, changes) need to be tweeted.
    """
    with open(targetfile) as infile:
        targetlist = json.load(infile)
    checked = __check_targets(targetlist)
    with open(targetfile, "w") as outfile:
        json.dump(checked["targets"], outfile, sort_keys = True, indent = 4)
    return checked
