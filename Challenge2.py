import nltk
from nltk.tokenize import sent_tokenize, word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

text = "Hi everyone, today is day 2 of the challenge of ABTalks.today we are doing the tokenization."

# Sentence Tokenization
sentences = sent_tokenize(text)
print(sentences)

# Word Tokenization
words = word_tokenize(text)
print(words)