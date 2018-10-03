#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from deck import Card, Deck
from random import randint

class BlackjackDeck(object):
    def __init__(self, deck_name=None):
        self.decks=[]
        self.decks.append(Deck('deck_one'))
        self.decks.append(Deck('deck_two'))
        self.cards=[]
        for deck in self.decks:
            for card in deck.cards:
                self.cards.append(card)

    def shuffle(self):
        '''shuffle decks'''
        buffer=[]
        self.cards=[]
        for deck in self.decks:
            deck.shuffle()
            for card in deck.cards:
                self.cards.append(card)

        while(len(self.cards)):
            i = randint(0, len(self.cards)-1)
            card = self.cards.pop(i)
            buffer.append(card)
        print('I like to ... shuffle it!')
        self.cards = buffer

    def get_number_of_cards_with_faces_on(self):
        sum = 0
        for card in self.cards:
            sum = sum + 1 if card.is_turned_on() else sum
        return sum

    def pop_card(self):
        return self.cards.pop()

    def get_num_of_cards_from_deck(self):
        return len(self.cards)

    def __str__(self):
        # for card in self.cards:
        #     print(card)
        return 'BlackjackDeck'
