#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 05:45:48 2022

@author: marcinbogusz
"""

# %%
raw_data = '345!23!3234!43434'
for char in raw_data:
    if char == '!':
        continue
    print(char)
    
# %%
raw_data = '345!23!3234!43434'
clean_data = ''
for char in raw_data:
    if char == '!':
        print(clean_data)
        continue
    clean_data = clean_data + char
print(clean_data)

# %%
raw_data = '345!23!3234!43434'
clean_data = ''

for char in raw_data:
    if char != '!':
        clean_data = clean_data + char
    else:
        clean_data = clean_data + ','
print(clean_data)

# %%
raw_data = '345!23!3234!43434'
clean_data = ''

for char in raw_data:
    if char != '!':
        clean_data += char
    else:
        clean_data += ','
print(clean_data)

# %%
suma = 0
for i in range(10):
    suma += i
print(suma)

# %%
saldo = 450
print('Saldo początkowe {}'.format(saldo))
for kwota in range(10, 60, 10):
    print('Wypłacona kwota {}'.format(kwota))
    saldo -= kwota
    print('Saldo: {}'.format(saldo))
print('Saldo końcowe: {}'.format(saldo))

# %% system sprawdzający czy w pinie są liczby
print('Witaj w systemie logowania.')
print('*' * 30)
nick = input('Podaj swój nick: ')
pin = input('Podaj swój kod pin, {}: '.format(nick))

if len(pin) == 4:
    for char in pin:
        if char not in '0123456789':
            print('Podałeś niepoprawny kod pin. Podaj tylko cyfry.')
            break
    else:
        print('Kod pin ważny.')
else:
    print('Podałeś niepoprawną długość kodu pin.')

        
    






