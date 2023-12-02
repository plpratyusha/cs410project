import json
import pandas as pd


data_file = 'reviews.csv'

# Load the CSV data into a pandas DataFrame
data = pd.read_csv(data_file, delimiter=',')

# Remove irrelevant columns
data = data.drop(['ReviewId', 'RecipeId', 'AuthorId', 'AuthorName', 'DateSubmitted', 'DateModified'], axis=1)

# Handle missing values
data.dropna(subset=['Rating', 'Review'], inplace=True)

# Text preprocessing
data['Review'] = data['Review'].str.lower()
data['Review'] = data['Review'].str.replace('[^\w\s]', '')
data['Review'] = data['Review'].str.split().str.join(' ')

# Data partitioning
from sklearn.model_selection import train_test_split

train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)




from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer

# Create a bag-of-words representation of the reviews
vectorizer = CountVectorizer()
train_features = vectorizer.fit_transform(train_data['Review'].values)
test_features = vectorizer.transform(test_data['Review'].values)

# Train the Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(train_features, train_data['Rating'].values)

# Classify the testing set
predicted_sentiment = classifier.predict(test_features)

# Evaluate the performance of the classifier
from sklearn.metrics import accuracy_score

accuracy = accuracy_score(test_data['Rating'].values, predicted_sentiment)
print("Accuracy:", accuracy)



import pandas as pd
from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics import accuracy_score

# Fit and transform the vectorizer on your training data
vectorizer = CountVectorizer()
train_features = vectorizer.fit_transform(train_data['Review'].values)

# Transform the test data using the same vocabulary
test_features = vectorizer.transform(test_data['Review'].values)

# Train the Naive Bayes classifier
classifier = MultinomialNB()
classifier.fit(train_features, train_data['Rating'].values)

# Test the scraped comment data

# Load the CSV data into a pandas DataFrame
data_file = 'comments_and_ratings.csv'
scraped_data = pd.read_csv(data_file, delimiter=',')

# Handle missing values
scraped_data.dropna(subset=['Comment', 'Rating'], inplace=True)

# Text preprocessing
scraped_data['Comment'] = scraped_data['Comment'].str.lower()
scraped_data['Comment'] = scraped_data['Comment'].str.replace('[^\w\s]', '')
scraped_data['Comment'] = scraped_data['Comment'].str.split().str.join(' ')

# Transform the scraped data using the same vectorizer
scraped_features = vectorizer.transform(scraped_data['Comment'].values)

# Classify the scraped data
predicted_sentiment = classifier.predict(scraped_features)

# Save sentiment analysis results to a JSON file
results = {
    "comments": scraped_data['Comment'].values.tolist(),
    "actual_ratings": scraped_data['Rating'].values.tolist(),
    "predicted_ratings": predicted_sentiment.tolist()
}

json_file_path = 'sentiment_results.json'
with open(json_file_path, 'w') as json_file:
    json.dump(results, json_file)

# Display comment, actual rating, and predicted classification
for comment, actual_rating, predicted_rating in zip(scraped_data['Comment'].values, scraped_data['Rating'].values, predicted_sentiment):
    print(f"Comment: {comment}\nActual Rating: {actual_rating}\nPredicted Classification: {predicted_rating}\n")
    
# Evaluate the performance of the classifier
accuracy = accuracy_score(scraped_data['Rating'].values, predicted_sentiment)
print("Accuracy:", accuracy)

