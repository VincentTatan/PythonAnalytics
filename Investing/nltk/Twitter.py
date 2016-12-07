from tweepy import Stream
from tweepy import OAuthHandler
from tweepy.streaming import StreamListener
from textblob import TextBlob

from twitterapistuff import *
from kitchen.text.converters import to_bytes,to_unicode

import json

class listener(StreamListener):

    def on_data(self, data):
    	try:
    		json_data = json.loads(data)
	    	post = json_data["text"]
	    	postblob = TextBlob(post)
	    	sentiment_value,subjectivity = postblob.sentiment.polarity,postblob.sentiment.subjectivity
	    	if subjectivity*100>=80: #It is a good tweet
	    		print (post,sentiment_value,subjectivity) 	#Review the post if it is subjective
	    		if sentiment_value>0:
	    			sentiment='pos'
	    		else:
	    			sentiment='neg'
	    		# Giving a count if tweet is good or not.
	        	output = open("twitter-out.txt","a")
	        	output.write(to_bytes(sentiment))
	        	output.write('\n')
	        	output.close()
			return True
        
    	except Exception, e:
    		return True
    	# print(data)
    	# encoder = json.JSONEncoder()
    	

    def on_error(self, status):
        print status

auth = OAuthHandler(ckey, csecret)
auth.set_access_token(atoken, asecret)

t = u"walmart"
twitterStream = Stream(auth, listener())
twitterStream.filter(track=[t])