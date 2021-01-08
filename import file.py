# -*- coding: utf-8 -*-
"""
Created on Fri Jan  8 07:51:12 2021
How to import data 
@author: bunya
"""
import os 
os.getcwd()
os.chdir("C:\\Users\\bunya\\python")

"""The basic structure for importing files is as follows:
file1 = open("file.name", mode)"""

# we open (or create) the file
file1 = open("file1.txt","w")
# at the moment, the file was created in our work directory but  it is empty
# we are in write mode; we then add text this way
file1.write("Add line n.1 to the file1")
# we close the file
file1.flush()
file1.close()

# we open the file in read mode
file1 = open("file1.txt", "r")
text1 = file1.read()
# we create an object that contains our file and display it with the print() function
text1 = file1.read()
print(text1)

# Add line 1 to file1
# we close the file
file1.close()
# we reopen the file in write mode
file1 = open("file1.txt","w")
# if we write the new text now, the line we had written  previously is replaced
file1.write("Let's replace the first line with this new one")
# we test
file1.flush()
file1.close()
file1 = open("file1.txt", "r")
text2 = file1.read()
print(text2)
#Let's replace the first line with this new one
file1.close()
# to add text without overwriting, we open the file in append mode
file1 = open("file1.txt", "a")
file1.write("\n Add a second line to this new version of the file")
file1.close()
file1 = open("file1.txt", "r")
text3 = file1.read()
print(text3)
# We replace the first line with this new one
# Add a second line to this new version of the file
# We can verify the length of the text with the len function()
len(text3)

#We can also create a small function that reads every line of the file:
file1 = open("file1.txt", "r")    
for line in file1:
    print(line, end = "")
# Or proceed as follows:     
with open("file1.txt", "a") as file:
    file1.write("this is the third line") 
    
    
    
    
    
#### import CSV FORMAT#####
# we import csv
import csv
""" next, I generate a random csv file that I save in the work 
directory and call it 'df'. The second argument, 'r', means we
are accessing the file in read mode."""
csv1 = open('df.csv', 'r')
# if we want to import a file that is not in the work directory, we can include the entire address, for example:
csv2 = open('/Users/bunya/python/df.csv', 'r')    
# we go on reading the first file
read = csv.reader(csv1)    



### IMPORT FROM WEB###
# we create an object that contains the address
from urllib.request import urlopen

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data"
# we create a connection
conn = urlopen(url)
file = csv.reader(conn)

