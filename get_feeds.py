import requests
import ast
import json
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
from tweepy import API

class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        self.print_formatted(data)
        return True

    def on_error(self, status):
        print(status)

    def print_formatted(self,data):
    	parsed_json = json.loads(data)
    	print(parsed_json['text'])
    	print(parsed_json['created_at'])



#Method to get Tweepy API object
def getAPI(opt):
	fp = open("twitter_keys.secure","r")
	fpRead = fp.readlines()
	secret_key = ast.literal_eval(fpRead[0])
	auth = OAuthHandler(secret_key['key'],secret_key['secret'])
	access_token = "617101081-J1NhQZ1yYU1yXEcG1GvhlsuNZK7IXBnHgQicdDXw"
	token_secret = "Ro1LiCKNszCfnq13VF43WJLxvVkGNXe4f8eOZhQjIC7RW"
	auth.set_access_token(access_token,token_secret)
	api = API(auth)
	if opt=="auth":
		return auth
	elif opt=="api":
		return api
	return api


if __name__ == '__main__':
    l = StdOutListener()
    auth = getAPI("auth")
    stream = Stream(auth, l)
    stream.filter(track=['shooting'])