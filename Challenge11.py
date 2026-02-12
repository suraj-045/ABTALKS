from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# -----------------------------
# Documents (given for Day 11)
# -----------------------------
doc1 = "Machine learning models help companies analyze large amounts of data to find patterns, make predictions, and improve business decisions."

doc2 = "Data science uses algorithms and statistical techniques to study datasets, discover insights, and support smarter decision making in organizations."

docs = [doc1, doc2]

print("Document 1:\n", doc1)
print("\nDocument 2:\n", doc2)

print("\n-----------------------------")

# -----------------------------
# Convert text to TF-IDF vectors
# -----------------------------
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(docs)

# -----------------------------
# Calculate Cosine Similarity
# -----------------------------
similarity = cosine_similarity(tfidf_matrix[0], tfidf_matrix[1])

print("Cosine Similarity Score:")
print(similarity[0][0])