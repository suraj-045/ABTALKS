import pandas as pd
from tokenizers import Tokenizer
from tokenizers.models import WordPiece
from tokenizers.trainers import WordPieceTrainer
from tokenizers.pre_tokenizers import Whitespace

# STEP 1: Read the CSV dataset (same as Day 5 & 6)
df = pd.read_csv("news_dataset.csv", engine="python")

# STEP 2: Combine title and content
df["text"] = df["title"].fillna("") + " " + df["content"].fillna("")

# STEP 3: Create corpus (THIS is where CSV is used)
corpus = df["text"].astype(str).tolist()

# STEP 4: Initialize WordPiece tokenizer
tokenizer = Tokenizer(WordPiece(unk_token="[UNK]"))
tokenizer.pre_tokenizer = Whitespace()

# STEP 5: Train WordPiece tokenizer on corpus
trainer = WordPieceTrainer(
    vocab_size=2000,
    special_tokens=["[UNK]"]
)

tokenizer.train_from_iterator(corpus, trainer)

# STEP 6: Print vocabulary size (MANDATORY)
print("Vocabulary Size:", len(tokenizer.get_vocab()))

# STEP 7: Show tokenization examples (MANDATORY)
examples = [
    "unhappiness",
    "playing football",
    "cryptocurrency",
    "governnmentt"
]

print("\nWordPiece Tokenization Examples:\n")
for text in examples:
    print(text, "→", tokenizer.encode(text).tokens)