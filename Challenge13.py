import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

# download once
nltk.download('punkt')
nltk.download('stopwords')

# simple preprocessing pipeline
def pipeline(text):
    text = text.lower()                      # lowercase
    text = re.sub(r'[^a-z\s]', '', text)    # remove symbols and numbers
    words = word_tokenize(text)              # tokenize

    stop_words = set(stopwords.words('english'))
    words = [w for w in words if w not in stop_words]  # remove stopwords

    return words

# example spam & normal messages
messages = [
    "WIN MONEY NOW!!! Click this link to claim prize",
    "Hey bro, are we meeting today?",
    "FREE offer just for you!!!",
    "Let's finish our assignment tonight"
]

# run pipeline
for m in messages:
    print("\nOriginal:", m)
    print("Processed:", pipeline(m))