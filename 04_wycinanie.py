#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 07:16:22 2022

@author: marcinbogusz
"""

name = 'Python'

# %%
print(name)
print(name[0])  # wycinanie tekstu po indeksie
print(name[1])
print(name[-1])

# %% konwencja wycinania
# name[start:stop]
# name[:stop]
# name[start:]
# name[start:stop:step] 
name[1:4]
name[:4]
name[2:]
name[:]

# %%
name[-2:]
name[-3:-1]

# %%
full = 'Python Programming'
print(full[7:])
print(full[::2])

# %%
sample = '#stop#this#flow'
print(sample[::5])

# %%
numbers = '8,9,7,4'
print(numbers[::2]) 

# %%
print(numbers[::-1])

# %%
name_2 = 'kajak'
print(name_2[::-2])

# %% Sprawdzenie, czy w naszej zmiennej jest dany znak

'P' in name
'p' in name
