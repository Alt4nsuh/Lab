import nltk
nltk.download('words')
from nltk.corpus import words as nltk_words

# Show some words from the NLTK corpus
print(len(nltk_words.words()[20:]))  # Displaying the first 20 words
