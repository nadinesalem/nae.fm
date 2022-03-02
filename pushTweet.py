import tweepy
import get_key

a = 'twitter'
key = get_key

apiKey = key.getKey(a,'api_key')
apiSecret = key.getKey(a,'secret')
accessToken = key.getKey(a,'access_token')
accessTokenSecret = key.getKey(a,'access_secret')

auth = tweepy.OAuthHandler(apiKey, apiSecret)
auth.set_access_token(accessToken, accessTokenSecret)



def tweetSong(tweet):
    api = tweepy.API(auth)
    api.update_status(tweet)
