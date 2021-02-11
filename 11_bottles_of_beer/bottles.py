#!/usr/bin/env python3
"""
Author : fleide <fleide@localhost>
Date   : 2021-02-11
Purpose: Chapter 11
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Bottles of beer song',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--num',
                        help='How many bottles',
                        metavar='number',
                        type=int,
                        default=10)

    args = parser.parse_args()

    if args.num < 1:
        parser.error(f'--num "{args.num}" must be greater than 0')

    return args


# --------------------------------------------------
def verse(bottle):
    """Sing a verse"""

    first = 's' if bottle > 1 else ''
    second = '' if bottle == 2 else 's'
    last = 'No more' if bottle == 1 else bottle-1

    return '\n'.join([
        f'{bottle} bottle{first} of beer on the wall,',
        f'{bottle} bottle{first} of beer,',
        'Take one down, pass it around,',
        f'{last} bottle{second} of beer on the wall!'
    ])


# --------------------------------------------------
def test_verse():
    """Test verse"""

    last_verse = verse(1)
    assert last_verse == '\n'.join([
        '1 bottle of beer on the wall,',
        '1 bottle of beer,',
        'Take one down, pass it around,',
        'No more bottles of beer on the wall!'
    ])

    two_bottles = verse(2)
    assert two_bottles == '\n'.join([
        '2 bottles of beer on the wall,',
        '2 bottles of beer,',
        'Take one down, pass it around,',
        '1 bottle of beer on the wall!'
    ])


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    num_list = list(range(args.num, 0, -1))
    for i in num_list:
        print(verse(i) + ('\n' if i > 1 else ''))


# --------------------------------------------------
if __name__ == '__main__':
    main()
