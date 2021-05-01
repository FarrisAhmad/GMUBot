import tweepy
from better_profanity import profanity
# Authenticate to Twitter
auth = tweepy.OAuthHandler("qVqsTAtCQqTrxBZ0YPjpc8JJz", "jIzg63IgE4GLeNkBiMkmLJQNXu2llFEd0gS7KSqycNFzJBGBON")
auth.set_access_token("1359691434299916288-6YLZrkIIFDYCwZngZZZq6mT8Kje3oE", "AvPZ89UNBGYCkOXWPTumrPtA6n9YrXg4WRGiW3rdiISpK")

# Create API object
api = tweepy.API(auth)

direct_messages = api.list_direct_messages()
print(direct_messages)
copy = direct_messages.copy()
print(copy)
for item in copy:
    print(item)
    api.update_status(str(item.message_create['message_data']['text']))
    api.destroy_direct_message(item.id)
mentions = api.mentions_timeline().copy()
for item in mentions:
    if (not (api.get_status(item.id).retweeted)) and (not profanity.contains_profanity(api.get_status(item.id).text)):
        api.retweet(item.id)

# api.update_status(direct_messages

#
# api qVqsTAtCQqTrxBZ0YPjpc8JJz
# api secret jIzg63IgE4GLeNkBiMkmLJQNXu2llFEd0gS7KSqycNFzJBGBON
#
#
# bearer AAAAAAAAAAAAAAAAAAAAAI6eNgEAAAAAQBDeNErgn1lIMw0ORDAYeMuPHyc%3DI0BY5rwIJ4DR9RnFyhy71XjQ4FmVpoGe909zGGL1Ch6XPr4BNn
# access 1359691434299916288-6YLZrkIIFDYCwZngZZZq6mT8Kje3oE
#
# access secret AvPZ89UNBGYCkOXWPTumrPtA6n9YrXg4WRGiW3rdiISpK

