#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul 16 13:00:54 2022

@author: marcinbogusz
"""

# tuple - uporządkowana struktura, której nie można zmieniać

empty_tuple = tuple()
print(empty_tuple)

# %%
amazon = ('Amazon', 'USA', 'Technology', 1)
google = ('Google', 'USA', 'Technology', 2)

# %%
name_google = google[0]
google[0] = 'Google Company' # error, nie możemy zmienić wartości w tuple

# %%
data = (amazon, google)
print(data)

# %%
a = ('Marcin', 'Bogusz')
print(a)

# %%
imie = 'Marcin'
naziwsko = 'Bogusz'

imie, naziwsko, id_user = ('Marcin', 'Bogusz', '001')

# %% rozpoakowanie tuply do zmiennych
amazon_name, country, sector, rank = amazon

# %%
stocks = 'Amazon', 'Apple', 'IBM'
print(type(stocks))

# %%
nested = 'Europa', 'Polska', ('Warszawa', 'Kraków', 'Wrocław')
print(nested)

# %%
a = 12
b = 14

c = b
b = a
a = c
print(a, b
      
# %% zarządzanie zmiennymi jest ułatwione dzięki tuple
x, y = 10, 15
x, y = y, x
print(x, y)