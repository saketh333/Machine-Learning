#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.

    Use a SVM to identify emails from the Enron corpus by their authors:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess

from sklearn.svm import SVC

#clf = SVC(kernel ='linear')#using kernel linear
clf = SVC(kernel ='rbf', C = 10000) #using kernel rbf


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
#features_train = features_train[:len(features_train)/100] 
#labels_train = labels_train[:len(labels_train)/100] 
t = time()
clf.fit(features_train, labels_train)
print ("Training Time {}".format(t - time()))
t1 = time()
print clf.score(features_test, labels_test)
print ("Predicting Time {}".format(t1 - time()))
predictions =  clf.predict(features_test)
print predictions[10],predictions[26],predictions[50]
print sum(predictions)
print sum(labels_test)