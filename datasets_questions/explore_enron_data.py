#!/usr/bin/python

""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).

    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }

    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:

    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle
import os

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "r"))

print len(enron_data) # count no of people in the data or keys

print len(enron_data['METTS MARK']) # No of features per person

# count person of interest in data
x = 0 
for names in enron_data:
    if enron_data[names]["poi"]==1:
        x += 1

print (x)

# to see how the names are printed
#for key, value in enron_data.iteritems():
#    print key
    
# stock value of james prentice
print enron_data['PRENTICE JAMES']['total_stock_value']        

# HOW MANY MESSAGES FROM WESLEY COLWELL TO POI
print enron_data['COLWELL WESLEY']['from_this_person_to_poi']     
       

print enron_data['SKILLING JEFFREY K']

salary  = 0
email = 0
for names in enron_data:
    if enron_data[names]['salary']!= 'NaN':
        salary += 1
    if enron_data[names]['email_address']!= 'NaN':
        email +=1
print "Quantified salary, emails {} {}".format(salary,email)

# how many people have nan for total_payments
total_payments = 0
count_no = 0
for names in enron_data:
    if enron_data[names]['total_payments'] == 'NaN':
        total_payments  += 1
    count_no += 1 
print count_no    
print "what percentage of people in whole have nan for total_payments {}".format(total_payments)
poi = 0
poi_total_payments = 0
for names in enron_data:
    if enron_data[names]['poi'] == True:
       poi += 1
       if enron_data[names]['total_payments'] == 'NaN':
           poi_total_payments += 1 

print poi, poi_total_payments        





# change working directory
os.chdir("C:/Users/Saketh/DA/Machine_learning/version-control/ud120-projects/final_project")

# open text file
f = open("poi_names.txt", "r")

# count no of lines in the file
print len(f.readlines())
