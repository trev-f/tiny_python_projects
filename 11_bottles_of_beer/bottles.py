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

    print('\n\n'.join(map(verse, range(args.number, 0, -1))))

    #for num in range(args.number, 0, -1):
    #    ver = verse(num) + '\n' if num > 1 else verse(num)
    #   print(ver)


# --------------------------------------------------
def verse(bottle):
    """Sing a verse"""

    bot1 = 'bottles' if bottle > 1 else 'bottle'
    bot2 = 'bottles' if bottle - 1 != 1 else 'bottle'
    next_bottle = bottle - 1 if bottle != 1 else 'No more'

    return '\n'.join([
            f'{bottle} {bot1} of beer on the wall,',
            f'{bottle} {bot1} of beer,',
            'Take one down, pass it around,',
            f'{next_bottle} {bot2} of beer on the wall!'
        ])


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,', '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,', '2 bottles of beer,',
        'Take one down, pass it around,', '1 bottle of beer on the wall!'
    ])    


# --------------------------------------------------
if __name__ == '__main__':
    main()
