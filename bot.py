import tweepy

# Authenticate to Twitter
auth = tweepy.OAuthHandler("9sWBI5513kq2H4w3Do6la9TgM", "4jdmsjKxyJWA6EuMy1Y5oBhMISq03qOzALk5xGUwbky5l9YyCu")
auth.set_access_token("806902782531870722-R1eu6ZP72fwyfV3RXM7eqM0KhNyhrXb", "2Z9b1nPqzeslANsGBlSkggA8FdRpzczg9EcfoHXRZp7dk")

# Create API object
api = tweepy.API(auth)

# Create a tweet
api.update_status("Hello world")
