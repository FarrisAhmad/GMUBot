import tweepy
# Authenticate to Twitter
auth = tweepy.OAuthHandler("qVqsTAtCQqTrxBZ0YPjpc8JJz", "jIzg63IgE4GLeNkBiMkmLJQNXu2llFEd0gS7KSqycNFzJBGBON")
auth.set_access_token("1359691434299916288-6YLZrkIIFDYCwZngZZZq6mT8Kje3oE", "AvPZ89UNBGYCkOXWPTumrPtA6n9YrXg4WRGiW3rdiISpK")

# Create API object
api = tweepy.API(auth)
if api.verify_credentials() == False:
    #Throw an exception if the API credentials are not valid
    raise Exception("ERROR: API Credentials are invalid")
