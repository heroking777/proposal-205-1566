import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score

# Load the data from Excel file
data = pd.read_excel('inter_school_205_info.xlsx')

# Preprocess the data
data['English'] = data['English'].fillna('')
data['Japanese'] = data['Japanese'].fillna('')

# Split the data into features and target
X = data[['English', 'Japanese']]
y = data['Category']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Vectorize the text data using TF-IDF
vectorizer = TfidfVectorizer()
X_train_vec = vectorizer.fit_transform(X_train['English'] + ' ' + X_train['Japanese'])
X_test_vec = vectorizer.transform(X_test['English'] + ' ' + X_test['Japanese'])

# Train a Naive Bayes classifier
clf = MultinomialNB()
clf.fit(X_train_vec, y_train)

# Evaluate the model on the test set
y_pred = clf.predict(X_test_vec)
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy:.2f}')