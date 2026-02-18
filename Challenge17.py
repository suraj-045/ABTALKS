import nltk
from nltk.tokenize import word_tokenize
from collections import Counter
from scipy.stats import poisson

nltk.download('punkt')

# simple example text
text = """
Artificial intelligence is helping businesses automate tasks and improve decision making.
AI systems analyze large amounts of data to find useful patterns.
Many industries use machine learning to increase efficiency and reduce manual work.
"""

# Step 1: tokenize words
words = word_tokenize(text.lower())

print("\nWords:")
print(words)

# Step 2: word frequency
freq = Counter(words)

print("\nWord Frequency:")
print(freq)

# Step 3: probability
total_words = len(words)

print("\nWord Probabilities:")
for w, c in freq.items():
    print(w, ":", round(c / total_words, 3))

# Step 4: simple distribution
# example: probability of word appearing 2 times
lam = freq['ai']   # use ai count as lambda
prob = poisson.pmf(2, lam)

print("\nPoisson Example (k=2, lambda=ai_count):")
print(prob)