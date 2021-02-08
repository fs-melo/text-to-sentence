# -*- coding: utf-8 -*-
"""
Created on Wed May 17 00:12:52 2017

@author: Fabrício
"""

import os
from nltk.tokenize import sent_tokenize
 
DD = os.getcwd()
text=open(DD+'/Files/text.txt').read()

sent_tokenize_list = sent_tokenize(text)
print(sent_tokenize_list)
filepath = './Files/sentences.txt'

with open(filepath, 'w') as file_handler:
    for item in sent_tokenize_list:
        file_handler.write("{}\n".format(item))
