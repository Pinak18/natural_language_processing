# -*- coding: utf-8 -*-
"""Text Preprocessing - NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1czv2gug9yj4vgBnpyadGS8isOliZ_sn2

# Text Preprocessing - NLP
"""

# !pip install nltk

"""### Step 1: Import Necessary Libraries"""

import nltk
nltk.download('punkt')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import string
import warnings
warnings.filterwarnings("ignore")

"""### Step 2: Sample Text"""

text = "This is a simple example: we're going to preprocess this text, removing stopwords and punctuation. We removed and done with preprocessing!"

"""### Step 3: Punctuation Removal"""

print(string.punctuation)

text = "".join([i for i in text if i not in string.punctuation])
text

"""### Step 4: Lowering the Text"""

text = text.lower()
text

"""### Step 5: Tokenization
#### In this step, the text is split into smaller units.
"""

words = word_tokenize(text)
print(words)

"""### Step 6: Stop Words Removal"""

nltk.download('stopwords')

stop_words = set(stopwords.words('english'))
print(stop_words)
print(len(stop_words))

filtered_words = [word for word in words if word not in stop_words]
print(filtered_words)

"""### Stemming:
### It is also known as the text standardization step where the words are stemmed or diminished to their root/base form.
"""

#from nltk.stem.porter import PorterStemmer
#porter_stemmer = PorterStemmer()

stem_text = [porter_stemmer.stem(word) for word in filtered_words]
print(stem_text)

"""### Lemmatization:
#### It stems the word but makes sure that it does not lose its meaning.  Lemmatization has a pre-defined dictionary that stores the context of words and checks the word in the dictionary while diminishing.
"""

from nltk.stem import WordNetLemmatizer
wordnet_lemmatizer = WordNetLemmatizer()

lemm_text = [wordnet_lemmatizer.lemmatize(word) for word in filtered_words]
print(lemm_text)

"""### Step 7: Print Results"""

print("Original Text:")
print(text)

print("\nTokenized Text:")
print(words)

print("\nCleaned and Stop Words Removed:")
print(filtered_words)

print("\nStemmed Text:")
print(stem_text)

