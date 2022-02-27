import tweepy
import get_key

a = 'twitter'
key = get_key

apiKey = key.getKey(a,'api_key')
apiSecret = key.getKey(a,'secret')
accessToken = key.getKey(a,'access_token')
accessTokenSecret = key.getKey(a,'access_secret')

client = tweepy.Client(consumer_key=apiKey,
                       consumer_secret=apiSecret,
                       access_token=accessToken,
                       access_token_secret=accessTokenSecret)

def tweetSong(tweet):
    client.create_tweet(text=tweet)
