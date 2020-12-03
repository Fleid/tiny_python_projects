#!/usr/bin/env python3
"""
Author : fleide <fleide@localhost>
Date   : 2020-12-02
Purpose: Say Hello
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Say Hello',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('-n',
                        '--name',
                        help='A name',
                        metavar='name',
                        type=str,
                        default='Universe')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    print('Hello ' + args.name + '!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
