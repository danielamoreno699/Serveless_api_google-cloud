
from flask import Flask, request, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
text = "I do not like it."

def SentimentAnalyzer(str):

    response = ''
    sia = SentimentIntensityAnalyzer()
# Analyze the sentiment of the text
    sentiment = sia.polarity_scores(text)

    if sentiment['compound'] > 0:
        response = 'this is positive'
        print('this is positive')
    elif sentiment['compound'] < 0:
        response = 'this is negative'
        print('this is negative')
    else: 
        response = 'this is neutral'
        print('neutral')
    return response
SentimentAnalyzer(text)

