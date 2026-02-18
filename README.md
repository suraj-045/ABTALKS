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

### Challenge 10: Feature Extraction (BoW & TF-IDF)
Demonstrates text feature extraction techniques using Scikit-Learn.

**Description:**
Converts a collection of text documents into numerical matrices using:
1.  **Bag of Words (BoW)**: Counts word occurrences using `CountVectorizer`.
2.  **TF-IDF**: Weighs words based on their frequency in a document vs. the corpus using `TfidfVectorizer`.

**Usage:**
Prerequisites:
```bash
pip install scikit-learn
```

Run the script:
```bash
python Challenge10.py
```

**Example Output:**
```text
Documents:
AI is helpful
AI AI makes work easy
Blockchain improves security
The system is running fast

--- Bag of Words ---
Words: ['ai' 'blockchain' 'easy' 'fast' 'helpful' 'improves' 'is' 'makes' 'running' 'security' 'system' 'the' 'work']
[[1 0 0 0 1 0 1 0 0 0 0 0 0]
 [2 0 1 0 0 0 0 1 0 0 0 0 1]
 ... ]

--- TF IDF ---
Words: ['ai' 'blockchain' 'easy' 'fast' 'helpful' 'improves' 'is' 'makes' 'running' 'security' 'system' 'the' 'work']
[[0.52 0.   0.   0.   0.66 ... ]
 ... ]
```

### Challenge 11: TF-IDF & Cosine Similarity
Demonstrates how to compute the similarity between two text documents using TF-IDF (Term Frequency-Inverse Document Frequency) and Cosine Similarity.

**Description:**
Calculates the cosine similarity score between two documents to determine how similar they are based on their content.

**Usage:**
Prerequisites:
```bash
pip install scikit-learn
```

Run the script:
```bash
python Challenge11.py
```

**Example Output:**
```text
Document 1:
 Machine learning models help companies analyze large amounts of data to find patterns, make predictions, and improve business decisions.

Document 2:
 Data science uses algorithms and statistical techniques to study datasets, discover insights, and support smarter decision making in organizations.

-----------------------------
Cosine Similarity Score:
0.11391496598792124
```

### Challenge 12: Simple Text Pipeline
Demonstrates a basic text processing pipeline that performs lowercasing, punctuation removal, tokenization, and stopword removal.

**Description:**
A simple pipeline function that takes a raw string, cleans it by removing non-alphabetic characters and stopwords, and returns a list of tokens.

**Usage:**
Prerequisites:
```bash
pip install nltk
```

Run the script:
```bash
python Challenge12.py
```

**Example Output:**
```text
Original: Why is AI amazing!
Output: ['ai', 'amazing']

Original: Machine learning helps automation.
Output: ['machine', 'learning', 'helps', 'automation']

Original: The system is running fast.
Output: ['system', 'running', 'fast']
```

### Challenge 13: Spam vs Ham Preprocessing
Demonstrates a text preprocessing pipeline applied to example spam and ham (non-spam) messages.

**Description:**
Applies lowercasing, symbol/number removal, tokenization, and stopword removal to a set of example messages to prepare them for potential classification.

**Usage:**
Prerequisites:
```bash
pip install nltk
```

Run the script:
```bash
python Challenge13.py
```

**Example Output:**
```text
Original: WIN MONEY NOW!!! Click this link to claim prize
Processed: ['win', 'money', 'click', 'link', 'claim', 'prize']

Original: Hey bro, are we meeting today?
Processed: ['hey', 'bro', 'meeting', 'today']

Original: FREE offer just for you!!!
Processed: ['free', 'offer']

Original: Let's finish our assignment tonight
Processed: ['lets', 'finish', 'assignment', 'tonight']
```

### Challenge 14: NLP Pipeline & Feature Extraction
A comprehensive script combining text cleaning, tokenization, word frequency analysis, and feature extraction (BoW & TF-IDF).

