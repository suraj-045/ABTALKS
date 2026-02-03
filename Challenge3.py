import re
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required NLTK resources (run once)

nltk.download('wordnet')
print("WordNet loaded successfully")
nltk.download('omw-1.4')

review = """
Bad plot, bad dialogue, bad acting, idiotic directing, the annoying porn groove soundtrack
that ran continually over the overacted script, and a crappy copy of the VHS cannot be
redeemed by consuming liquor. Trust me, because I stuck this turkey out to the end.
It was so pathetically bad all over that I had to figure it was a fourth-rate spoof of
Springtime for Hitler.<br /><br />
The girl who played Janis Joplin was the only faint spark of interest, and that was only
because she could sing better than the original.<br /><br />
If you want to watch something similar but a thousand times better, then watch
Beyond The Valley of The Dolls.
"""

# STEP 1: Clean the text
clean_text = review.lower()
clean_text = re.sub(r'<br\s*/?>', ' ', clean_text)   
clean_text = re.sub(r'[^a-z\s]', '', clean_text)  

# STEP 2: Tokenization
tokens = word_tokenize(clean_text)

# STEP 3: Stemming
stemmer = PorterStemmer()
stemmed_tokens = [stemmer.stem(word) for word in tokens]

# STEP 4: Lemmatization
lemmatizer = WordNetLemmatizer()
lemmatized_tokens = [lemmatizer.lemmatize(word) for word in tokens]

# STEP 5: Comparison
print("Original Words (first 20):")
print(tokens[:20])

print("\nStemmed Words (first 20):")
print(stemmed_tokens[:20])

print("\nLemmatized Words (first 20):")
print(lemmatized_tokens[:20])