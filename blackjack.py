#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# blackjack - project2 study python

import os
from deck import Deck, Card

def gretting_display():
    print('_____________________________________')
    print('___________  blackjack  _____________')
    print('_____________________________________')
    print('')

if __name__ == "__main__":    
    gretting_display()
    deck=Deck()
    card=Card()
    print(card)
    
    # TODO
    # criar objeto deck (generico)*
    # criar objeto blackjackdeck (com regras do blackjack) 
    #   com pontuações das cartas e soma de valores, estouro de pontuacao, blackjack (21), win, lose partida
    # criar objeto wallet
    #   guardar valor, checar valor, receber valor, checar se esta sem dinheiro
    # criar objeto player 
    #   (com composicao de wallet e uma mao (lista de cartas em posse) e funcoes: wait ou pedir)
    # criar objeto dealer (herda de player) 
    #   com metodo new_bj_deck (descarta deck anterior e pega um novo)
    #   o dealer so pode pedir ate 5 cartas ou chegar ate 17
    #   new_bj_deck: usar quando o deck chegar na metade do numero de cartas usado (ou mais, quando terminar uma partida)

    # criar funcao gameplay
    #   desenvolver estrutura principal que envolva todos os objetos
