import tweepy, time, sys
from samplekeys import keys # This goes into samplekeys.py and takes the "keys" set. You can also specify another set of keys.
 
argfile = str(sys.argv[1]) # You will need to pass a .txt file as an argument in order to assign this.
 
CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

# Set up OAuth - basically logging into the account.
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
 
filename=open(argfile,'r')
f=filename.readlines() # Read the lines of the textfile one-by-one 
filename.close()
 
for line in f:
    api.update_status(status=line)
    time.sleep(x) # Tweet every x seconds (add any value)

# IMPORTANT
# 1. Make sure you pass a textfile as an argument (see README.md for instructions on how to run this in Terminal)
# 2. Don't leave empty lines in your textfile! (Or, handle those errors accordingly)
# 3. Twitter doesn't allow repeat statuses. Avoid repeated lines, or handle the errors accordingly.