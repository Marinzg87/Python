#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 06:43:01 2022

@author: marcinbogusz
"""

# %% break - przerywa pętlę w wybranym momencie
for i in '0123456789':
    print(i, type(i))
    
# %%
for i in '0123456789':
    i = int(i)
    if i == 6:
        print(i, type(i))
        break
    
# %%
for i in '0123456789':
    i = int(i)
    print(i)
    if i == 6:
        break
    
# %%
sample = 'Python Course'
for char in sample:
    if char == ' ':
        break
    print(char)

print('Koniec.')

# %%
for char in 'kowalskij@gmail.com':
    if char == '@':
        print('Adres email zweryfikowany.')
        break
    else:
    print('Adres email nie jest poprawny.')
    
print('Koniec.')