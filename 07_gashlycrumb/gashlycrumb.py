#!/usr/bin/env python3
"""
Author : fleide <fleide@localhost>
Date   : 2021-01-27
Purpose: Working with directories
"""

import argparse


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Gashly Crumbing',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('letter',
                        metavar='letter',
                        nargs='+', # 1 or more
                        help='Letter(s)')


    parser.add_argument('-f',
                        '--file',
                        help='A readable dictionary file',
                        metavar='FILE',
                        type=argparse.FileType('rt'),
                        default="gashlycrumb.txt")

    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    letters = args.letter
    dictionary_source = args.file

    dictionary = {}

    for line in dictionary_source:
        dictionary[line[0]] = line.rstrip()

    for letter in letters:
        print(dictionary.get(letter.upper(),letter+' is not found'))

# --------------------------------------------------
if __name__ == '__main__':
    main()
