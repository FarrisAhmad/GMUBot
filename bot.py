import tweepy
from better_profanity import profanity
from lotStructure import *

#Define Structure of mason lots that we will monitor
masonLots=LotList()
masonLots.appendLot("A")
masonLots.appendLot("L")
masonLots.appendLot("C")
masonLots.appendLot("K")
masonLots.appendLot("PV")
masonLots.appendLot("M")
masonLots.appendLot("O")
masonLots.appendLot("P")

#To build string with all lots, call masonLots.buildUpdateMessage()
# Specify select lots by passing a list of strings as a parameter ie: masonLots.buildUpdateMessage(["a", "PV"])

#Listener class
class MyStreamListener(tweepy.StreamListener):
    def on_status(self, status):
        print(status)
        direct_messages = api.list_direct_messages()
        # For each direct message in the list, tweet out the message and then delete it.
        for item in direct_messages:
            print(item)
            # check for profanity in the direct message before tweeting
            if (not profanity.contains_profanity(str(item.message_create['message_data']['text']))):
                api.update_status(str(item.message_create['message_data']['text']))
            # delete the message so it is not tweeted multiple times
            api.destroy_direct_message(item.id)
        if ((not (api.get_status(status.id).retweeted)))  and (not profanity.contains_profanity(status.text)):
            api.retweet(status.id)
    def on_error(self, status_code):
        print("ERROR"+status_code)
        if status_code == 420:
            #returning False in on_data disconnects the stream
            return False
class MessageListener(tweepy.StreamListener):
    def on_direct_message( self, status ):
        print("Entered on_direct_message()")
        try:
            print(status)
            return True
        except BaseException as e:
            print("Failed on_direct_message()", str(e))
    def on_error(self, status_code):
        print("ERROR"+str(status_code))
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
