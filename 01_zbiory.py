#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 14:05:07 2022

@author: marcinbogusz
"""

empty_set = set()
print(empty_set)
print(type(empty_set))


# %%
techs = {'python', 'java', 'c++', 'sql'}
print(len(techs))

# %%
set('python') # funkcja set, unikalne wartości doda do zbioru
set('aaaaaaaale')


# %%
'python' in techs
'go' in techs

# %% metody dla zbiorów
dir(set)

# %%
techs.add('sas')
print(techs)

# %%
techs.remove('sas')

# %% wyrywa dowolny element, zwraca go nam i usuwa ze zbioru
techs.pop()

# %%
techs.clear()


# %% logika zbiorów
A = {1, 2, 3, 4, 5, 6, 7}
B = {5, 6, 7, 8, 9}
C = {5, 6}

C.issubset(A)
C.issubset({5, 7})
A.issuperset(C) # A jest badzbiorem zbioru C - wszystkie elementy C są w A
A.union(B) # łączy wartości zbiorów, usuwwa dulikaty
A.intersection(B) # pokazuje tylko elemety wspólne
A.symmetric_difference(B) # wyłacza tylko elementy wspólne

D = A.copy()
