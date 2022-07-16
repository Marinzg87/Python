#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 13:22:25 2022

@author: marcinbogusz
"""

# %%
empty_list = list()
print(empty_list)

# %%
techs = ['python', 'java', 'c++', 'go', 'sql']
techs[0] = 'python 3.8'
print(techs)

# %%
numbers = [3, 5, 3, 5, 23]
print(numbers)
print(type(numbers))

# %%
mixed = ['python', 3.8, 4, True]

# %%
empty = []
nested = [[1, 2, 3], ['python', 'java', 'go'], 3]

# %%
first = ['mleko', 'ziemianki', 'makaron']
second = ['woda', 'jajka']

bucket = [first, second]

# %%
len(bucket)

# %%
techs += ['javascript']
print(techs)

# %%
print(dir(list))
