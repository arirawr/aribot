import tweepy, time
from tweepy import StreamListener
from tweepy import Stream
from keys import wavokeys

CONSUMER_KEY = wavokeys['consumer_key']
CONSUMER_SECRET = wavokeys['consumer_secret']
ACCESS_TOKEN = wavokeys['access_token']
ACCESS_TOKEN_SECRET = wavokeys['access_token_secret']
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

class StdOutListener(StreamListener):
    ''' Handles data received from the stream. '''
 
    def on_status(self, status):
        if 'RT' not in status.text:
        # Prints the text of the tweet
            print('Tweet text: ' + status.text)
            s = status.author.screen_name
            print(s)
            time.sleep(10)
            api.create_favorite(status.id)
        return True
 
    def on_error(self, status_code):
        print('Got an error with status code: ' + str(status_code))
        return True # To continue listening
 
    def on_timeout(self):
        print('Timeout...')
        return True # To continue listening
 
if __name__ == '__main__':
    listener = StdOutListener()
 
    stream = Stream(auth, listener)
    stream.filter(track=['#wavo', '#wavome', '@wavome', 'wavo', 'wavome'])