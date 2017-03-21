import os
import sys
import argparse
import json

from sklearn.datasets import load_files
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import Pipeline


# Loads corpus directory path into a Sci-Kit-Learn Dataset
def loadDS(path):
    dataset = load_files(path)
    docs = []
    for raw_data in dataset.data:
        docs.append(raw_data)
    dataset.data = docs
    categories = dataset.target_names
    print('From {:s}:\n{:d} Docs in {:d} categories:\n{:s}\n\n'.format(
        path,
        len(dataset.data),
        len(categories),
        ', '.join(categories))
    )
    return dataset


# Travel dataset loading for training
travelDS = loadDS('/ml/resources/corpus/travel/train')

# Build token count matrix
countVect = CountVectorizer()
travelTokenCountMatrix = countVect.fit_transform(travelDS.data)
#print X_train_counts.shape
#print countVect.vocabulary_.get(u'plage')

# Term Frequency times Inverse Document Frequency
tfidfTransformer = TfidfTransformer()
travelTfidf = tfidfTransformer.fit_transform(travelTokenCountMatrix)
#print X_train_tfidf.shape

# Build a naiv Bayes classifier for the travel DS
naiveBayesMultinomial = MultinomialNB()
clf = naiveBayesMultinomial.fit(travelTfidf, travelDS.target)


# Test dataset
testDS = ['Je veux partir en amoureux',
        'Je veux de belles plages', 
        'je suis trop stresse',
        'je veux me ressourcer en nature',
        'je reve de nager avec des requins']
testTokenCount = countVect.transform(testDS)
testTfidf = tfidfTransformer.transform(testTokenCount)

# Test classification
testPredicted = clf.predict(testTfidf)

# Results
for travelTestSentence, predictedCategory in zip(testDS, testPredicted):
    print('%r => %s' % (travelTestSentence, travelDS.target_names[predictedCategory]))
