#!/usr/bin/env python3
"""
Author : fleide <fleide@localhost>
Date   : 2021-01-21
Purpose: 05 - Howler
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Howler howling',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional',
                        metavar='str',
                        help='A positional argument')

    parser.add_argument('-o',
                        '--on',
                        help='A boolean flag',
                        action='store_true')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    flag_arg = args.on
    pos_arg = args.positional

    str = ''

    if flag_arg:
        if os.path.isfile(pos_arg):
            str = open(pos_arg).read().rstrip().upper()
        else:
            #ERROR PATH
            print('This is not working')
    else:
        str = pos_arg.upper()

    print(str)


# --------------------------------------------------
if __name__ == '__main__':
    main()
