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
                        '--outfile',
                        help='Output filename',
                        metavar='str',
                        type=str,
                        default='')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    out_arg = args.outfile
    pos_arg = args.positional

    str = ''

    if os.path.isfile(pos_arg):
        str = open(pos_arg).read().rstrip().upper()
    else:
        str = pos_arg.upper()

    if out_arg:
        out_fh = open(out_arg,'wt')
        print(str, file=out_fh)
        out_fh.close()
    else:
        print(str)


# --------------------------------------------------
if __name__ == '__main__':
    main()
