#!/usr/bin/env python3
"""
Author : fleide <fleide@localhost>
Date   : 2020-12-03
Purpose: Rock the Casbah
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Look out matey!',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('positional', #name of the parameter in the program
                        metavar='mob', #name of the parameter for the caller
                        help='A mobile object ahead')

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()

    output_message = 'Ahoy, Captain, a '+ args.positional +' off the larboard bow!'
    print(output_message)


# --------------------------------------------------
if __name__ == '__main__':
    main()
