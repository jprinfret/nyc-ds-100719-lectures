#!/usr/bin/env python
# coding: utf-8

# In[21]:


import pandas as pd
import numpy as np
from sklearn import metrics
import time
import os
import glob
import re


# In[14]:


#read in the answers
answers = pd.read_csv('test_actuals.csv', index_col = 0, header=None, names=['Genres'] )


# In[ ]:


# create a list of all file names
# starting with testlabels_ from the file


# In[33]:



path = '/Users/swilson5/Documents/DSC/ds-100719/nyc-ds-100719-lectures/week-11/NLP/classification-assessment/answers'
extension = 'csv'
os.chdir(path)
files = glob.glob('*.{}'.format(extension))
print(files)


# In[35]:


#create dictionary to store results
results = {}


# In[ ]:


# loop over the list read the file, and score the answers


# In[36]:


for file in files:
    name = file.split("_")[-1].split(".")[0]
    print(name)
    guesses = pd.read_csv(file, index_col=0, header=None )
    guesses.sort_index(inplace=True)

    if guesses.shape[0] != 3561:
        print(name, "not the correct size", guesses.shape[0]  )
        # continue
    score = metrics.f1_score(answers,guesses, average='weighted')
    acc = metrics.accuracy_score(answers,guesses)
    results[name]= [score, acc]


# In[46]:


sorted_results = sorted(results.items(), key=lambda x: x[1][0])

print('Now printing the results with in ascending order')
# In[50]:
time.sleep(10)

for k,v in sorted_results:
#     print(k,v)
    print('{} achieved an F1 score of {} and an accuracy score of {} \n'.format(
          k.upper(), v[0], v[1]))

    time.sleep(2)
