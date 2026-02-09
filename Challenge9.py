from tokenizers import Tokenizer
from tokenizers.models import BPE, WordPiece
from tokenizers.trainers import BpeTrainer, WordPieceTrainer
from tokenizers.pre_tokenizers import Whitespace

# INPUT TEXT (Bigger)

text = ( "Cryptocurrency markets are experiencing high volatility in 2024 "
    "as global investors react to economic uncertainty and rapid " "technological innovation.")

print("Input Text:\n", text)
print("\n" + "="*60)

# 1️⃣ WHITESPACE TOKENIZATION
whitespace_tokens = text.split()

print("1️⃣ Whitespace Tokenization:")
print(whitespace_tokens)
print("Token Count:", len(whitespace_tokens))
print("\n" + "="*60)

# 2️⃣ BPE TOKENIZATION

bpe_tokenizer = Tokenizer(BPE(unk_token="[UNK]"))
bpe_tokenizer.pre_tokenizer = Whitespace()

bpe_trainer = BpeTrainer(vocab_size=200)
bpe_tokenizer.train_from_iterator([text], bpe_trainer)

bpe_tokens = bpe_tokenizer.encode(text).tokens

print("2️⃣ BPE Tokenization:")
print(bpe_tokens)
print("Token Count:", len(bpe_tokens))
print("\n" + "="*60)

# 3️⃣ WORDPIECE TOKENIZATION
wp_tokenizer = Tokenizer(WordPiece(unk_token="[UNK]"))
wp_tokenizer.pre_tokenizer = Whitespace()

wp_trainer = WordPieceTrainer(vocab_size=200)
wp_tokenizer.train_from_iterator([text], wp_trainer)

wp_tokens = wp_tokenizer.encode(text).tokens

print("3️⃣ WordPiece Tokenization:")
print(wp_tokens)
print("Token Count:", len(wp_tokens))
print("\n" + "="*60)