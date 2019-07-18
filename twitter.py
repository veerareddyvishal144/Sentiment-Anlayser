import tweepy
from textblob import TextBlob
import unicodedata
cons_key='ekjtv5tJ0EsfdJD6KNMULxJ5N'
cons_secret='T8xHeMBXz6sKYq0roIPnkAsSGRKJrodR05dPlJMNpaJe49CVaM'
access_token='2551720986-ycC6dx2ivoKizrvHgugHNUmMAfmNs82ZL5GobPm'
access_token_secret='E95yv8Xgn0wcl7qhqRbOUxr8EwEntIifiRIuqEjUeV9rH'
auth=tweepy.OAuthHandler(cons_key,cons_secret)
auth.set_access_token(access_token,access_token_secret)
api=tweepy.API(auth)
pub_tweets=api.search(str(input("Enter your term:")))

for i in pub_tweets:
        try:
                st=i.text.encode("utf-8")
		
                
                print("%s\n"% st)  
                ana=TextBlob(i.text)
                print(ana)
                print(ana.sentiment)
        except:
                continue
   
