import requests
import json
import time
import pushTweet
import get_key

on = True
oldNP = 0
username = get_key.getKey('lfm','username')
apiKey = get_key.getKey('lfm','api_key')



def lfmGet(payload):
    headers = {'user-agent': 'flexii'}

    url = 'https://ws.audioscrobbler.com/2.0/'
    payload['user'] = username
    payload['api_key'] = apiKey
    payload['format'] = 'json'
    payload['limit'] = '1'


    response = requests.get(url, headers=headers, params=payload)
    return response

while on:
    jsonData = lfmGet({'method': 'user.getRecentTracks'})
    obj = json.loads(jsonData.content.decode('utf-8'))
    newNP = (obj['recenttracks']['track'][1]['date'])
    if newNP != oldNP:
        contents = f"@flexiimusic is currently listening to {str(obj['recenttracks']['track'][0]['name'])} by {str(obj['recenttracks']['track'][0]['artist']['#text'])}!"
        pushTweet.tweetSong(contents)

    else:
        print('still playing same song!!')
    oldNP = newNP
    print(contents)
    time.sleep(60)
