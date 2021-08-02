#!/bin/python3

#Teminal coin flip because im broke and dont have real money :)

#importing libs
import random
import string

#the coin flip function uses random choice from .random lib.
def flipCoin():
	return random.choice(["HEAD","TAILS"])
print(flipCoin())
