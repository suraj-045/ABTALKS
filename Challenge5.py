import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download required NLTK data (run once)
nltk.download('punkt')
nltk.download('stopwords')

# Step 1: Read CSV
df = pd.read_csv("news_dataset.csv", engine="python", encoding='utf-8')

# Step 2: Combine title and content
df["text"] = df["title"].fillna("") + " " + df["content"].fillna("")

# Pre-load stopwords to avoid re-loading in loop (Performance optimization)
stop_words = set(stopwords.words('english'))

# Step 3: Simple preprocessing function
def clean_text(text):
    if not isinstance(text, str):
        return ""
    text = text.lower()                          # lowercase
    text = re.sub(r'[^a-z\s]', '', text)         # remove numbers & punctuation
    words = word_tokenize(text)                  # tokenize
    
    words = [w for w in words if w not in stop_words]
    return " ".join(words)                       # join with space

# Step 4: Apply cleaning to all news
df["cleaned_text"] = df["text"].apply(clean_text)

# Step 5: Print output
print("Cleaned News Articles:\n")
for i, text in enumerate(df["cleaned_text"], start=1):
    print(f"Article {i}: {text}")