#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Wallet(object):
    def __init__(self, value, player_name):
        self.money=value
        self.player_name = player_name

    def add(self, value):
        self.money += value
    
    def check_money(self):
        return self.money
    
    def subtract(self, value):
        if value <= self.money:
            self.money -= value
            return 0
        return -1

    def is_broken(self):
        return (self.check_money() <= 0)

    def __str__(self):
        return 'wallet from %s: %d' % (self.player_name, self.money)