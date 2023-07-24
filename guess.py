#!`which python3`
###
# File: guess.py
# Author: Conlan Wesson
# License: GNU General Public License v3.0
###

import argparse

parser = argparse.ArgumentParser(description="Make guesses at the Wordle solution.")
parser.add_argument('infile', help="Input dictionary filename.")
args = parser.parse_args()

class Rule:
    def check(self, word):
        return False

class Keep(Rule):
    def __init__(self, letter, position):
        self._letter = letter
        self._position = position
    
    def check(self, word):
        return word[self._position] == self._letter
    
    def __str__(self):
        return "Keep {} at {}".format(self._letter, self._position)

class Move(Rule):
    def __init__(self, letter, position, exceptions):
        self._letter = letter
        self._position = position
        self._exceptions = exceptions
    
    def check(self, word):
        if word[self._position] == self._letter:
            return False
        pos = word.find(self._letter)
        return (pos != -1) and (pos not in self._exceptions)
    
    def __str__(self):
        return "Move {} from {}".format(self._letter, self._position)

class NotIn(Rule):
    def __init__(self, letter, exceptions):
        self._letter = letter
        self._exceptions = exceptions
    
    def check(self, word):
        pos = word.find(self._letter)
        while pos in self._exceptions:
            pos = word.find(self._letter, pos+1)
        return pos == -1
    
    def __str__(self):
        return "Not {}".format(self._letter)

words = {}
with open(args.infile, 'r') as infile:
    for word in infile:
        word = word.strip()
        (word, score) = word.split('=')
        words[word] = int(score)

log = open("rules.log", 'w')
keeps = set()
moves = set()
while True:
    if len(words) == 0:
        print("No more guesses")
        break
    max_score = 0
    for word in words:
        if words[word] > max_score:
            max_score = words[word]
            guess = word
    
    print("Guess -> {}".format(guess))
    words.pop(guess)
    
    state = input("state =? ")
    if state != "":
        rules = []
        for pos in range(len(state)):
            r = state[pos]
            letter = guess[pos]
            if r == 'k':
                # Keep in this position
                rules.append(Keep(letter, pos))
                keeps.add(pos)
            elif r == 'm':
                # Move to another position
                rules.append(Move(letter, pos, keeps))
                moves.add(letter)
            elif letter not in moves:
                # Not in word
                rules.append(NotIn(letter, keeps))
        
        new_words = {}
        for word in words:
            accept = True
            for rule in rules:
                if not rule.check(word):
                    accept = False
                    log.write("{} -> {}\n".format(word, rule))
                    break
            if accept:
                new_words[word] = words[word]
        
        words = new_words

log.close()

