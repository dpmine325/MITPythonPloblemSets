# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

s = 'afwhddasfsasxzakm'
vowel = "aeiou"
count=0

for letter in s:
    for v in vowel:
        if letter == v:
            count +=1
            break
        
print (count)
    
