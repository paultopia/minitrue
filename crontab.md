## Tentative instructions for using crontab to run on a vps. 

(I'm personally trying this out as we speak, so these instructions may change if something breaks.)

**First change**: crontab doesn't necessarily run in the directory of the script, so rather than the below, a better strategy is to just write a shell script that changes to the relevant directory and then runs from there.

I'm personally testing this on the smallest ($5/mo) digitalocean [droplet](https://www.digitalocean.com/products/compute/), running 32 bit ubuntu 16.10. 

1.  Install dependencies. These include python 3.x, tweepy, and requests.  If you just use the anaconda python installation, it'll include requests (and lots of other stuff besides.)

```
apt-get update
curl -o anaconda.sh https://repo.continuum.io/archive/Anaconda3-4.2.0-Linux-x86.sh
bash ~/anaconda.sh -b -p /root/anaconda
echo "export PATH=/root/anaconda/bin:$PATH" >> .bashrc
source .bashrc
pip install tweepy
```

2.  Get minitrue on your vps:

```
mkdir minitrue
cd minitrue
curl -Lk minitrue.tar.gz https://github.com/paultopia/minitrue/archive/v0.1.0.tar.gz | tar zx
cd minitrue-0.1.0/
chmod +x addurl.py
chmod +x minitrue.py

```

3.  Add twitter credentials (see the readme for a link to a tutorial) to a file in this directory named `twittercreds.json`.  Use the editor of your choice. JSON format, the file should look like this: 

```
{"consumer_key": "YOUR_INFO",
 "consumer_secret": "YOUR_INFO",
 "access_token": "YOUR_INFO",
 "access_secret": "YOUR_INFO"}
 ```
 
4. get the full path of your python install with `which python`

5. get the full path of minitrue with `readlink -f minitrue.py`

6. edit your crontab with crontab -e 

7.  Put the following line in, replacing as appropriate. 

`@daily PATH_TO_PYTHON PATH_TO_MINITRUE > /dev/null 2>&1`

This will run at midnight every day.  If you want, do it at a different time (which might help in disguising minitrue traffic down the road.) See [crontab tutorial](https://help.ubuntu.com/community/CronHowto) for how.

NOTE: some of these commands may require sudo if you use them from an account other than root.  I'm just living dangerously and doing it from root.
