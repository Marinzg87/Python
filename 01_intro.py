# -*- coding: utf-8 -*-

# komentarz - dobre komentowanie kodu jest kluczowe
# dzielenie kodu na komórki # %%

# %% dodawania
print(2 + 2)

# %% mnożenie
print(3 * 3)

# %% wyrażenie matematyczne
print(3 + 2 * 2)

# %% dzielenie z resztą
10 / 3
4 / 2

# %% dzielenie całkowite
print(10 // 3)
print(7 // 6)

# %% potęgowanie
print(2 ** 5)

# %% dzielenie modulu - zwraca resztę z dzielenia, może posłużyć do odszukania liczb parzystych
print(10 % 3)
print(12 % 5)

# %% kolejność wykonywania działań
print((10 -2 ** 3) * 10)

# %% test wydruku komórki w konsoli, w mojej wersji spyder klawisz F9
2 + 2

# %% przypisywanie zmiennych
a = 10
b = 20

c = a * b
print(c)

# %% zmienne tekstowe
print('love python')
"love python"

# %% print apostrofu
print("It's the best!")

'It\'s the best!'

# %% funkcja print
print('Python 3.7')

# %% 
print('Python\n3.7')

print("""Python
3.7""")

# %% zaawansowane printowanie
print('\tPython') ## pusta przestrzeń komenda t
print('\t\t\tPython')

# %% błędy
print('C:\path\to\something\new')

print('C:\path\\to\something\\new') ## znak ucieczki pozwala uniknąć błędów

print(r'C:\path\to\something\new') ## r- raw text

# %%
import os
os.getcwd()

# %%
print("""Instrukcja uruchamiania pliku przyklad.py:

    --file [nazwa pliku]
        zapisuje output do pliku
        
    --quiet
        wycisza logi w konsoli
        
Koniec.""")

# %%
text = "I love Python. "
print(text)
print( text * 3)
print('hau...' * 8)
print('*' * 30)


# %%
'Python'
'Py' 'thon'
print('Py' 'thon')

# %% not best practice - konwencja 79 znaków
url = 'https://ml-repository-krakers.s3-ue-west-1.amazonaws.com/python_course/python.png'

# %% best practice - konwencja 79 znaków
url_2 = ('https://ml-repository-krakers.s3-ue-west-1.amazonaws.com/'
       'python_course/python.png')

# %%
name = 'Python'
print(name + ' 3.7')
print(name, '3.7')

# %%
age = 35
imie = 'Marcin'

print(imie + ' ' +  str(age))
print(imie, age)
print('{} ma {} lat.'.format(imie, age))
print('{0} ma {1} lat.'.format(imie, age))
print('{1} ma {0} lat.'.format(imie, age))

# %% 
saldo = 40
saldo = saldo + 30
saldo += 30
saldo = saldo - 10
saldo -= 10

print(saldo)

# %%
lokata = 1000
czynnik_akumulacyjny = 1 + 0.04
lokata_po_roku = lokata * czynnik_akumulacyjny
print('Wartość lokaty po roku:', lokata_po_roku)

# %%
pixel = 150
pixel = pixel / 255
pixel /= 255
print(pixel)

# %%
base = 2
base = base ** 5
base **= 5
print(base)

# %%
x = 103
x = x % 10
x %= 10
print(x)

# %%
imie = 'Marcin '
nazwisko = 'Bogusz'
nazwa = imie + nazwisko

# %%
name = 'Python '
version = '3.8'
name += version
print(name)

