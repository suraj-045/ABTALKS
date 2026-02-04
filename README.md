# ABTalks Challenges

A collection of Python challenges for ABTalks.

## Challenges

### Challenge 1: User Details
A simple interactive script that collects and displays user information.

**Description:**
Prompts the user for their **Name**, **Age**, and **City**, then displays a formatted summary and greeting.

**Usage:**
```bash
python Challenge1.py
```

**Example Output:**
```text
Enter your name: Alice
Enter your age: 25
Enter your city: New York

--- user Details ---
Name: Alice
Age: 25
City:  New York

Hello Alice !
You are 25 years old and you live in New York
```

---

### Challenge 2: Tokenization
Demonstrates basic Natural Language Processing (NLP) using the NLTK library.

**Description:**
Performs sentence and word tokenization on a sample text string.

**Usage:**
Prerequisites:
```bash
pip install nltk
```
The script automatically downloads the required NLTK data (`punkt`, `punkt_tab`).

Run the script:
```bash
python Challenge2.py
```

**Example Output:**
```text
['Hi everyone, today is day 2 of the challenge of ABTalks.today we are doing the tokenization.']
['Hi', 'everyone', ',', 'today', 'is', 'day', '2', 'of', 'the', 'challenge', 'of', 'ABTalks.today', 'we', 'are', 'doing', 'the', 'tokenization', '.']
```

### Challenge 3: Stemming vs Lemmatization
Demonstrates the difference between Stemming and Lemmatization using NLTK.

**Description:**
Performs text cleaning (tokenization, removing HTML tags/non-alphabetic characters), and then compares the results of PorterStemmer and WordNetLemmatizer on a sample movie review.

**Usage:**
Prerequisites:
```bash
pip install nltk
```
The script automatically downloads required NLTK data (`punkt`, `wordnet`, `omw-1.4`).

Run the script:
```bash
python Challenge3.py
```

**Example Output:**
```text
Original Words (first 20):
['bad', 'plot', 'bad', 'dialogue', 'bad', 'acting', 'idiotic', 'directing', 'the', 'annoying', 'porn', 'groove', 'soundtrack', 'that', 'ran', 'continually', 'over', 'the', 'overacted', 'script']

Stemmed Words (first 20):
['bad', 'plot', 'bad', 'dialogu', 'bad', 'act', 'idiot', 'direct', 'the', 'annoy', 'porn', 'groov', 'soundtrack', 'that', 'ran', 'continu', 'over', 'the', 'overact', 'script']

Lemmatized Words (first 20):
['bad', 'plot', 'bad', 'dialogue', 'bad', 'acting', 'idiotic', 'directing', 'the', 'annoying', 'porn', 'groove', 'soundtrack', 'that', 'ran', 'continually', 'over', 'the', 'overacted', 'script']
```

### Challenge 4: Stopwords Removal
Demonstrates how to clean text by removing stopwords, punctuation, and converting to lowercase using NLTK and Regex.

**Description:**
Takes a noisy text (with special characters, URLs, HTML tags), cleans it using Regex, tokenizes it, and removes common English stopwords.

**Usage:**
Prerequisites:
```bash
pip install nltk
```
The script automatically downloads required NLTK data (`punkt`, `stopwords`).

Run the script:
```bash
python Challenge4.py
```

**Example Output:**
```text
Cleaned Text:
omg movie sooo goood cant even explain felt totally worth watching even night audio like sooo bad check httptinyurlcomxyz brbr btw watched x still wan na watch
```

## 📂 Project Structure

- `Challenge1.py`: User details script.
- `Challenge2.py`: Tokenization script.
- `Challenge3.py`: Stemming vs Lemmatization script.
- `Challenge4.py`: Stopwords removal script.
- `README.md`: Project documentation.
