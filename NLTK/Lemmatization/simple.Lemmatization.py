from nltk.stem import WordNetLemmatizer

words = ["studying","cooking","frustrated","looked","made"]

lemmatizer = WordNetLemmatizer()

lemmatized_words = [lemmatizer.lemmatize(word,pos='v') for word in words]

print("original words : ",words)
print("lemmatized words : ", lemmatized_words)
