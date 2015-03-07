# aribot
Simple tweepy scripts for automated Twitter interactivity.

__I'll be making some base use-case templates for you to use...stay tuned!__

## requirements

To run any of these scripts, you'll need:
- [python](https://www.python.org/downloads/)
- tweepy library  `pip install tweepy`

## templates

## scripts
_aribot.py_ tweets every 90 seconds, pulling line-by-line from a text file that is given as an argument.

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
