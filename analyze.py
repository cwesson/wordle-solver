#!`which python3`
###
# File: analyze.py
# Author: Conlan Wesson
# License: GNU General Public License v3.0
###

import argparse

parser = argparse.ArgumentParser(description="Analyze dictionary to determine best words to guess.")
parser.add_argument('infile', help="Input dictionary filename.")
parser.add_argument('outfile', help="Output dictionary filename.")
args = parser.parse_args()

letters = {}
position = []

with open(args.infile, 'r') as words:
    for word in words:
        word = word.strip()
        for i in range(len(word)):
            letter = word[i]
            if letter in letters:
                letters[letter] += 1
            else:
                letters[letter] = 1
            
            if len(position) <= i:
                position.append({})
            
            if letter in position[i]:
                position[i][letter] += 1
            else:
                position[i][letter] = 1

scores = {}

scorefile = open(args.outfile, 'w')
with open(args.infile, 'r') as words:
    for word in words:
        word = word.strip()
        score = 0
        seen = []
        for i in range(len(word)):
            letter = word[i]
            score += position[i][letter]
            if letter not in seen:
                score += letters[letter]
                seen.append(letter)
        scores[word] = score
        scorefile.write("{}={}\n".format(word,score))
scorefile.close()

max_score = 0
max_word = ""
for word in scores:
    if scores[word] > max_score:
        max_score = scores[word]
        max_word = word

print(max_word)


