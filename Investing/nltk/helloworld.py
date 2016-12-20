from nltk.tokenize import sent_tokenize,word_tokenize

# nltk.download()

# Tokenizing - Word tokenizer...sentence tokenizers
# Lexicon and corporas
# Corpora = body of text. E.g: Medical journal,presidential speeches,English language
# Lexicon = dictionary, words and their meanings

# Investor-speak...regular english-speak

# Investors speak 'bull' = someone who is positive about the market
# As opposed to English speak as 'bull' -- Scary animal you don't want running at you

example_text = 'Hello Mr.Smith, how are you doing today? The weather is great and python is awesome. The sky is pinkish blue. You should not be cardboard.'

# print(sent_tokenize(example_text))
# print(word_tokenize(example_text))


for i in word_tokenize(example_text):
	print i