#!/usr/bin/python

""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.

    Use a Decision Tree to identify emails from the Enron corpus by author:    
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
from sklearn import tree


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

clf = tree.DecisionTreeClassifier(min_samples_split = 40)
t = time()
clf = clf.fit(features_train, labels_train) # fitting model
print ("training_time{}".format(t - time()))
t1 = time()
print (clf.score(features_test,labels_test)) # testing accuracy
print ("testing_time {}".format(t1 - time())) 

#print (features_train.shape) No of features in the model