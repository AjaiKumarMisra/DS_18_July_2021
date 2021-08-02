# Write a Python program to count the number of characters in a string: 'google.com'
# O/p should be in the form of dictionary and each char should be used as key and their number of occurrences should be value

from collections import Counter 
dictN={}
counter=1
j=""
lst=list("google.com")
   
d=Counter('google.com')
for key,value in d.items():
    dictN.update({""+key+"":value})

print(dictN)    
    