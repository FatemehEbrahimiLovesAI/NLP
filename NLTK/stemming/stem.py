from nltk.stem import PorterStemmer

# Create an object of the PorterStemmer class
stemmer = PorterStemmer()

# The words we want to be stemmed
words = ["angrier", "happier","studing","harder","cooking","farther"]

# We stem the words and put them in another list
stemmed_words = [stemmer.stem(word )for word in words]

# we can print them
print("our original words: ", words)
print("our stemmed words: ",stemmed_words)
