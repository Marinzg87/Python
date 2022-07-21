#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul 21 06:08:33 2022

@author: marcinbogusz
"""

# %% pętla while od for różni się tym, że to my podajemy warunek zatrzymiania
i = 0
while i < 5:
    print(i)
    i += 1 #bez warunku inkrementowania naszej zmiennej, możemy napisać nieskończoną pętle
    
# %%
n = 0
while True:
    print(n)
    if n > 10:
        break
    n += 1
    
# %%
while True:
    name = input('Podaj swoje imię: ')
    if len(name) >= 3 and name.isalpha():
        break
print('Cześć {} '.format(name))

# %% liczby nieparzyste
n = 0

while n < 20:
    n += 1
    if n % 2 == 0:
        continue
    print(n)
    
# %% liczby parzyste
n = 0

while n < 20:
    n += 1
    if n % 2 != 0:
        continue
    print(n)
    
# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 63

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if flaga:
    print('Znaleziono element {}'.format(wartosc))

# %%
lista_do_przeszukania = [12, 53, 13, 63, 34]
flaga = False
wartosc = 60

idx = 0
while idx < len(lista_do_przeszukania):
    if lista_do_przeszukania[idx] == wartosc:
        flaga = True
        break
    idx += 1
if not flaga:
    lista_do_przeszukania.append(wartosc)









