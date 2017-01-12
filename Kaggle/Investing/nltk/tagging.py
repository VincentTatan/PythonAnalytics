import nltk
from nltk.corpus import state_union
from nltk.tokenize import PunktSentenceTokenizer
# Stopwords
# stemming
# tagging/tokenization; Part of speech tuples
# Chunking/ Chinking: Grouping words as one meaning. Chinking: Leave out chunks in chunk 
# Named Entity Recognition: Chunking with more named entity lexicon
# Wordnet: Lexicon list and relevance of words(similarity, antonym,synonym)
# Text Classification : Spam, sentimental analysis
# POS tag list:

# CC	coordinating conjunction
# CD	cardinal digit
# DT	determiner
# EX	existential there (like: "there is" ... think of it like "there exists")
# FW	foreign word
# IN	preposition/subordinating conjunction
# JJ	adjective	'big'
# JJR	adjective, comparative	'bigger'
# JJS	adjective, superlative	'biggest'
# LS	list marker	1)
# MD	modal	could, will
# NN	noun, singular 'desk'
# NNS	noun plural	'desks'
# NNP	proper noun, singular	'Harrison'
# NNPS	proper noun, plural	'Americans'
# PDT	predeterminer	'all the kids'
# POS	possessive ending	parent's
# PRP	personal pronoun	I, he, she
# PRP$	possessive pronoun	my, his, hers
# RB	adverb	very, silently,
# RBR	adverb, comparative	better
# RBS	adverb, superlative	best
# RP	particle	give up
# TO	to	go 'to' the store.
# UH	interjection	errrrrrrrm
# VB	verb, base form	take
# VBD	verb, past tense	took
# VBG	verb, gerund/present participle	taking
# VBN	verb, past participle	taken
# VBP	verb, sing. present, non-3d	take
# VBZ	verb, 3rd person sing. present	takes
# WDT	wh-determiner	which
# WP	wh-pronoun	who, what
# WP$	possessive wh-pronoun	whose
# WRB	wh-abverb	where, when

# NE Type and Examples
# ORGANIZATION - Georgia-Pacific Corp., WHO
# PERSON - Eddy Bonte, President Obama
# LOCATION - Murray River, Mount Everest
# DATE - June, 2008-06-29
# TIME - two fifty a m, 1:30 p.m.
# MONEY - 175 million Canadian Dollars, GBP 10.40
# PERCENT - twenty pct, 18.75 %
# FACILITY - Washington Monument, Stonehenge
# GPE - South East Asia, Midlothian

train_text = state_union.raw("2005-GWBush.txt")
example_text = state_union.raw("2006-GWBush.txt")
custom_sent_tokenizer = PunktSentenceTokenizer(train_text)

tokenized = custom_sent_tokenizer.tokenize(example_text)

def process_content():
	try:
		for i in tokenized:
			words=nltk.word_tokenize(i)
			tagged=nltk.pos_tag(words)

			# Chunking and chinking
 		# 	chunkGram = r"""Chunk: {<.*>+}
   #                                  }<VB.?|IN|DT|TO>+{"""			chunkParser = nltk.RegexpParser(chunkGram)
			# chunked = chunkParser.parse(tagged)
			# chunked.draw()
 			namedEnt = nltk.ne_chunk(tagged, binary=True)
 			namedEnt.draw()

	except Exception as e:
		print(str(e))

process_content()