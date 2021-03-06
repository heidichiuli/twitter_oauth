from requests_oauthlib import OAuth1Session
import secrets
import json

client_key = secrets.api_key
client_secret = secrets.api_secret

resource_owner_key = secrets.access_token
resource_owner_secret = secrets.access_owner_secret

protected_url = 'https://api.twitter.com/1.1/account/settings.json'

oauth = OAuth1Session(client_key,
                          client_secret=client_secret,
                          resource_owner_key=resource_owner_key,
                          resource_owner_secret=resource_owner_secret)

protected_url = 'https://api.twitter.com/1.1/search/tweets.json'
params = {'q':'food'}
r = oauth.get(protected_url, params=params)
#print (r.text)

list_of_tweets = json.loads(r.text)
the_str = ''
for dictionary in list_of_tweets['statuses']:
    print(dictionary['user']['screen_name'] + "\n" + dictionary['text'] + "\n--------")
