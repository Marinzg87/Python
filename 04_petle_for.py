#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 20 06:04:22 2022

@author: marcinbogusz
"""

# %%
name = 'python'

for character in name:
    print(character)
    
# %%
name = 'python'
index = 0

for character in name:
    print(index, character)
    index = index + 1
    
# %%
for index in range(10):
    print(index)
    
# %%
for index in range(len(name)):
    print('Nr indeksu: ', index, 'Litera: ', name[index])

# %%
for i in enumerate(name):
    print(i)

# %%
for indeks, character in enumerate(name):
    print(indeks, character)
    
# %%
for i in [4, 5, 6, 8, 6]:
    print(i)
    
# %% f.enumerate jest rekomendowanym sposobem dla pętli for, wyciągania indeksów
for i, value in enumerate([4, 5, 6, 8, 6]):
    print(i, value)
    
# %% f.range buduje iterator, po którym możemy iterować w pętli
for i in range(10):
    print(i)
    
# %%
for i in range(10, 20):
    print(i)

# %%
for i in range(10, 20, 2):
    print(i)

# %%
for i in range(10, 0, -1):
    print(i)

# %%
for i in range(10, -1, -1):
    print(i)

# %%
techs = 'java'
for i in range(len(techs)):
    print(i, techs[i])
    
# %%
string = 'Python Course'
for char in string:
    print(char)
    
# %%
string = 'Python Course'
for char in string[:6]:
    print(char)

# %%
string = 'Python Course'
for char in string[::-1]:
    print(char)

# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    print(char)
    
# %%
hashtags = '#sport#gym#fitness'
for char in hashtags:
    if char not in '#':
        print(char)

# %%
for char, number in zip('abcde', '12345'):
    print(char, number)
    
# %%
hashtags = '#sport#gym#fitness#'
result = ''
for char in hashtags:
    if char not in '#':
        result = result + char
    else:
        print(result)
        result = ''
