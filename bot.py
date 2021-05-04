import tweepy
from better_profanity import profanity
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status)
        if ((not (api.get_status(status.id).retweeted)))  and (not profanity.contains_profanity(status.text)):
            api.retweet(status.id)
    def on_error(self, status_code):
        print("ERROR")
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
# Authenticate to Twitter
auth = tweepy.OAuthHandler("qVqsTAtCQqTrxBZ0YPjpc8JJz", "jIzg63IgE4GLeNkBiMkmLJQNXu2llFEd0gS7KSqycNFzJBGBON")
auth.set_access_token("1359691434299916288-6YLZrkIIFDYCwZngZZZq6mT8Kje3oE", "AvPZ89UNBGYCkOXWPTumrPtA6n9YrXg4WRGiW3rdiISpK")

# Create API object
api = tweepy.API(auth)
#Collect any direct messages sent to the user
myStreamListener = MyStreamListener()
myStream = tweepy.Stream(auth = api.auth, listener=myStreamListener)
myStream.filter(track=['GeorgeMasonPark'],is_async=True)
