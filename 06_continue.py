#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 05:33:20 2022

@author: marcinbogusz
"""

# %%
for i in range(10):
    if i == 6:
        continue
    print(i)
    
# f.continue pozwoliło iterować elementy != 6

# %%
for i in range(20):
    if i % 2 == 0: #liczby nieparzyste
        continue
    print(i)

# %%
for i in range(20):
    if i % 2 == 1: #liczby parzyste
        continue
    print(i)    

# %%
sample = 'Python Course'
for char in sample:
    if char == ' ':
        continue
    print(char)

# %%
hashtags = '#summer#holiday#free'
result = ''
for char in hashtags:
    if char =='#':
        print(result)
        result = ''
        continue
    result = result + char
print(result)

