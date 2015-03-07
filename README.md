# aribot
Simple tweepy scripts for automated Twitter interactivity.

In the spirit of Twitter, share this project!

<a href="https://twitter.com/share" class="twitter-share-button" data-url="http://github.com/arirawr/aribot" data-text="Simple tweepy scripts for automated Twitter interactivity:" data-via="imariari" data-related="imariari" data-hashtags="python,twitter,botbotbot">Tweet</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>

<a href="https://twitter.com/imariari" class="twitter-follow-button" data-show-count="false">Follow @imariari</a>
<script>!function(d,s,id){var js,fjs=d.getElementsByTagName(s)[0],p=/^http:/.test(d.location)?'http':'https';if(!d.getElementById(id)){js=d.createElement(s);js.id=id;js.src=p+'://platform.twitter.com/widgets.js';fjs.parentNode.insertBefore(js,fjs);}}(document, 'script', 'twitter-wjs');</script>

__I'll be making some base use-case templates for you to use...stay tuned!__

## requirements

To run any of these scripts, you'll need:
- [python](https://www.python.org/downloads/)
- [tweepy](https://github.com/tweepy/tweepy) (`pip install tweepy`)
- [Twitter app and keys](https://apps.twitter.com/), with appropriate permissions (usually read and write)

## templates

__samplekeys.py__ is the place for your Twitter keys. If you put your project on Github, remember to .gitignore (see my .gitignore file)

__autotweet.py__ reads lines from a text file and tweets from your bot's account at specified intervals. To run: `python autotweet.py yourtextfile.txt`

## examples

#### Add your own scripts by submitting a pull request!

__aribot.py__ (from the _autotweet.py_ template) tweets every 90 seconds, pulling line-by-line from a text file that is given as an argument.

To run: 
`python aribot.py yourtextfile.txt`

---

_arireplybot.py_, when run, searches for a keyword and tweets at any users who used that keyword.

To run:
`python arireplybot.py`

_Note: will be updated later with error handling_

---

_aristreambot.py_ constantly monitors a stream of tweets with given filters and favourites, retweets, and replies.

To run:
`python aristreambot.py`

_Note: limited error handling. Will be updated._

---

_wavofave.py_ favorites all tweets with given keywords, with a 10 second delay.

To run:
`python wavofave.py`
