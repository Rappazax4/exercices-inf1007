#!/usr/bin/env python
# -*- coding: utf-8 -*-

def majuscule(mot):
    # TODO completer la fonction ici
    nov_mot = ""
    
    for letter in mot:
        letter = chr(ord(letter)-32)
        nov_mot += letter
    
    mot = nov_mot
    return mot


if __name__ == '__main__':
    mots = [
        'riz',
        'cours',
        'voiture',
        'oiseau',
        'bonjour',
        'églantier',
        'arbre'
    ]
    for i in range(len(mots)):
        mots[i] = majuscule(mots[i])

    print(mots)

