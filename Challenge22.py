import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# Step 1: Example Dataset
texts = [
"Win money now",
"Limited time offer click here",
"Free prize waiting for you",
"Congratulations you won a reward",
"Call me later",
"Hey how are you",
"Let's meet tomorrow",
"Did you finish the assignment",
"See you at the meeting",
"Please review the document"
]

labels = [1,1,1,1,0,0,0,0,0,0]   # 1 = spam, 0 = normal

data = pd.DataFrame({"text": texts, "label": labels})

# Step 2: Feature Extraction
vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data["text"])

y = data["label"]

# Step 3: Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Step 4: Train Logistic Regression
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 5: Prediction
y_pred = model.predict(X_test)

# Step 6: Evaluation
print("\nAccuracy:", accuracy_score(y_test, y_pred))

print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, y_pred))