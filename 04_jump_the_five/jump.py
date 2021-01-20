#!/usr/bin/env python3
"""
Author : fleide <fleide@localhost>
Date   : 2021-01-20
Purpose: Learning about dictionaries
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Jumping into dicts',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('str',
                        metavar='str',
                        help='A positional argument')

    return parser.parse_args()


# --------------------------------------------------
def main():

    args = get_args()
    pos_arg = args.str

    jumper = {'1': '9','2': '8','2': '8','3': '7','4': '6','5': '0','6': '4','7': '3','8': '2','9': '1','0': '5'}
    new_text = ''

    for char in pos_arg:
        new_text +=jumper.get(char, char)
    print(new_text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
