# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 22:57:01 2017

@author: Saketh
"""
#!/usr/bin/python

import matplotlib.pyplot as plt
from prep_terrain_data import makeTerrainData
from class_vis import prettyPicture
#from sklearn.ensemble import AdaBoostClassifier, RandomForestClassifier
#from sklearn import tree                         
from time import time
#from sklearn.naive_bayes import GaussianNB
#from sklearn.model_selection import cross_val_score
#from sklearn.datasets import make_blobs
#from sklearn.ensemble import ExtraTreesClassifier
#from sklearn.tree import DecisionTreeClassifier
from sklearn import neighbors

features_train, labels_train, features_test, labels_test = makeTerrainData()



clf= neighbors.KNeighborsClassifier(algorithm="auto",n_neighbors=8,weights='uniform',p=1)
time0= time()
clf.fit(features_train,labels_train)


print "accuracy:", clf.score(features_test, labels_test)


try:
    prettyPicture(clf, features_test, labels_test)
except NameError:
    pass