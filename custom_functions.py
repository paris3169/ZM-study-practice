# -*- coding: utf-8 -*-
"""008_custom_functions.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1tQYc9XAI_ZMPj8GI5XdXWkn4QwpV3w0Z
"""

#this is a list of my customized functiona created while practicing the session on Natural Language processing

import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import time
import random

def visualize_tweets(df,size=10):
  random_indexes=np.random.choice(df.index,size=size)
  include_target="target" in df.columns  #to check if the passed dataframe contain also the target label (is a train dataframe)
  if include_target==True:
    columns=["text","target"]
  else:
    columns=["text"]
  random_df=df[columns].loc[random_indexes]
  for row,col in random_df.iterrows():
    print(f"tweet index: {row}")
    text=col["text"]
    print(f"tweet: {text}")
    if include_target==True:
      target=col["target"]
      tweet_type="disaster" if target==1 else "no disaster"
      print(f"target: {target}, tweet_type: {tweet_type}")
    print("\n")

def get_most_wrong(test_sentences,test_labels,model,num=20):

    pred_probs=model.predict(test_sentences)
    y_pred=tf.squeeze(np.round(pred_probs),axis=1)
    df=pd.DataFrame({"tweet":test_sentences,"y_true":test_labels,"y_pred":y_pred,"pred_probs":tf.squeeze(pred_probs)})
    df["error"]=(df["y_true"]!=df["y_pred"])
    all_wrong=df.sort_values(by="pred_probs",ascending=False)
    most_wrong=all_wrong.head(num)
    return most_wrong