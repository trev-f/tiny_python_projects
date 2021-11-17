#!/usr/bin/env python3
"""
Author : treevooor <treevooor@localhost>
Date   : 2021-11-15
Purpose: Telephone
"""

import argparse
import os
import random
import string


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Telephone',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        help='Input text or file')

    parser.add_argument('-s',
                        '--seed',
                        metavar='seed',
                        help='Random seed',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        metavar='mutations',
                        help='Percent mutations',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    if not 0 <= args.mutations <= 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    return args


# --------------------------------------------------
def main():
    """main program"""

    args = get_args()

    # set number mutations
    n_mutations = round(len(args.text) * args.mutations)

    # define mutation space
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))

    # randomly sample characters to change
    random.seed(args.seed)
    indexes = random.sample(range(len(args.text)), n_mutations)

    mut_text = args.text
    for i in indexes:
        mut_char = random.choice(alpha.replace(mut_text[i], ''))

        mut_text = mut_text[:i] + mut_char + mut_text[i+1:]

    # print what was said and what was heard
    print(f'You said: "{args.text}"')
    print(f'I heard : "{mut_text}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
