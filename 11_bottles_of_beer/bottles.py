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



    verse = '\n'.join(['1 bottle of beer on the wall,',
             '1 bottle of beer,',
             'Take one down, pass it around,',
             'No more bottles of beer on the wall!'])

    print(verse)


def verse(bottle):
    """Sing a verse"""

    if bottle > 2:
        verse = '\n'.join([])
    elif bottle == 2:
        verse = '\n'.join([f'{bottle} bottles of beer on the wall,',
            f'{bottle} bottles of beer,',
            'Take one down, pass it around,',
            f'{bottle - 1} bottle of beer on the wall!'
        ])
    elif bottle == 1:
        verse = '\n'.join(['1 bottle of beer on the wall,',
            '1 bottle of beer,',
            'Take one down, pass it around,',
            'No more bottles of beer on the wall!'
        ])
    else:
        pass

    return verse


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
