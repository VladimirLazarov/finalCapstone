## Amazon Review Sentiment Analysis

This project analyzes the sentiment of Amazon product reviews using spaCy and TextBlob libraries. It helps understand the overall customer perception of the products based on their reviews.

**Table of Contents**

* Project Description
* Installation
* Usage
* Credits

**Project Description**

This Python script analyzes the sentiment of Amazon product reviews stored in a CSV file named "amazon_product_reviews.csv". It utilizes spaCy for text preprocessing and TextBlob for sentiment analysis. The script classifies each review as positive, negative, or neutral based on its polarity score.

**Installation**

1. Make sure you have Python 3.x installed on your system.
2. Open a terminal or command prompt and navigate to the directory containing this script and the CSV file.
3. Install the required libraries using pip:

```bash
pip install pandas spacy textblob
```

4. Download a small English language model for spaCy:

```bash
python -m spacy download en_core_web_sm
```

**Usage**

1. Run the script from the command line:

```bash
python amazon_review_sentiment.py
```

2. The script will analyze each review in the CSV file and print the review text, polarity score, and sentiment (positive, negative, or neutral) for each review.

**Example Output:**

```
Review: This product is amazing! It works exactly as advertised. 
Polarity score: 0.8 
Sentiment: positive

Review: This product is a complete waste of money. Do not buy it! 
Polarity score: -0.7 
Sentiment: negative

Review: The product is okay, but I expected better quality. 
Polarity score: 0.2 
Sentiment: neutral
```

**Credits**

* pandas: [https://pandas.pydata.org/](https://pandas.pydata.org/)
* spaCy: [https://spacy.io/](https://spacy.io/)
* TextBlob: [https://textblob.readthedocs.io/en/dev/quickstart.html](https://textblob.readthedocs.io/en/dev/quickstart.html)

**Note:**

This script provides a basic sentiment analysis example. More advanced techniques can be used for improved accuracy.
