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

    if sorted:
        foods.sort()

    bringing = ''
    if (len(foods) == 1):
        bringing = foods[0]
    elif (len(foods) == 2):
        bringing = f'{foods[0]} and {foods[1]}'
    else:
        last_food = foods.pop(-1)
        bringing = ', '.join(foods) + f', and {last_food}'

    print(f'You are bringing {bringing}.')

# --------------------------------------------------
if __name__ == '__main__':
    main()
