#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 13:14:01 2022

@author: marcinbogusz
"""

# %%
def funkcja_1():
    print('Pierwsza funkcja uruchomiona.')
    
funkcja_1()

# %%
def funkcja_2(x, y):
    print('Podane argumenty to: {}, {}'.format(x, y))
    
funkcja_2(2, 10)

# %%
def funkcja_3(x, y):
    print('Podane argumenty to: {1}, {0}'.format(x, y))
    
funkcja_3(2, 10)

# %%
def funkcja_4(x, y=10):
    print('Podane argumenty to: {}, {}'.format(x, y))
    
funkcja_4(2)

# %%
def funkcja_5(x=3, y=10):
    print('Podane argumenty to: {}, {}'.format(x, y))
    
funkcja_5()

# %%
import math
math.sqrt(2)
math.exp(1)
math.sin(0)

# %%
def funkcja_6():
    print('Uruchomiono.')
    
funkcja_6()
print(type(funkcja_6))

fun = funkcja_6()

# %%
def add(x, y):
    return x + y

add(2, 6)
result = add(2, 6)

# %%
def subtract(x: int, y: int):
    """
    Odejmuje od siebie dwie liczby.
    """
    return x - y

subtract(10, 6)

# %%
def print_menu():
    print('Start programu...')
    print('*' * 30)
    print("""Wybierz jedną z podanych opcji:
          0 - logowanie
          1 - wyjście""")
    print('*' * 30)
    print('Koniec programu.')

print_menu()

# %%
def print_even(maximum):
    even = []
    for i in range(maximum + 1):
        if i % 2 == 0:
            even.append(i)
    return even

print_even(10)
num = print_even(20)

# %%
def write_file(file_name, text):
    with open(file_name, 'w') as file:
        print(text, file=file)
        
write_file('sample_2.txt', 'Pierwsza.\nDruga.\nTrzecia')

# %%
def calculate_profit(pv, rate, n):
    return pv * (1 + rate) ** n - pv

calculate_profit(1000, 0.02, 1)

# %%
def calculate_profit(pv=1000, rate=0.03, n=1):
    return pv * (1 + rate) ** n - pv

# calculate_profit(1000, 0.02, 1)
calculate_profit(rate=0.15)
