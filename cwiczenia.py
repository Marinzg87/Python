#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 05:41:58 2022

@author: marcinbogusz
"""

# %%
fakt = 'python jest łatwy i przyjemny'
lista = list(fakt)
zbior = set(lista)

if len(zbior) < 20:
    print('Mniej niż 20 unikalnych znaków.')
else:
    print('Liczba unikalnych znaków jest większa lub równa 20.')
    
# %%
text = 'sfdjakvqksdfafewfvdafafv'
if 'q' in text:
    print('Zawiera')
else:
    print('Nie zawiera')
    
# %%
text = 'sfdjakvqksdfafewfvdafafv'
'Zawiera' if 'q' in text else 'Nie zawiera'

# %%
for i in range(0,21):
    print(i)
    
# %%
hashtags = '#weekend#good#time#'
result = ''

for char in hashtags:
    if char not in '#':
        result = result + char
    else:
        print(result)
        result = ''

# %%
hashtags = '#weekend#good#time#'
result = ''

for char in hashtags:
    if char not in '#':
        result = result + char
    else:
        if result:
            print(result)
            result = ''
            
# %% walidator hasła
ps = 'jnhvsoics!vd'
if len(ps) > 10:
    for char in ps:
        if '!' in ps:
            print('Hasło poprawne')
            break
        else:
            print('Hasło niepoprawne')
            break
else:
    print('Hasło niepoprawne')

