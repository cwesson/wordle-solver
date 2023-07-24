# Wordle Solver
There are three scripts to help solve Wordle: reduce.py, analyze.py, and guess.py.  Reduce and analyze operate on files
containing a newline separated list of words.  Analyze outputs a file containing each word and its score separated by
and equal sign ("=") on separate lines.  Guess uses the output of analyze to determine the best words to pick.  The user
must enter feedback for each word as one character per character in the words.  "k" (keep) indicates the letter must
appear in that position (green in Wordle).  "m" (move) indicates the letter appears in the word but not in that position
(yellow in Wordle).  "n" (not) indicates the letter does not appear again in the word (gray in Wordle).

This has been tested with words of up to 11 letters.

## reduce.py
Reduces the dictionary to words of the proper length.

## analyze.py
Analyzes the words and assigns each word a score.  Words with the most common letters, and letters that most often
appear in the same position most are weighted higher.  Words with duplicate letters are weighted lower.  Using this for
5 letter words, the script finds "tares" as the first word to choose.  Intuitively this makes sense.  It has and "e",
"t", and "a", the three most common letters in English.  It also ends in an "s" which is common as many words will be
the plural form of four letter words.  Additionally, words ending in "es" are fairly common.

## guess.py
Makes guesses at the Wordle solution.  The user must enter feedback for each word.  For each letter in the word, enter
one of the following:
* k - (green) keep the letter at this position.
* m - (yellow) move the letter to a different position.
* n - (gray) not in the word again.

If the word is not found by Wordle, simply press enter with no feedback.

This works by building a set of rules based on the feedback.  It checks each word on the list against the rules and
removes any words that violate a rule.  It then picks the word with the highest score as the next guess.  It also
outputs a log, rules.log, for debugging.  The log contains all the words eliminated from consideration along with the
reason they were removed.

## words_alpha.txt
This word list is from https://github.com/dwyl/english-words, it is licensed under The Unlicense.

