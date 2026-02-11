from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

# simple example sentences
docs = [
    "AI is helpful",
    "AI AI makes work easy",
    "Blockchain improves security",
    "The system is running fast"
]

print("Documents:")
for d in docs:
    print(d)

print("\n--- Bag of Words ---")

bow = CountVectorizer()
bow_result = bow.fit_transform(docs)

print("Words:", bow.get_feature_names_out())
print(bow_result.toarray())

print("\n--- TF IDF ---")

tfidf = TfidfVectorizer()
tfidf_result = tfidf.fit_transform(docs)

print("Words:", tfidf.get_feature_names_out())
print(tfidf_result.toarray())