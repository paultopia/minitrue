# minitrue
defense against tamping with public data

monitor data tampering.  simple app to run on a vps (linode, digitalocean, etc.), feed it a list of URLs, and it will generate a hash of current content at that url, and then alert when changes.

the point: suppose Donald Trump goes full 1984 and tampers with government data.  For example, modifying climate data to conceal evidence of human generated climate change.  (Or some corporation screws with its shareholder information, etc. etc.)  Wouldn't it be nice to prove that the data has been tampered with?  Take the files (like the csv, or pdf reports, or whatever) online.  Feed the URLs to minitrue.  This application will save them on a server and tweet out a secure hash to allow you to prove that the saved file existed on the date of the tweet (assuming twitter isn't compromised, and doesn't decide to start allowing tweet editing). 

Then every day minitrue goes back and checks the url(s). If anything changes, it tweets out a change alert and saves the new file for purposes of comparision.  Some of those changes might be innocent (url changes, adding new data to an existing file).  Some might be malicious (retroactively changing data to deceive the public). Minitrue will allow you to prove that the new file is different from the file on the original date, and hence catch the malicious changes. 

Note: I recommend also printing out the hashes and using other date-verification methods (the old-fashioned "mail it to yourself" in a sealed envelope trick at a minimum) to confirm the date of the hashes. Just in case Twitter is compromised, or decides that this violates its rules and bans it. 

other verification methods coming if I can figure some out.  would be real nice to do a blockchain kind of thing. 

**WIP**

requires: 

- a twitter account with developer privs.  See tutorial for how to set this up here: https://www.digitalocean.com/community/tutorials/how-to-create-a-twitter-app 

- a \*nix server/vps 

will have:

installer shell script and frozen distributable
