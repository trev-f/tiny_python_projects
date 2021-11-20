#!/usr/bin/env python3
"""
Author : treevooor <treevooor@localhost>
Date   : 2021-11-20
Purpose: Bottles of beer song
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--number',
                        metavar='number',
                        help='How many bottles',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.number < 1:
        parser.error(f'--num "{args.number}" must be greater than 0')

    return args


# --------------------------------------------------
def main():
    """main program"""

    args = get_args()


# --------------------------------------------------
if __name__ == '__main__':
    main()
