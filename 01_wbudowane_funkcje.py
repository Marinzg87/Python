#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 22 12:20:43 2022

@author: marcinbogusz
"""

# %% liczba bezwlędna
abs(10)
abs(-10)
print(abs(-10))

# %% testowanie logiki elementu
bool([])
bool('')
bool({})
bool(' ')
bool(True)
bool(12)
bool(0)

# %% atrybuty i metody
dir()
dir(list)
dir(tuple)

# %% iterowanie
enumerate(['marcin', 'python', 'java'])
list(enumerate(['marcin', 'python', 'java']))

# %% wykonanie działań, które będą przekazane jako tekst
eval('1 + 1')

x = 10
eval('x + 13')

# %% informacja o obiekcie
filter?


# %% filtrowanie danych
list(filter(abs, [-2, -1, 0, 1, 2]))

# %%
list(filter(bool, ['python', '', 'java']))

# %% konwersja liczby lub wartości text na liczbę zmienno przecinkową
float(1)
float(1.3)
float('1')
float('ffr')
float('3.5')

# %% typ elementu
type(1)
type('vdf')

# %% pomoc
help()
help(float)

# %% zbdanie czy obiekt jest instancją naszej klasy
isinstance?
isinstance(1, int)
isinstance(1, float)
isinstance(1.0, float)

# %% zwraca długość danego elementu
len('python')
len('')
len(' ')
len([])
len([[3,4], [4,5,6,7, [5,5]]])

# %% przyjmuje obiekt iterowalny i zwraca listę
list('python')
list(range(10))

# %% podobna do filter
list(map(abs, [-2, -1, 0, 1, 2]))

# %%
names = ['marcin', 'tomek', 'janek']
list(map(str.title, names))

# %% statystyka max i min
max([1, 2, 5, 2])
max('pawel')
max('marcin')

min([1, 2, 4, 6])
min('marcin')

# %% potęgowanie
pow(2, 4)
2 ** 4

# %%
list(reversed([5, 3, 7]))
list(reversed('python'))

# %% zaokrąglenia
round(4.324255)
round(3.4242424, 2)

# %%
str(1)
str(343.434)

# %%
sum([3, 4, 5, 3])

# %% iterowanie po kilku elementach jednocześnie
lista_1 = [1, 2, 3]
lista_2 = [4, 5, 6]

list(zip(lista_1, lista_2))

# %%
list(zip('python', 'course'))




