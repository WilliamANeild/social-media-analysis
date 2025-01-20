import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from nltk import tokenize

class SentimentAnanlysisService:
    def __init__(self):
        nltk.download('punkt_tab')
        nltk.download('vader_lexicon')
        self.sid = SentimentIntensityAnalyzer()

    def get_sentiment(self, text: str) -> float:
        tokens = tokenize.sent_tokenize(text)
        total = 0
        for token in tokens:
            ss = self.sid.polarity_scores(token)
            total += ss.get("compound", 0)
        return total/len(tokens)