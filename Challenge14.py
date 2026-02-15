import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from collections import Counter
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer

nltk.download('punkt')
nltk.download('stopwords')

# example text (you can change)
text = """AI is rapidly transforming modern industries by improving automation, data analysis, and decision making.
         Many companies are using machine learning systems to understand customer behavior, reduce manual work, and increase productivity.
         As technology continues to evolve, organizations focus on building smarter solutions that can learn from data and adapt to real-world challenges."""

# STEP 1 – Cleaning & Tokenizing
text_lower = text.lower()
text_clean = re.sub(r'[^a-z\s]', '', text_lower)

words = word_tokenize(text_clean)

stop_words = set(stopwords.words('english'))
words = [w for w in words if w not in stop_words]

print("\nCleaned Words:")
print(words)

# STEP 2 – Word Frequency
freq = Counter(words)
print("\nWord Frequency:")
print(freq)
# STEP 2 – BoW & TF-IDF
docs = [text]

bow = CountVectorizer()
bow_result = bow.fit_transform(docs)
print("\nBoW Words:")
print(bow.get_feature_names_out())
print(bow_result.toarray())

tfidf = TfidfVectorizer()
tfidf_result = tfidf.fit_transform(docs)
print("\nTF-IDF Words:")
print(tfidf.get_feature_names_out())
print(tfidf_result.toarray())

# STEP 3 – Simple Pipeline
def pipeline(t):
    t = t.lower()
    t = re.sub(r'[^a-z\s]', '', t)
    w = word_tokenize(t)
    w = [x for x in w if x not in stop_words]
    return w

print("\nPipeline Test:")
print(pipeline("Machine learning helps AI systems"))