import pandas as pd
import spacy
from textblob import TextBlob

# Load the dataset 
amazon_products = pd.read_csv('amazon_product_reviews.csv', low_memory=False)

# Get info 
print(amazon_products.info())

# Select relevant columns and remove missing values 
amazon_products = amazon_products[['reviews.text']].dropna()

# Load the spaCy model
nlp = spacy.load("en_core_web_sm")

def analyze_polarity(review_text):
    # Preprocess the text with spaCy
    doc = nlp(review_text)

    # Analyze sentiment with TextBlob
    blob = TextBlob(review_text)
    polarity = blob.sentiment.polarity

    return polarity

for review_text in amazon_products['reviews.text']:
    polarity_score = analyze_polarity(review_text)

    if polarity_score > 0:
        sentiment = 'positive'
    elif polarity_score < 0:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'

    print(f"Review: {review_text}\nPolarity score: {polarity_score}\nSentiment: {sentiment}\n")
