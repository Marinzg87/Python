#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 13:46:12 2022

@author: marcinbogusz
"""

# %%
techs = []
print(techs)

# %% append dodawanie elementów
techs.append('python')
print(techs)

# %%
techs.append('java')

# %% zagnieżdżanie
techs.append(['hadoop', 'spark'])
print(techs)

# %% dodanie elementów do tego samego poziomu
techs.extend(['sql', 'sas'])
print(techs)

# %% insert
techs.insert(0, 'go')
print(techs)

# %%
techs.insert(2, 'r')
print(techs)

# %% pop usuwa, bez argumentu bierze ostatnią, listy są uporządkowane
techs.pop()
print(techs)
print(techs.pop())

print(techs.pop(0))

# %%
techs.insert(3, 'php')

techs.index('r')

# %%
techs = ['python', 'java', 'sql', 'php', 'r', 'angular']
techs.count('python')
techs.count('java')

# %%
techs.sort()
techs.sort(reverse=True)

# %%
techs[::-1]
techs.reverse()

# %%
techs[1] = 'c++'
