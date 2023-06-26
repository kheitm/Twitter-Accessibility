#%%
# pip install versions s3fs==0.5.1 and fsspec==0.8.3
import tweepy
import pandas as pd 
import json
import s3fs 

# %%
def run_twitter_etl():

    consumer_key = "XXXX" 
    consumer_secret = "XXXX" 
    access_key = "XXXX"
    access_secret = "XXXX"


    # Twitter authentication
    auth = tweepy.OAuthHandler(access_key, access_secret)   
    auth.set_access_token(consumer_key, consumer_secret) 

    # # # Creating an API object 
    api = tweepy.API(auth)
    query = '#a11y -filter:retweets'
    limit = 1000
    tweets = tweepy.Cursor(api.search_tweets,
                            q=query,
                            lang="de", 
                            tweet_mode = 'extended').items(limit)


    ###  Creating data frame of tweet information
    user_info = [[tweet.user.screen_name, tweet.user.location, tweet._json["full_text"], tweet.created_at] for tweet in tweets]

    df = pd.DataFrame(user_info, columns=['User', 'Location', 'Text', 'Date'])
    df.to_csv('a11y_de_tweets.csv')

run_twitter_etl()
