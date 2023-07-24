#!`which python3`
###
# File: reduce.py
# Author: Conlan Wesson
# License: GNU General Public License v3.0
###

import argparse

parser = argparse.ArgumentParser(description="Reduce dictionary to words of the proper length.")
parser.add_argument('-n', '--length', default=5, help="Length of words to keep.")
parser.add_argument('infile', help="Input dictionary filename.")
parser.add_argument('outfile', help="Output dictionary filename.")
args = parser.parse_args()

with open(args.outfile, 'w') as output:
    with open(args.infile, 'r') as words:
        for word in words:
            word = word.strip()
            if len(word) == args.length:
                output.write(word + '\n')

