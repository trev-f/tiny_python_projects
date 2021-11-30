#!/usr/bin/env python3
"""
Author : treevooor <treevooor@localhost>
Date   : 2021-11-29
Purpose: Ransom Note
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Ransom Note',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        metavar='int',
                        type=int,
                        default=None,
                        help='Random seed')

    args = parser.parse_args()

    return args


# --------------------------------------------------
def main():
    """main program"""

    args = get_args()


# --------------------------------------------------
if __name__ == '__main__':
    main()
