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

## 📂 Project Structure

- `Challenge1.py`: User details script.
- `Challenge2.py`: Tokenization script.
- `README.md`: Project documentation.
