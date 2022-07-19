#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 19 09:33:31 2022

@author: marcinbogusz
"""

# %%
version = 3.8

print(version)

# %%
version > 3
version <= 3

# %%
number = 1200
number > 1000
number == 1200 # operator porównania ==
number != 1200 # operator różnicy
number != 1000

# %% instrukcja wwarunkowa
#if [warunek]:
#    [instrukcje]

# %%
if 8 < 10:
    print('Tak')
    
if 8 > 10:
    print('Tak')
    
# %%
a = 12
if a > 10:
    print('a > 10')
    
# %%
a = 5
if a > 10:
    print('a > 10')
else:
    print('a < 10')
    
# %%
age = 35
if age < 18:
    print('Nie masz uprawńień.')
else:
    print('Dostęp przyznany.')
    
# %%
age = 15
if age == 18:
    print('Masz 18 lat.')
elif age < 18:
    print('Nie masz uprawnień.')
else:
    print('Dostęp przyznany.')
    
# %% lepsza czytelność programu
age = 35
if age == 18:
    print('Masz 18 lat.')
elif age < 18:
    print('Nie masz uprawnień.')
elif age > 18:
    print('Dostęp przyznany.')

# %%
age = int(input('Podaj swój wiek: ')) # f.input odczytuje str, f.int konwersja
if age == 18:
    print('Masz 18 lat.')
elif age < 18:
    print('Nie masz uprawnień.')
elif age > 18:
    print('Dostęp przyznany.')
    
# %%
print('Program uruchomiony....')
print("""Włam się do systemu, zgadując dwucyfrowy pin.
Numer pin składa się z cyfr: 0, 1, 2.""")
pin = int(input('Wprowadź numer pin: '))

if pin == 21:
    print('Brawo! Złamałeś system.')
elif pin == 20:
    print('Byłeś blisko!.')
else:
    print('Nie zgadłeś.')
    
# %%
bool(' ')    
bool(0)

# %%
string = ''

if string:
    print('Niepusty ciąg znaków.')
else:
    print('Pusty ciąg znaków.')

# %%
number = 1
if number:
    print('Liczba niezerowa!')
else:
    print('Zerrrrro!!')
    
# %%
default_flag = True

if default_flag: # można dopisać == True, ale jest to zbędne
    print('Doszło do defaultu')
else:
    print('Nie doszło')

# %% zaprzeczenia
default_flag = False

if not default_flag: # można dopisać == True, ale jest to zbędne
    print('Nie doszło')
else:
    print('Doszło do defaultu')
    

    