import tweepy as tw
import pandas as pd

consumer_key = '9jdI3FD8w4qLc6p9aTxik28Rc'
consumer_secret = 'PKcB81s6dZT3ZX3MgFvT7N7Hd8ZJ9mjORpQW7UST14ZBAZ3fiZ'
access_token = '837035864869990401-jRnhuIG3F9NQ4NM64C7i8MotSporOp4'
access_token_secret = 't8AEPZiQ0NXacKYS2q2McuU3wE6mNOEnn2ot5EEWzMYzx'

auth = tw.OAuthHandler(consumer_key, consumer_secret)

auth.set_access_token(access_token,access_token_secret)

api = tw.API(auth, wait_on_rate_limit= True)

# Here are some of the best fantasy football experts and insiders to follow for up to date news
accounts = ['MatthewBerryTMR','AdamSchefter', 'The_Oddsmaker', 'justinboone','allinkid','evansilva','adamlevitan','SigmundBloom','JeneBramel','FieldYates']


tweet_id = []
text = []
created_at = []
favorite_count = []
retweet_count = []
user_id = []
user_screen_name = []
user_description = []
verified = []
Is_Quote =[]
Author_replied_to = []

for account in accounts:
    stream = api.user_timeline(account)
    print("Getting tweets from: @",account)
    for tweet in stream:
        tweet_id.append(tweet.id) # the tweet id
        text.append(tweet.text) # the actual full text of the tweet
        created_at.append(tweet.created_at) # when the tweet was created
        favorite_count.append(tweet.favorite_count) # number of times the tweet has been favorited
        retweet_count.append(tweet.retweet_count) # number of times the tweet has been re-tweeted
        verified.append(tweet.user.verified) # is user verified or not
        user_description.append(tweet.user.description) # description of user
        user_id.append(tweet.user.id) # User id
        user_screen_name.append(tweet.user.screen_name) # screen name
        Is_Quote.append(tweet.is_quote_status)    # whether or not tweet is a shared tweet from someone else and just added comments to it
        Author_replied_to.append(tweet.in_reply_to_screen_name) # screen name of account that the tweet was in reply to

dict = {'tweet_id': tweet_id,
              'text': text,
              'user': user_id,
              'user_screen_name': user_screen_name,
              'favorite_count': favorite_count,
              'retweet_count': retweet_count,
              'created_at': created_at,
              'user_description': user_description,
              'verified': verified,
              'Is_Quote': Is_Quote,
              'Author_replied_to': Author_replied_to
              }

df = pd.DataFrame(dict)

print(df)

df.to_csv("FantasyFootball.csv", index = True, header = True)