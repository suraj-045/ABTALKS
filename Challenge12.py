import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

nltk.download('punkt')
nltk.download('stopwords')

# simple pipeline function
def pipeline(text):
    text = text.lower()                      # lowercase
    text = re.sub(r'[^a-z\s]', '', text)    # remove punctuation
    words = word_tokenize(text)              # tokenize

    stop_words = set(stopwords.words('english'))
    words = [w for w in words if w not in stop_words]   # remove stopwords

    return words

# test texts
texts = [
    "Why is AI amazing!",
    "Machine learning helps automation.",
    "The system is running fast."
]

for t in texts:
    print("\nOriginal:", t)
    print("Output:", pipeline(t))