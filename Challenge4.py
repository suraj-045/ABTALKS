import re
import nltk
from nltk.corpus import stopwords 
from nltk.tokenize import word_tokenize
nltk.download('punkt')
nltk.download('stopwords')

#Noisy text
text = """ OMG this movie was sooo goood!!! 😍😍 I can't even explain how I felt!!
Totally worth watching even @night. But the audio was like sooo bad???!
Check it: http://tinyurl.com/xyz123 <br><br>
BTW I watched it 2x and still wanna watch again!!!"""

#Step 1:Convert to Lowercase
text = text.lower()

#Step 2: Remove punctuation and numbers
text = re.sub(r'[^a-z\s]', '',text)

#Step 3: Tokenization
words = word_tokenize(text)

#Step 4: Remove stopwords
stop_words = set(stopwords.words('english'))
clean_words = [word for word in words if word not in stop_words]

#Step 5:Join words back into text
clean_text = " ".join(clean_words)

#Output
print("Cleaned Text:")
print(clean_text)