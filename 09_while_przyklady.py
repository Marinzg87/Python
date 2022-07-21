#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:36:34 2022

@author: marcinbogusz
"""

# %%
KOD_PIN = '0000'

pin = input('Podaj kod pin: ')

while pin != KOD_PIN:
    pin = input('Spróbuj ponownie jeszcze raz: ')
print('Zalogowany!')

# %%
KOD_PIN = '0000'

pin = ''
counter = 0

while pin != KOD_PIN and counter < 3:
    pin = input('Wprowadź kod pin: ')
    if pin == KOD_PIN:
        print('Zalogowany.')
        break
    counter += 1
else:
    print('Zbyt dużo prób logowania.')



