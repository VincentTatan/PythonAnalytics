from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()

# A very similar operation to stemming is called lemmatizing. The major difference between these is, as you saw earlier, stemming can often create non-existent words, whereas lemmas are actual words.

# Better to do stemming. with configuration setting for type of speech
print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("goose"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("better",pos='a'))
print(lemmatizer.lemmatize("best",pos='a'))

print(lemmatizer.lemmatize("run"))
print(lemmatizer.lemmatize("run",pos='v'))
