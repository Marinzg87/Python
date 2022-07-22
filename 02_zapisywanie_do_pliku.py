#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 11:59:34 2022

@author: marcinbogusz
"""

# %% zapisanie danych do pliku
techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'w') as file:
    for tech in techs:
        print(tech, file=file)

# %%
even_number = list(range(100))[::2]

with open('numbers.txt', 'w') as file:
    for number in even_number:
        file.write(str(number) + '\n')
        
# %% dodanie nowych danych do pliku, a nie jego nadpisywanie
techs = ['python', 'java', 'sql', 'r', 'scala']

with open('techs.txt', 'a') as file:
    for tech in techs:
        print(tech, file=file)

# %%
technologies = []
with open('techs.txt', 'r') as file:
    for line in file:
        technologies.append(line)
print(technologies)

# %%
technologies = []
with open('techs.txt', 'r') as file:
    for line in file:
        technologies.append(line[:-1])
print(technologies)

# %%
with open('tree.txt', 'w') as file:
    for j in range(2):
        for i in range(10):
            print('{:>9}'.format('*' * i), end="", file=file)
            print('{}'.format('*' * i), file=file)

# %%
with open('tree.txt', 'a') as file:
    for j in range(2):
        for i in range(10):
            print('{:>9}'.format('*' * i), end="", file=file)
            print('{}'.format('*' * i), file=file)
