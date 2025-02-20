#!/usr/bin/env python3
"""
Author : treevooor <treevooor@localhost>
Date   : 2021-11-08
Purpose: Gashlycrumb
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashlycrumb',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        help='Letter(s)',
                        nargs='+')

    parser.add_argument('-f',
                        '--file',
                        help='Input file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default='gashlycrumb.txt')


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    gashlycrumb = {}
    for line in args.file:
        gashlycrumb.update({line[0].upper(): line.rstrip()})

    for letter in args.letter:
        if letter.upper() in gashlycrumb:
            print(gashlycrumb.get(letter.upper()))
        else:
            print(f'I do not know "{letter.upper()}".')
        

# --------------------------------------------------
if __name__ == '__main__':
    main()
