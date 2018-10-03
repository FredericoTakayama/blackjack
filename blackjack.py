#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# blackjack - project2 study python

import os

from deck import Deck, Card
from blackjack_deck import BlackjackDeck
from player import Player
# from wallet import Wallet # not necessary since player already imports it
from enum import Enum


class GamePlay(object):
    def __init__(self):
        self.game_on = True
        self.game_start = True
        self.state = 0

    def gretting_display(self):
        print('_____________________________________')
        print('___________  blackjack  _____________')
        print('_____________________________________')
        print('')    
    
    @staticmethod
    def has_bursted(player):
        return True if player.get_sum_from_cards() > 21 else False
    
    @staticmethod
    def got_blackjack(player):
        return True if player.get_sum_from_cards() == 21 else False

    @staticmethod
    def check_winner_from_round(player,dealer):
        if GamePlay.got_blackjack(player) or GamePlay.has_bursted(dealer):
            return 1 # player wins
        elif GamePlay.got_blackjack(dealer) or GamePlay.has_bursted(player) :
            return -1 # dealer wins
        elif player.get_sum_from_cards() > dealer.get_sum_from_cards():
            return 1
        elif player.get_sum_from_cards() < dealer.get_sum_from_cards():
            return -1
        else:
            return 0 # tie
    
    @staticmethod
    def press_any_key():
        input("Press Enter to continue...")

class phases(Enum):
    BET_PHASE = 0
    PLAYER_PHASE_1 = 1
    PLAYER_PHASE_2 = 3
    DEALER_PHASE = 4
    TIE = 5
    PLAYER_WON = 6
    DEALER_WON = 7
    CHECK_WALLETS = 8

if __name__ == "__main__":
    gameplay = GamePlay()

    while(gameplay.game_on):
        gameplay.gretting_display()
        bj_deck=BlackjackDeck()
        bj_deck.shuffle()
        # print(bj_deck)
        player = Player('player')
        dealer = Player('dealer')
        
        gameplay.game_start = True
        gameplay.state = phases.BET_PHASE

        while(gameplay.game_start):

            if gameplay.state == phases.BET_PHASE:
                # clean hands
                player.clean_hand()
                dealer.clean_hand()

                # check if its necessary to change to a new deck
                # this bj_dec has two decks, so when get half of it, refresh it
                if bj_deck.get_num_of_cards_from_deck() <= 52:
                    # change to a new deck
                    bj_deck=BlackjackDeck()
                    bj_deck.shuffle()

                print(player.wallet)
                print(dealer.wallet)
                try:
                    bet = int(input('How much do you wanna bet? '))
                    if bet <= player.wallet.check_money() and bet <= dealer.wallet.check_money():
                        player.wallet.subtract(bet)
                        dealer.wallet.subtract(bet)
                        bet *= 2
                        gameplay.state = phases.PLAYER_PHASE_1
                    else:
                        print('invalid bet, please select a valid value')
                except:
                    print('invalid entry, please select a valid value')

            elif gameplay.state == phases.PLAYER_PHASE_1:
                print('_____________________________________')
                # player receives 2 cards:*
                print('Player receives 2 cards:')
                for i in range(0,2):
                    player.pick_card(bj_deck.pop_card())
                player.show_hand()
                # check if already got a blackjack:
                if GamePlay.got_blackjack(player):
                    print('Blackjack!')
                    gameplay.state = phases.PLAYER_WON
                else:
                    gameplay.state = phases.PLAYER_PHASE_2

            elif gameplay.state == phases.PLAYER_PHASE_2:
                res = input('(w)ait or (p)ick another card? ')
                if res == 'w':
                    gameplay.state = phases.DEALER_PHASE
                elif res == 'p':
                    player.pick_card(bj_deck.pop_card())
                    player.show_hand()

                    # check if already got a blackjack:
                    if GamePlay.got_blackjack(player):
                        gameplay.state = phases.PLAYER_WON
                    elif player.get_sum_from_cards() > 21: # check if bursted:
                        gameplay.state = phases.DEALER_WON
                else:
                    print('invalid entry, please choose again')

            elif gameplay.state == phases.DEALER_PHASE: # Dealer phase
                print('_____________________________________')
                print('Now its Dealer phase!!!!!')
                print('Dealer picks 2 cards:')
                # dealer picks 2 cards:
                for i in range(0,2):
                    dealer.pick_card(bj_deck.pop_card())
                dealer.show_hand()

                # dealer can take up to 5 cards and need to stop when equal or above value 17:
                while (dealer.get_sum_from_cards() < 17 and len(dealer.cards) < 5):
                    print('dealer pick a card:')
                    dealer.pick_card(bj_deck.pop_card())
                    dealer.show_hand()

                # check win/lost
                print('_____________________________________')
                res = GamePlay.check_winner_from_round(player,dealer)
                if res > 0:
                    gameplay.state = phases.PLAYER_WON
                elif res < 0:
                    gameplay.state = phases.DEALER_WON
                else:
                    gameplay.state = phases.TIE

            # Ending Phases
            elif gameplay.state == phases.TIE:
                print('Tie!')
                player.pay_bet(bet/2.0)
                dealer.pay_bet(bet/2.0)
                gameplay.state = phases.CHECK_WALLETS
                GamePlay.press_any_key()

            elif gameplay.state == phases.PLAYER_WON:
                print('Player won!')
                player.pay_bet(bet)
                gameplay.state = phases.CHECK_WALLETS
                GamePlay.press_any_key()
            
            elif gameplay.state == phases.DEALER_WON:
                print('Player lose!')
                dealer.pay_bet(bet)
                gameplay.state = phases.CHECK_WALLETS
                GamePlay.press_any_key()
            
            elif gameplay.state == phases.CHECK_WALLETS:
                # se player zerou:
                if float(player.wallet.check_money()) == 0.0:
                    print('Oh no man, too bad. Good luck next time..')
                    print('Game over')
                    gameplay.game_start = False
                # se dealer zerou:
                elif float(dealer.wallet.check_money()) == 0.0:
                    print('Breaking the bank! Player won the house!')
                    print('Game over')
                    gameplay.game_start = False
                # se ninguem zerou
                else:                
                    gameplay.state = phases.BET_PHASE
                    os.system('cls' if os.name == 'nt' else 'clear') # clear terminal

            else:
                print("invalid phase. It shouldn't be here..")
   
        res = input('Start a new Game(y/n): ')
        gameplay.game_on = True if res == 'y' else False
        os.system('cls' if os.name == 'nt' else 'clear') # clear terminal
