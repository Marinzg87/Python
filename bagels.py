"""Bajgle, autor: Al Sweigart, al@inventwithpython.com
Logiczna gra na dedukcję, gdzie musisz odgadnąć liczbę na podstawie wskazówek.
Kod przepisany z książki, przez Marcin Bogusz, bogusz.marcin@icloud.com
Inną wersję tej gry znajdziesz w książce "Twórz własne gry komputerowe w Pythonie",
https:(...)
Etykiety: krótki, gra, łamigłówka"""

import random

NUM_DIGITS = 3  # (!) Spróbuj ustawić tę stałą na 1 lub 10.
MAX_GUESSES = 10  # (1) Spróbuj ustawić tę stałą na 1 lub 100.


def main():
    print('''Bajgle, logiczna gra na dedukcję.
Autor: Al Sweigart, al@inventwithpython.com

Mam na myśli {}-cyfrową liczbę, w której nie powtarza się żadna z cyfr.
Spróbuj ją odgadnąć. Oto wskazówki:
Gdy mówię:      Oznacza to:
   Piko         Jedna cyfra jest poprawna, ale jest na złej pozycji.)
   Fermi        Jedna cyfra jest poprawna i znajduje się w odpowiednim miejscu.
   Bajgle       Żadna cyfra nie jest poprawna.

Na przykład, jeśli tajna liczba to 248, a Ty podasz liczbę 843,
wskazówka będzie brzmieć Fermi Piko.'''.format(NUM_DIGITS))

    while True:     # Pętla główna
        # Ta zmienna przechowuje liczbę, którą gracz musi odgadnąć:
        secretNum = getSecretNum()
        print('Mam na myśli liczbę.')
        print('Masz {} prób, by odgadnąć, jaka to liczba.'.format(MAX_GUESSES))

        numGuesses = 1
        while numGuesses <= MAX_GUESSES:
            guess = ''
            # Wykonywanie pętli, dopóki gracz nie poda poprawnej liczby:
            while len(guess) != NUM_DIGITS or not guess.isdecimal():
                print('Próba #{}: '.format(numGuesses))
                guess = input('> ')

            clues = getClues(guess, secretNum)
            print(clues)
            numGuesses += 1

            if guess == secretNum:
                break  # Podana liczba jest poprawna, zakończ pętlę.
            if numGuesses > MAX_GUESSES:
                print('Wykorzystałeś wszystkie próby.')
                print('Prawidłowa odpowiedź to: {}.'.format(secretNum))

        # Zapytaj gracza, czy chce zagrać ponownie.
        print('Czy chcesz zagrać jeszcze raz? (tak lub nie)')
        if not input('> ').lower().startswith('t'):
            break
    print('Dziękuję za grę!')
