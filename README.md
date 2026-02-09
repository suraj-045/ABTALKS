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

### Challenge 5: News Dataset Cleaning
Demonstrates text preprocessing on a real-world style CSV dataset.

**Description:**
Reads a noisy news dataset (`news_dataset.csv`), combines title and content, and performs text cleaning (lowercasing, removing special characters/numbers, tokenization, and stopword removal).

**Usage:**
Prerequisites:
```bash
pip install pandas nltk
```
The script automatically downloads required NLTK data (`punkt`, `stopwords`).

Run the script:
```bash
python Challenge5.py
```

**Example Dataset (`news_dataset.csv`):**
Contains fields: `id`, `title`, `content`.

**Example Output:**
```text
Cleaned News Articles:
Article 1: breaking election results election results finally shocker elections...
Article 2: tech giants release new ai models google openai released new models...
...
```

### Challenge 6: Word Frequency Visualization
Analyzes word frequency in the news dataset and creates a bar chart of the top 20 most frequent words.

**Description:**
Reads the `news_dataset.csv`, combines title and content, performs text cleaning (tokenization, stopword removal), counts word frequencies, and generates a bar chart saved as an image.

**Usage:**
Prerequisites:
```bash
pip install pandas nltk matplotlib
```
The script automatically downloads required NLTK data (`punkt`, `stopwords`) if missing.

Run the script:
```bash
python Challenge6.py
```

**Output:**
- Prints the top 20 most frequent words to the console.
- Saves a bar chart visualization to `top_20_words.png`.

**Example Console Output:**
```text
Top 20 Most Frequent Words:

new: 10
pm: 3
match: 3
...
```

### Challenge 8: WordPiece Tokenization (Hugging Face)
Demonstrates subword tokenization using the Hugging Face `tokenizers` library.

**Description:**
Trains a WordPiece tokenizer on the `news_dataset.csv` corpus to handle out-of-vocabulary words by breaking them into subword units. This approach is widely used in modern NLP models like BERT.

**Usage:**
Prerequisites:
```bash
pip install pandas tokenizers
```

Run the script:
```bash
python Challenge8.py
```

**Output:**
- Prints the vocabulary size.
- Shows tokenization examples for words.

**Example Output:**
```text
Vocabulary Size: ~1000

WordPiece Tokenization Examples:

unhappiness → ['u', '##n', '##h', '##ap', '##p', '##in', '##ess']
playing football → ['pl', '##ay', '##ing', 'f', '##o', '##otball']
cryptocurrency → ['crypto', '##c', '##u', '##rr', '##en', '##c', '##y']
governnmentt → ['go', '##ver', '##n', '##n', '##m', '##en', '##t', '##t']
```
*(Note: Tokenization splits may vary based on the training dataset size and content)*

### Challenge 9: Tokenization Comparison
Demonstrates and compares different tokenization techniques: Whitespace, BPE (Byte Pair Encoding), and WordPiece.

**Description:**
Uses the `tokenizers` library to tokenize a sample text using three different methods:
1.  **Whitespace Tokenization**: Simple splitting by whitespace.
2.  **BPE Tokenization**: Subword tokenization using Byte Pair Encoding.
3.  **WordPiece Tokenization**: Subword tokenization using the WordPiece algorithm (used in BERT).

**Usage:**
Prerequisites:
```bash
pip install tokenizers
```

Run the script:
```bash
python Challenge9.py
```

**Example Output:**
```text
Input Text:
 Cryptocurrency markets are experiencing high volatility in 2024 ...

1️⃣ Whitespace Tokenization:
['Cryptocurrency', 'markets', 'are', 'experiencing', 'high', 'volatility', 'in', '2024', 'as', 'global', 'investors', 'react', 'to', 'economic', 'uncertainty', 'and', 'rapid', 'technological', 'innovation.']
Token Count: 19

2️⃣ BPE Tokenization:
['Cry', 'pt', 'oc', 'ur', 're', 'nc', 'y', 'mark', 'ets', 'are', 'ex', 'per', 'i', 'enc', 'ing', 'high', 'vol', 'at', 'il', 'ity', 'in', '20', '24', 'as', 'gl', 'ob', 'al', 'in', 've', 'st', 'ors', 're', 'act', 'to', 'ec', 'on', 'om', 'ic', 'un', 'ce', 'rt', 'ai', 'nt', 'y', 'and', 'rap', 'id', 'te', 'ch', 'no', 'lo', 'gi', 'cal', 'in', 'no', 'va', 'tion', '.']
Token Count: 58

3️⃣ WordPiece Tokenization:
['Cry', '##pt', '##oc', '##ur', '##re', '##nc', '##y', 'mar', '##ke', '##ts', 'are', 'ex', '##pe', '##ri', '##en', '##ci', '##ng', 'high', 'vo', '##la', '##ti', '##li', '##ty', 'in', '202', '##4', 'as', 'glo', '##ba', '##l', 'in', '##ve', '##st', '##or', '##s', 're', '##ac', '##t', 'to', 'ec', '##on', '##om', '##ic', 'un', '##ce', '##rt', '##ai', '##nt', '##y', 'and', 'ra', '##pi', '##d', 'te', '##ch', '##no', '##lo', '##gi', '##ca', '##l', 'in', '##no', '##va', '##ti', '##on', '.']
Token Count: 66
```

## 📂 Project Structure

- `Challenge1.py`: User details script.
- `Challenge2.py`: Tokenization script.
- `Challenge3.py`: Stemming vs Lemmatization script.
- `Challenge4.py`: Stopwords removal script.
- `Challenge5.py`: News dataset cleaning script.
- `Challenge6.py`: Word frequency visualization script.
- `Challenge8.py`: WordPiece tokenization script (Hugging Face).
- `Challenge9.py`: Tokenization comparison script (Whitespace, BPE, WordPiece).
- `news_dataset.csv`: Sample dataset for Challenge 5, 6 & 8.
- `top_20_words.png`: Generated plot from Challenge 6.
- `README.md`: Project documentation.
