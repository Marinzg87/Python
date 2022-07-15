#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jul 15 07:56:49 2022

@author: marcinbogusz
"""

text = 'Witaj na kursie Pythona.\nPython jest wspaniały.'

print(text)

# %%
dir(text)
help(str.count) # pomoc z dokumentacji 

# %% Wielka litera tylko w pierwszym wyrazie
text.capitalize()

# %% Wielka litera dla każdego wyrazu w ciągu
text.title()

# %% Zwraca ilość powtórzonych stringów
text.count('Python')

# %% Zwraca prawda/fałsz, dla podanego warunku, sprawdza od początku str
text.startswith('Wi')

'python'.startswith('py')

# %%
text.endswith('y.')

# %%
'sample.py'.endswith('.py')

# %% numer indeksu od którego się znajduje
text.find('Python')
text[text.find('Python'):]

# %%
hashtags = '#sport#gym'
idx = hashtags.find('#')

# %% czy zawiera znaki alfanumeryczne
'marcin87'.isalnum() #True
'marcin87 '.isalnum() #False

# %% czy wszystkie znaki są liczbami
'43434'.isdigit()

# %% znaki z małej litery
'pyThon'.islower()

# %% duże litery
'MARCIN'.isupper()

# %% łączenie tekstów
' '.join(['python', '3.8'])
'#'.join(['sport', 'gym', 'fit'])
','.join(['1', '2', '3', '4'])

# %% zastąpowanie danych
'#good#time#mood'.replace('#', ' ')

# %%
'column name'.replace(' ','_')

# %% wycinanie białych znaków w tekście
'     python     '.strip()
'     python     '.rstrip() # wycinanie spacji po prawej stronie
'     python     '.lstrip() # wycinanie spacji po lewej stronie

# %% dzielenie
'1,2,3,4,5'.split(',')

'python java php sql sas'.split() # bez podawania argumentu domyślnie wybiera spację

'#gym#fit#mood'.split('#')

# %% wypełnianie liczbą zer
'12'.zfill(5)
'1'.zfill(10)
