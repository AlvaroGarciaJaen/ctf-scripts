#!/usr/bin/env python3

import argparse

table = {}

def set_empty_table():
    for i in range(ord('a'),ord('{')):
        table[chr(i)] = ""
    for i in range(ord('A'),ord('[')):
        table[chr(i)] = ""

def shift(n, text):
    set_empty_table()

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

def shift_all(text):
    print('='*len(text), end='\n')
    print('Original:')
    print(text)
    print('='*len(text), end='\n\n')

    for i in range(1,26):
        print('Shift = {}'.format(i))
        print(shift(i, text))
        print('-'*len(text))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Simple caesar cipher.')
    parser.add_argument('--all', action='store_true', help='shift of the caesar cipher')
    parser.add_argument('--shift', dest='shift', type=int, help='shift of the caesar cipher')
    parser.add_argument('text', type=str, help='text to cipher')
    args = parser.parse_args()

    if not args.all:
        print(shift(args.shift, args.text))
    else:
        shift_all(args.text)
