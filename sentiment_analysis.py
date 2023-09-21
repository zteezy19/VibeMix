from textblob import TextBlob


def analyze(text: str) -> str:
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0:
        return "positive"
    if polarity < 0:
        return "negative"
    else:
        return "neutral"
