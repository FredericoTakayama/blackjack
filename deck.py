#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from random import randint

class Card(object):
    def __init__(self, suit_idx = 0,number_idx = 0, deck_name=None):
        suits = ['Club', 'Heart', 'Spade', 'Diamond']
        numbers = [i for i in range(1,14)] # indica o valor da carta
        names = ['ace','two','three','four','five','six','seven','eigth','nine','ten','jack','queen','king']
        self.suit = suits[suit_idx]
        self.number = numbers[number_idx]
        self.name = names[number_idx]
        self.face_on = False # indica se esta virada (True) ou nao (False)
        self.deck_name = deck_name
        self.shows_deck_name = False # for debug, change it to True

    def turn(self):
        self.face_on = not self.face_on

    def is_turned_on(self):
        return self.face_on

    def __str__(self):
        if self.deck_name and self.shows_deck_name:
            return '%s: %s of %s' % (self.deck_name, self.name, self.suit)
        else:
            return '%s of %s' % (self.name, self.suit)

class Deck(Card):
    def __init__(self, deck_name=None):
        self.deck_name = deck_name
        self.cards=[]
        for i in range(0,4):
            for j in range(0,13):
                card=Card(i, j, self.deck_name)
                self.cards.append(card)

    def shuffle(self):
        '''shuffle deck'''
        buffer=[]
        while(len(self.cards)):
            i = randint(0, len(self.cards)-1)
            card = self.cards.pop(i)
            buffer.append(card)
        print('I like to shuffle it, shuffle it')
        self.cards = buffer

    def get_number_of_cards_with_faces_on(self):
        sum = 0
        for card in self.cards:
            sum = sum + 1 if card.is_turned_on() else sum
        return sum

    def __str__(self):
        # for card in self.cards:
        #     print(card)
        return 'deck: %s' % (self.deck_name)