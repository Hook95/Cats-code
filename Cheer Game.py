# -*- coding: utf-8 -*-
"""
Created on Sat Jul 17 09:35:15 2021

@author: letme
"""
an_letters = 'aefhilmnorsxAEFHILMNORSX'
word= input(' I will cheer for you! Enter a word: ')
times = int(input('Enthusiasm level (1-10): '))

for char in word:
    if char  in an_letters:
        print('Give me an ' + char + '! ' + char)
    else:
        print('Give me a ' + char + '! ' + char)
print('What does that spell?')
for i in range (times):
            print(word, '!!!')
    
            