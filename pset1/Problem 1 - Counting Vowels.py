
# -*- coding: utf-8 -*-
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:
s = 'azcbobobegghakl'
count = 0
z = -1
for k in s:
    z+=1
    if (s[z] == 'a' or s[z] == 'e' or s[z] == 'i'or s[z] == 'o'or s[z] == 'u'):
        count+=1
print('Number of vowels:',count)
