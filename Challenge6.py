import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from collections import Counter
import matplotlib.pyplot as plt

# Download NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Step 1: Read CSV (same as Day 5)
df = pd.read_csv("news_dataset.csv", engine="python", encoding="utf-8")

# Step 2: Combine title and content
df["text"] = df["title"].fillna("") + " " + df["content"].fillna("")

stop_words = set(stopwords.words("english"))

# Step 3: Simple cleaning function
def clean_text(text):
    text = text.lower()
    text = re.sub(r'[^a-z\s]', '', text)
    words = word_tokenize(text)
    words = [w for w in words if w not in stop_words]
    return words

# Step 4: Apply cleaning and collect all words
all_words = []
for t in df["text"]:
    all_words.extend(clean_text(t))

# Step 5: Word frequency distribution
freq_dist = Counter(all_words)

# Top 20 most frequent words
top_20 = freq_dist.most_common(20)

# Print top 20
print("Top 20 Most Frequent Words:\n")
for word, count in top_20:
    print(f"{word}: {count}")

# Step 6: Visualization
words = [w for w, c in top_20]
counts = [c for w, c in top_20]

plt.figure()
plt.bar(words, counts)
plt.xticks(rotation=45)
plt.title("Top 20 Most Frequent Words")
plt.xlabel("Words")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()