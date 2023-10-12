from flask import Flask, request, jsonify
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

nltk.download('vader_lexicon')

app = Flask(__name__)

# Define the sentiment analyzer function
def SentimentAnalyzer(text):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(text)

    if sentiment['compound'] > 0:
        response = 'This is positive'
    elif sentiment['compound'] < 0:
        response = 'This is negative'
    else:
        response = 'This is neutral'
    return response


@app.route('/sentiment', methods=['GET'])
def analyze_sentiment():
    text = request.args.get('q')  

    if text:
        sia_response = SentimentAnalyzer(text)
        result = {'result': sia_response}
        return jsonify(result)
    else:
        return jsonify({'error': 'Please provide a "q" query parameter in the URL.'}), 400

if __name__ == '__main__':
    app.run(debug=True)

