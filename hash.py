from requests import get
from shutil import copyfileobj
from hashlib import sha256
import gzip

# fetch and save to file
def fetch_and_save(url, name):
	file = get(url, stream=True)
	with open(name, 'wb') as out:
		copyfileobj(file.raw, out)

# generate sha265 of file
def hashfile(file):
	with open(file, "rb") as infile:
		f = infile.read()
	hash = sha256()
	hash.update(f)
	return hash.hexdigest()

# generate sha265 of stream directly from url (to use for modification checks)
def fetch_and_hash(url):
	file = get(url, stream=True)
	f = file.raw.read()
	hash = sha256()
	hash.update(f)
	return hash.hexdigest()

# some files show up gzizpped, and this saves text files in binary. The function below gets them out either way.
def open_binary_string_file(filename):
	try:
		with open(filename, "rb") as f:
			bytes = f.read()
			return bytes.decode()
	except UnicodeDecodeError:
		with gzip.open(filename, "rb") as f:
			bytes = f.read()
			return bytes.decode()
