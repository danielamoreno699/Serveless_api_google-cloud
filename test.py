# import nltk
# nltk.download()
# from nltk.tokenize import sent_tokenize, word_tokenize

# example_test= "Hello, There"
# print(sent_tokenize(example_test))

import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER lexicon (if not already downloaded)
nltk.download('vader_lexicon')

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Sample text for sentiment analysis
text = "I do not like it."

# Analyze the sentiment of the text
sentiment = sia.polarity_scores(text)
print(sentiment)
if sentiment['compound'] > 0:
    print('this is positive')
elif sentiment['compound'] < 0:
    print('this is negative')
else: 
    print('neither positive or negative')

# Interpret the sentiment scores
print("Sentiment Scores:")
print("Positive: ", sentiment['pos'])
print("Negative: ", sentiment['neg'])
print("Neutral: ", sentiment['neu'])
print("Compound: ", sentiment['compound'])
