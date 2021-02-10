# -*- coding: utf-8 -*-


import os, sys
import re
import spacy
import random
import re
from spacy.util import minibatch, compounding
from spacy.scorer import Scorer
from spacy.gold import GoldParse
from spacy import displacy
import pandas as pd
import jsonlines
import random
import math
from pathlib import Path

nlp = spacy.load(os.path.abspath("Abusive"))

import tweepy
import re
from textblob import TextBlob
import datetime as DT
import matplotlib.pyplot as plt
import numpy

api_key= "nFvSqzCeuGCsSpljT0DxhpT93"
api_secret_key = "7mAYkwbbsqpwL9UxvNEaX8krmtttniST6MR7SvyRRTK593ulZB"
access_token = "3198259110-psr3uDfYIDJWeTa8sPQjXp9Qi4x5y6JP2XukYNy" 
access_token_secret = "H0kHwDgtNedWKtIdDwIDqFiIPAquYl9G95jA8J618FsNa"

auth = tweepy.OAuthHandler(api_key, api_secret_key) 
auth.set_access_token(access_token, access_token_secret) 
api=tweepy.API(auth)

df= pd.DataFrame()
for i in range(14):
  hasilAnalisis =[]
  today = DT.date.today()
  dayH = today - DT.timedelta(days=i)
  dayHminusOne = dayH-DT.timedelta(days=1)
  print(str(dayH))
  hasilSearch = api.search(q="pemerintah", lang="id", count=300, since=str(dayHminusOne), until=str(dayH))
  json_data = [r._json for r in hasilSearch]
  data = pd.io.json.json_normalize(json_data)
  df=df.append(data)

def klasifikasi(tweet):
  tweet_bersih = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)"," ",tweet).split())
  analysis=TextBlob(tweet_bersih)
  doc = nlp(tweet_bersih)
  if doc.cats['nonabusive']< doc.cats['abusive']:
    tweet="abusive"
  else :
    tweet="Nonabusive"
  return tweet

date=list(df['created_at'])
text = list(df['text'])
predict = [klasifikasi(data) for data in text]
predict_result = pd.DataFrame(
    {'text': text,
     'date':date ,
     'prediction': predict
    })

predict_result = pd.DataFrame(
    {'text': text,
     'date':date ,
     'prediction': predict
    })

predict_result.to_csv('data abuse detection')

print('New data added')

predict_result.to_csv(data,index=False)

print('Dataset updated')

