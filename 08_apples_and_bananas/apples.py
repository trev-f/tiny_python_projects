#!/usr/bin/env python3
"""
Author : treevooor <treevooor@localhost>
Date   : 2021-11-09
Purpose: Apples and bananas
"""

import argparse


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


    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()


# --------------------------------------------------
if __name__ == '__main__':
    main()