**Description:**
Demonstrates a full NLP workflow:
1.  **Cleaning & Tokenizing**: Lowercasing, removing non-alphabetic characters, and removing stopwords.
2.  **Word Frequency**: Counting occurrences of each word.
3.  **Feature Extraction**: Generating Bag of Words (BoW) and TF-IDF matrices.
4.  **Pipeline Function**: A reusable function for text preprocessing.

**Usage:**
Prerequisites:
```bash
pip install nltk scikit-learn
```

Run the script:
```bash
python Challenge14.py
```

**Example Output:**
```text
Cleaned Words:
['ai', 'rapidly', 'transforming', 'modern', 'industries', ...]

Word Frequency:
Counter({'data': 2, 'ai': 1, 'rapidly': 1, ...})

BoW Words:
['adapt' 'ai' 'analysis' 'and' ... ]
[[1 1 1 3 ... ]]

TF-IDF Words:
['adapt' 'ai' 'analysis' 'and' ... ]
[[0.12 0.12 0.12 0.36 ... ]]

Pipeline Test:
['machine', 'learning', 'helps', 'ai', 'systems']
```

### Challenge 15: Simple Word Embeddings
Demonstrates basic word embedding operations using NumPy, including creating a manual embedding matrix, calculating dot products, and computing cosine similarity.

**Description:**
Uses a manually defined embedding matrix to represent sentences/words and explores vector operations:
1.  **Embedding Matrix**: A small manual example of word embeddings.
2.  **Dot Product**: Calculates the dot product of the matrix with its transpose.
3.  **Cosine Similarity**: Computes similarity between the vectors.
4.  **Mean Embedding**: Calculates the average vector of the embeddings.

**Usage:**
Prerequisites:
```bash
pip install numpy
```

Run the script:
```bash
python Challenge15.py
```

**Example Output:**
```text
Embedding Matrix:
[[0.8 0.2 0.6]
 [0.7 0.3 0.5]
 [0.2 0.9 0.4]]

...

Cosine Similarity Matrix:
[[1.         0.99022095 0.56591426]
 [0.99022095 1.         0.66623908]
 [0.56591426 0.66623908 1.        ]]

Mean Embedding:
[0.56666667 0.46666667 0.5       ]
```

### Challenge 16: Matrix Multiplication for Embeddings
Demonstrates matrix operations commonly used in Deep Learning, specifically dot products and matrix multiplication with embeddings using NumPy.

**Description:**
Performs matrix multiplication on a manually defined embedding matrix to show relationships between vectors.
1.  **Embedding Matrix**: A small manual example of word embeddings.
2.  **Dot Product**: Calculates the dot product between two specific vectors.
3.  **Matrix Multiplication**: Multiplies the embedding matrix by its transpose ($A \cdot A^T$) to compute similarities between all pairs of vectors.

**Usage:**
Prerequisites:
```bash
pip install numpy
```

Run the script:
```bash
python Challenge16.py
```

**Example Output:**
```text
Embedding Matrix:
[[0.8 0.2 0.6]
 [0.7 0.3 0.5]
 [0.2 0.9 0.4]]

Matrix Shape:
(3, 3)

Dot Product (Vector 1 · Vector 2):
0.9199999999999999

Matrix Multiplication Result:
[[1.04 0.92 0.58]
 [0.92 0.83 0.61]
 [0.58 0.61 1.01]]
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
- `Challenge10.py`: Bag of Words and TF-IDF feature extraction script.
- `Challenge11.py`: TF-IDF & Cosine Similarity script.
- `Challenge12.py`: Simple Text Pipeline script.
- `Challenge13.py`: Spam vs Ham Preprocessing script.
- `Challenge14.py`: NLP Pipeline & Feature Extraction script.
- `Challenge15.py`: Simple Word Embeddings script.
- `Challenge16.py`: Matrix Multiplication for Embeddings script.
- `news_dataset.csv`: Sample dataset for Challenge 5, 6 & 8.
- `top_20_words.png`: Generated plot from Challenge 6.
- `README.md`: Project documentation.
