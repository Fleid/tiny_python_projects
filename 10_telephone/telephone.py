#!/usr/bin/env python3
"""
Author : fleide <fleide@localhost>
Date   : 2021-02-05
Purpose: Rock the Casbah
"""

import argparse
import os

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
                        help='Random seed',
                        metavar='int',
                        type=int,
                        default=None)

    parser.add_argument('-m',
                        '--mutations',
                        help='Percent mutations',
                        metavar='float',
                        type=float,
                        default=0.1)

    args = parser.parse_args()

    if args.mutations < 0 or args.mutations > 1:
        parser.error(f'--mutations "{args.mutations}" must be between 0 and 1')

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    str_arg = args.arg
    int_arg = args.int
    file_arg = args.file
    flag_arg = args.on
    pos_arg = args.positional

    print(f'str_arg = "{str_arg}"')
    print(f'int_arg = "{int_arg}"')
    print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
    print(f'flag_arg = "{flag_arg}"')
    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
