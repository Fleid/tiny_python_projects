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

    print(f'positional = "{pos_arg}"')


# --------------------------------------------------
if __name__ == '__main__':
    main()
