
import nltk
import random
from nltk.corpus import movie_reviews
from nltk.classify.scikitlearn import SklearnClassifier
import pickle

from sklearn.naive_bayes import MultinomialNB, GaussianNB, BernoulliNB 
from sklearn.linear_model import LogisticRegression,SGDClassifier
from sklearn.svm import SVC,LinearSVC,NuSVC

from nltk.classify import ClassifierI
from nltk.tokenize import word_tokenize
from statistics import mode
class VoteClassifier(ClassifierI):
	def __init__(self,*classifiers):
		self._classifiers = classifiers
	def classify():
		votes=[]
		for c in self._classifiers:
			v=c.classify(features)
			votes.append(v)
		return mode(votes)
	def confidence(self,features):
		votes=[]
		for c in self._classifiers:
			v = c.classify(features)
			votes.append(v)
		choice_votes=votes.count(mode(votes))
		conf = choice_votes/len(votes)
		return conf

# Classify the number of support vector
documents = [(list(movie_reviews.words(fileid)),category)
				for category in movie_reviews.categories()
				for fileid in movie_reviews.fileids(category)]

random.shuffle(documents)
# print(documents[1])

short_pos = open("positive.txt","r").read().decode('utf-8','ignore')
short_neg = open("negative.txt","r").read().decode('utf-8','ignore')


for r in short_pos.split('\n'):
    documents.append( (r, "pos") )
    print(r)

for r in short_neg.split('\n'):
    documents.append( (r, "neg") )
    
# documents = []
# for category in moview_reviews_categories():
# 	for fileid in movie_reviews.fileids():
# 		documents.append(list(movie_reviews.words(fileid)),category)


all_words=[]
short_pos_words = word_tokenize(short_pos)
short_neg_words = word_tokenize(short_neg)

for w in short_pos_words:
	all_words.append(w.lower())
for w in short_neg_words:
	all_words.append(w.lower())

for w in movie_reviews.words():
	all_words.append(w.lower())

all_words = nltk.FreqDist(all_words)
# print(all_words.most_common(15))
# print(all_words("stupid"))

word_features = list(all_words.keys())[:5000]

# Find out which one is positive or negative
def find_features(document):
	words = word_tokenize(document)
	features = {}
	for w in word_features:
		features[w]=(w in words)
	return features


# print((find_features(movie_reviews.words('neg/cv000_29416.txt'))))

featuresets = [(find_features(rev),category) for (rev,category) in documents]
random.shuffle(featuresets)
# Positive data exampler
training_set =featuresets[:10000]
testing_set =featuresets[10000:]

# Negative data exampler (to see if there is a bias)
# training_set =featuresets[100:]
# testing_set =featuresets[:100]

classifier_f = open('naivebayes.pickle','rb')
classifier = pickle.load(classifier_f)
classifier_f.close()


# We save the training classifier at pickle to save time
# classifier = nltk.NaiveBayesClassifier.train(training_set)
print("Original Naive Bayes Algo Accuracy",(nltk.classify.accuracy(classifier,testing_set))*100)
classifier.show_most_informative_features(15)

# Write pickle
# save_classifier = open('naivebayes.pickle','wb')
# pickle.dump(classifier,save_classifier)
# save_classifier.close()


MNB_classifier = SklearnClassifier(MultinomialNB())
MNB_classifier.train(training_set)
print("MNB_classifier Algo Accuracy",(nltk.classify.accuracy(MNB_classifier,testing_set))*100)
# GaussianNB_classifier = SklearnClassifier(GaussianNB())
# GaussianNB_classifier.train(training_set)
# print("GaussianNB_classifier Algo Accuracy",(nltk.classify.accuracy(GaussianNB_classifier,testing_set))*100)
BernoulliNB_classifier = SklearnClassifier(BernoulliNB())
BernoulliNB_classifier.train(training_set)
print("BernoulliNB_classifier Algo Accuracy",(nltk.classify.accuracy(BernoulliNB_classifier,testing_set))*100)

# LogisticRegression,SGDClassifier
# SVC,LinearSVC,NuSVC
LogisticRegression_classifier = SklearnClassifier(LogisticRegression())
LogisticRegression_classifier.train(training_set)
print("LogisticRegression_classifier Algo Accuracy",(nltk.classify.accuracy(LogisticRegression_classifier,testing_set))*100)
SGDClassifier_classifier = SklearnClassifier(SGDClassifier())
SGDClassifier_classifier.train(training_set)
print("SGDClassifier_classifier Algo Accuracy",(nltk.classify.accuracy(SGDClassifier_classifier,testing_set))*100)
# eliminated cause too weak
# SVC_classifier = SklearnClassifier(SVC())
# SVC_classifier.train(training_set)
# print("SVC_classifier Algo Accuracy",(nltk.classify.accuracy(SVC_classifier,testing_set))*100)
LinearSVC_classifier = SklearnClassifier(LinearSVC())
LinearSVC_classifier.train(training_set)
print("LinearSVC_classifier Algo Accuracy",(nltk.classify.accuracy(LinearSVC_classifier,testing_set))*100)
NuSVC_classifier = SklearnClassifier(NuSVC())
NuSVC_classifier.train(training_set)
print("NuSVC_classifier Algo Accuracy",(nltk.classify.accuracy(NuSVC_classifier,testing_set))*100)

# Ending score, certainty of that score 

# voted_classifier = VoteClassifier(classifier,MNB_classifier,BernoulliNB_classifier,LogisticRegression_classifier,
# 	SGDClassifier_classifier,LinearSVC_classifier,NuSVC_classifier)

# print("voted_classifier accuracy percent:", (nltk.classify.accuracy(voted_classifier, testing_set))*100)

# print("Classification:", voted_classifier.classify(testing_set[0][0]), "Confidence %:",voted_classifier.confidence(testing_set[0][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[1][0]), "Confidence %:",voted_classifier.confidence(testing_set[1][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[2][0]), "Confidence %:",voted_classifier.confidence(testing_set[2][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[3][0]), "Confidence %:",voted_classifier.confidence(testing_set[3][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[4][0]), "Confidence %:",voted_classifier.confidence(testing_set[4][0])*100)
# print("Classification:", voted_classifier.classify(testing_set[5][0]), "Confidence %:",voted_classifier.confidence(testing_set[5][0])*100)
