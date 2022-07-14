#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 08:41:48 2022

@author: marcinbogusz
"""

# %% konwencja nazwenictwa zmiennych
imie = 'Marcin'
_imie = 'Piotr' # zmienna środowiskowa Pythona, nie powinno się jej używać

# %% nazwenictwo bez znacznia
a = 8
b = 20

c = a * b
print(c)

# %% nazwenictwo posiadające znaczenie
przepracowane_godziny = 8
stawka_godzinowa = 20

dzienna_pensja = przepracowane_godziny * stawka_godzinowa
print(dzienna_penssja)

# %% style
camelCase = 'Python 3.8'
PascalCase = 'Python 3.8'
snake_case = 'Python 3.8' # nazwy metod i zmiennych
kebab-case = 'Python 3.8'
UPPER = 'Python' # przechowywanie stałych

# %% nazwy zarezerwowane dla Python
import keyword
keyword.kwlist
