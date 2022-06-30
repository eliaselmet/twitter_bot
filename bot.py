import tweepy
from credentials import * 

client = tweepy.Client(bearer_token=bearer_token,
                        consumer_key= consumer_key,
                        consumer_secret= consumer_secret,
                        access_token= access_token,
                        access_token_secret=access_token_secret)  

#response = client.create_tweet(text='hello world 2')
query = 'barcelona'
max_results = 10

def searchTweets(client, query, max_results):
    tweets = client.search_recent_tweets(query=query, max_results=max_results)
    tweet_data =  tweets.data
    results = []
    if not tweet_data is None and len(tweet_data) > 0:
        for tweet in tweet_data:
            obj = {}
            obj['id'] = tweet.id
            obj['text'] = tweet.text
            results.append(obj)
        return results

results = searchTweets(client,query,max_results)

print(results)