#!/usr/bin/env python3
"""
Author : fleide <fleide@localhost>
Date   : 2020-12-04
Purpose: Picnic
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('foods',
                        metavar='foods',
                        nargs='+', # we can take more than one
                        help='Item(s) to bring')

    parser.add_argument('-s',
                        '--sorted',
                        help='Sort the items (default: False)',
                        action='store_true') # magic!

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    sorted = args.sorted
    foods = args.foods

    if (len(foods) == 1):
        print(f'You are bringing {foods[0]}.')
    elif (len(foods) == 2):
        print(f'You are bringing {foods[0]} and {foods[1]}.')
    else:
        last_food = foods.pop(-1)
        comma_sep_list = ', '.join(foods)
        print(f'You are bringing {comma_sep_list}, and {last_food}.')


# --------------------------------------------------
if __name__ == '__main__':
    main()
