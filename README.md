# Amazon Product Review Sentiment Analyzer

## Description
This project analyzes the sentiment of Amazon product reviews. It is essential for businesses to understand customer sentiment towards their products to improve customer satisfaction and product quality. This tool uses natural language processing techniques to analyze the polarity of the reviews, categorizing them as positive, negative, or neutral.

## Table of Contents
1. [Installation](#installation)
2. [Usage](#usage)
3. [Credits](#credits)

## Installation
To install this project locally, follow these steps:
1. Clone this repository to your local machine.
2. Install the required dependencies:
3. Download the dataset 'amazon_product_reviews.csv' and place it in the project directory.

## Usage
Once you have installed the project, you can use it as follows:
1. Run the provided Python script.
2. The script will load the dataset, analyze the sentiment of each review, and print the results.
3. You can modify the script to suit your needs, such as saving the results to a file or integrating it into a larger application.

Example:
```python
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
