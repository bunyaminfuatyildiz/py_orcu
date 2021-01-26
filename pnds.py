# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 18:13:23 2021

@author: bunya
"""
  # pandas: Data Manipulation
import pandas as pd
df2 = pd.DataFrame({'Names': ['Simon', 'Kate', 'Francis', 'Laura', 'Mary', 'Julian', 'Rosie', 'Simon', 'Laura'],
                      'Height':[180, 165, 170, 164, 163, 175, 166, 180, 164],
                        'Weight':[85, 65, 68, 45, 43, 72, 46, 85, 45],
                          'Pref_food': ['steak', 'pizza', 'pasta', 'pizza', 'vegetables', 'steak', 'seafood', 'steak', 'pizza'],
                          'Sex': ['m','f','m','f','f','m','f', 'm', 'f']})


"Starting with the ‘Sex’ variable, let’s create two dummy variables and continue with pandas:"
df_dummy = pd.get_dummies(df2['Sex'], prefix = 'Sex')

#At this point, we can join these two dummy variables to the  original dataset: 
df2.join(df_dummy)
#Now let’s remove the original ‘Sex’ variable:
del df2['Sex']
 df2.duplicated()
 df2.drop_duplicates()
df3 = df2.drop_duplicates()
df2.drop(2)
df3.stack()
 stacked = df3.stack()
# and now we can return it to its original format using 
unstacked = stacked.unstack()
print(unstacked)
pd.melt(df3)
df2.head(2)

# we invert rows and columns
 df2.T
 
 import numpy as np
 np.random.seed(1)
""" Instead of extracting a number of cases, we can extract a percentage, 
with the argument frac= instead of n="""
df2.sample(frac = .1)
df2.sample(frac = .5) 
df3.nlargest(3, "Weight") 
df3.nsmallest(4, "Weight") 




####  pandas: Missing Values
df_missing = pd.read_csv('df_missing.csv')
df_missing
 print(df_missing.shape) 
  print(df_missing.dropna().shape)
pd.isnull(df_missing) 
 df_missing.isnull().sum()
# or determine the total of missing data
df_missing.isnull().sum().sum()
#To perform a deletion, proceed as follows:
df_missing.dropna() 
#We eliminated the lines containing missing values. We can also delete  THe  columns with missing values:
df_missing.dropna(axis = 1, how = 'any') 
df_missing.fillna(0) 
df_missing.fillna('missing')
"""Let’s consider a variable, such as variable ‘C’. The following line of code 
will replace every missing value in the variable C with the mean of C:"""
df_missing['C'].fillna(df_missing['C'].mean())

"""Two important .fillna methods can be used to impute missing values: 
ffill and backfill"""
df_missing['C'].fillna(method = 'ffill')
df_missing['C'].fillna(method = 'backfill')


####pandas: Merging Two Datasets 
""""To merge more than 
two datasets, we can use .concat():?"""
pd.concat([df1, df2, df3]) 
# by default, the merge() function extracts common cases to the two datasets, so it is 'inner' by default. Inner join selects records that have matching values in both datasets 
  #### pandas: Basic Statistics
  
  
df = pd.DataFrame({'Names': ['Simon', 'Kate', 'Francis', 'Laura', 'Mary', 'Julian', 'Rosie', 'Simon', 'Laura'],
                      'Height':[180, 165, 170, 164, 163, 175, 166, 180, 164],
                        'Weight':[85, 65, 68, 45, 43, 72, 46, 85, 45],
                          'Pref_food': ['steak', 'pizza', 'pasta', 'pizza', 'vegetables', 'steak', 'seafood', 'steak', 'pizza'],
                          'Sex': ['m','f','m','f','f','m','f', 'm', 'f']})
 
df.describe() 
df.describe().transpose() 
# value counts
df.count()
# median calculation
>>> df['Height'].median() 
 
 
 
 