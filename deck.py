#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

class Card(object):
    def __init__(self,suit_idx = 0,number_idx = 0):
        suits = ['Club', 'Heart', 'Spade', 'Diamond']
        numbers = [i for i in range(1,14)]
        names = ['ace','two','three','four','five','six','seven','eigth','nine','ten','jack','queen','king']
        self.suit = suits[suit_idx]
        self.number = numbers[number_idx]
        self.name = names[number_idx]
        self.face_on = False # indica se esta virada (True) ou nao (False)

    def turn(self):
        self.face_on = not self.face_on

    def is_turned_on(self):
        return self.face_on

    def __str__(self):
        return '%s of %s' % (self.name,self.suit)

class Deck(Card):
    def __init__(self):
        self.cards=[]
        for i in range(0,4):
            for j in range(0,13):
                card=Card(i,j)
                self.cards.append(card)

    def shuffle(self):
        buffer=[]
        while(len(cards)):
            i = randint(0, len(cards)-1)
            pass

    def get_number_of_cards_with_faces_on(self):
        pass

    def __str__(self):
        pass