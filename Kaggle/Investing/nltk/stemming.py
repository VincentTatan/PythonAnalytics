from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

ps = PorterStemmer()
# Very redundant and very inefficient to just store the word
# I was taking a ride in the car
# I was riding in the car
example_words = ["python","pythonning","pythoner","pythoned","pythoniy"]

# for w in example_words:
# 	print(ps.stem(w))

new_text = "It is very important to be pythoniy while you are pythoning with python. All pythoner has been pythoning at least once."
words = word_tokenize(new_text)

for w in words:
	print(ps.stem(w))
