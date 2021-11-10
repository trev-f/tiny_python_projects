#!/usr/bin/env python3
"""
Author : treevooor <treevooor@localhost>
Date   : 2021-11-09
Purpose: Apples and bananas
"""

import argparse
import os


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to subsitutue',
                        metavar='vowel',
                        type=str,
                        choices=['a', 'e', 'i', 'o', 'u'],
                        default='a')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    vowels = 'aeiou'

    out_text = ''
    for letter in args.text:
        if letter.lower() in vowels:
            if letter.islower():
                out_text += letter.replace(letter, args.vowel)
            else:
                out_text += letter.replace(letter, args.vowel.upper())
        else:
            out_text += letter

    print(out_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
