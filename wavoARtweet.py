import tweepy
from tweepy import StreamListener
from tweepy import Stream
from keys import wavoarkeys

CONSUMER_KEY = wavoarkeys['consumer_key']
CONSUMER_SECRET = wavoarkeys['consumer_secret']
ACCESS_TOKEN = wavoarkeys['access_token']
ACCESS_TOKEN_SECRET = wavoarkeys['access_token_secret']
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
            if 'soundcloud' or 'SoundCloud' or 'Soundcloud' in status.text:
                print('SOUNDCLOUD!!!!')
            #api.create_favorite(status.id)
                try:
                    message = '@' + s + ' Sweet track! Did you know you can gate free downloads and get more followers with Wavo? Try it free: http://bit.ly/WavoPRO'
                    api.update_status(status=message, in_reply_to_status_id=status.id)
                except:
                    print('DUPLICATE TWEET ERROR')
            #    try:
            #        print('duplicate tweet error')
            #        message = '@' + s + ' You tweeted with my hashtag AGAIN!'
            #        api.update_status(status=message, in_reply_to_status_id=status.id)
            #    except:
            #        print('double duplicate tweet error')
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
    stream.filter(track=['#freedownload'])