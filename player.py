#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from wallet import Wallet

class Player(object):
    def __init__(self, name):
        self.wallet = Wallet(100, name)
        self.cards = []
        self.name = name

    def pick_card(self, card):
        self.cards.append(card)

    def clean_hand(self):
        self.cards = []
    
    def get_sum_from_cards(self):
        '''retorna a soma das cartas de acordo com a regra do blackjack'''
        sum = 0
        aces = 0 # guarda a quantidade de aces
        for card in self.cards:
            number = card.number
            if number == 1: # se for ace:
                aces += 1
            elif number > 10:
                sum += 10
            else:
                sum += number

        if aces:
            sum += sum + aces - 1 # soma a quantidade de aces -1
            if (sum + 11) <= 21:
                sum += 11
            else:
                sum += 1

        return sum

    def show_hand(self):
        print('Cards from %s' % (self.name))
        for card in self.cards:            
            print(card)
        print('sum: %d' % self.get_sum_from_cards())

    def pay_bet(self,bet):
        self.wallet.add(bet)

    def show_wallet(self):
        print(self.wallet)
