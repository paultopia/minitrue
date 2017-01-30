from requests import get
import json

site = "https://hash-archive.org"
#site = "http://localhost:8000"

def hx_check(url, hash):
	conn = get(site+"/api/enqueue/"+url, stream=True)
	data = conn.raw.read();
	obj = json.loads(data.decode())
	#print(hash, obj["hashes"])
	# TODO: Compare?

def hx_all(targets):
	for target in targets:
		hx_check(target["url"], target["hash"])

