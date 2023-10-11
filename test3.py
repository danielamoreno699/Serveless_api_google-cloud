from flask import Flask, request, jsonify
from nltk.sentiment import SentimentIntensityAnalyzer

app = Flask(__name__)

@app.route('/sentiment', methods=['POST'])
def analyze_sentiment():
    data = request.get_json()
    text = data.get('text')

    if text:
        sia = SentimentIntensityAnalyzer()
        sentiment = sia.polarity_scores(text)
        return jsonify(sentiment)
    else:
        return jsonify({'error': 'Please provide a "text" parameter in the request.'}), 400

if __name__ == "__main__":
    app.run(debug=True)
