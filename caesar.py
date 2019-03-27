#!/usr/bin/env python3

import argparse
from colors import bcolors
import re


def generate_empty_table():
    """Generates a dictionary with no values to be used as a transtale table"""
    table = {}
    for i in range(ord('a'),ord('{')):
        table[chr(i)] = ""
    for i in range(ord('A'),ord('[')):
        table[chr(i)] = ""
    
    return table

def format_wordlist(dictionary):
    """Formats the wordlist removing \n in lowercase"""
    return [word.split()[0].lower() for word in dictionary]

def shift(text, n):
    """Shifts the text by n"""
    table = generate_empty_table()

    for key in table.keys():
        if key.isupper():
            mod = ord('[')
            reference = ord('A')
        else:
            mod = ord('{')
            reference = ord('a')
        new_value = (ord(key) + n) % mod
        if new_value < reference:
            new_value += reference
        table[key] = chr(new_value)

    trantab = str.maketrans("".join(table.keys()), "".join(table.values()))

    return text.translate(trantab)

# TODO: Need to consider the parsing. Marking the not alpha characters with red too??
def shift_all(text, dictionary):
    """Calls shift with all 25 possibilities. If a wordlist is used, it marks the matching words with red"""
    head = '[-] Original:'

    try:
        wordlist = format_wordlist(dictionary)
        regex = re.compile(r'[a-z]+|[A-Z]+', re.I)
    except:
        wordlist = []

    parsing = len(wordlist) != 0

    print("Parsing {}".format(parsing))

    print('='*max(len(head),len(text)), end='\n')
    print(head)
    print(text)
    print('='*max(len(head),len(text)), end='\n')

    for i in range(1,26):
        head = '[+] Shift = {}'.format(i)
        print(head)
        result = shift(text, i)
        for word in result.split():
            if parsing:
                p = regex.findall(word)[0]
                if regex.findall(word.lower())[0] in wordlist:
                    word = bcolors.FAIL + word + bcolors.ENDC
            print(word, end=" ")
        print()
        print('-'*max(len(head),len(text)))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple caesar cipher.')
    parser.add_argument('--all', action='store_true', help='shift of the caesar cipher')
    parser.add_argument('--shift', dest='shift', type=int, help='shift of the caesar cipher')
    parser.add_argument('--dict', dest='dict', type=argparse.FileType('r'), help='dictionary to use')
    parser.add_argument('text', type=str, help='text to cipher')
    args = parser.parse_args()

    if not args.all:
        print(shift(args.text, args.shift))
    else:
        shift_all(args.text, args.dict)
