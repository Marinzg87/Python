#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:47:04 2022

@author: marcinbogusz
"""

# %%
file = open('simple.txt', 'r')

for line in file:
    print(line, end='')
    
file.close()

# %%
with open('simple.txt', 'r') as file:
    for line in file:
        print(line, end='')
    
# %%
# Tryby odczytu pliku
# 'r' - read - otwiera plik do odczytu, zwraca błąd jeśli plik nie istnieje
# 'a' - append - otwiera plik do dopisania, tworzy plik jeśli nie istnieje
# 'w' - write - otwiera plik do zapisu, tworzy plik jeśli nie istnieje

# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    print(line)

# %%
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    print(lines)

# %%
with open('simple.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line, end="")

# %%
with open('simple.txt', 'r') as file:
    line = file.readline()
    while line:
        print(line, end='')
        line = file.readline()

# %%
with open('simple.txt', 'r') as file:
    lines = file.read()
    print(lines)


