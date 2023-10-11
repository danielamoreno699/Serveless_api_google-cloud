
from flask import Flask, request, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')
#text = "I do not like it."

# sentiment analizer function for api
def SentimentAnalyzer(str):

    response = ''
    sia = SentimentIntensityAnalyzer()
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

# route
app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    if request.method == 'POST':
        data = request.get_json()
        text = data.get('text')

        if text:
            sia_response = SentimentAnalyzer(text)
            return jsonify(sia_response)
        else:
            return jsonify({'error': 'Please provide a "text" parameter in the request.'}), 400

if __name__ == "__main__":
    app.run(debug=True)