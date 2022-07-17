#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 17 22:51:24 2022

@author: marcinbogusz
"""

# %% pusty słownik
empty_dict = dict()

d = {} # kolejny sposób utworzenia pustego słownika, nawias sześcienny
print(type(d))

e = set() # pusty zbiór

# %% słownik, nieuporządkowana struktura, zawiera pray klucz:wartość
pol_to_eng = {'jeden' : 'one', 'dwa' : 'two', 'trzy' : 'three'}
# klucze w słowniku muszą być unikalne, nie mogą się powtórzyć

# %%
name_to_digit = {'jeden' : 1, 'dwa' : 2, 'trzy' : 3}

# %%
len(name_to_digit)
# dict = {'key' : 'value', 'key2' : 'value2'}

# %% dodawanie elementów do słownika
pol_to_eng['cztery'] = 'four'

# %%
pol_to_eng.clear()

# %%
pol_to_eng_copied = pol_to_eng.copy()

# %% wydobycie wszystkich kluczy ze słownika
list(pol_to_eng.keys())

# %% wartości
pol_to_eng.values()
list(pol_to_eng.values())

# %% klucze & wartości
pol_to_eng.items()

# %%
pol_to_eng['jeden']

pol_to_eng.get('jeden')
pol_to_eng.get('zero', 'Nan')

# %%
pol_to_eng.pop('dwa')
pol_to_eng.popitem()

# %%
pol_to_eng.update({'jeden':1})

# %%
capitals = {'Polska':'Warszawa','Niemcy':'Berlin','Czechy':'Praga'}
capitals['Włochy'] = 'Rzym'
cities = sorted(list(capitals.values()))
print(cities)