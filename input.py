#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 14 08:31:38 2022

@author: marcinbogusz
"""

# %%
imie = input('Podaj swoje imię: ')

# print('Cześć', imie)
print('Cześć {}!'.format(imie))

# %%
jezyk = input('Jakiego języka chcesz się nauczyć? ')

print('Podano język {}'.format(jezyk))

# %%
name = input('Podaj imię: ')
age = input('Podaj wiek: ')

print('Cześć {}! Masz {} lat.'.format(name, age))

# %% funkcja input podaje wartości jako tekst
age_2 = input('Podaj wiek: ') # tutaj będzie zmienna str
age_3 = int(input('Podaj wiek: '))

# %%
x = '1323435'
y = 12334
z = '0'

print('x: {0}\ny: {1}\nz: {2}'.format(type(x), type(y), type(z)))
