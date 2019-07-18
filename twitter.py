import tweepy
from textblob import TextBlob
import unicodedata
cons_key=''
cons_secret=''
access_token=''
access_token_secret='H'
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
   
