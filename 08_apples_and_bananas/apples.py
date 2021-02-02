#!/usr/bin/env python3
"""
Author : fleide <fleide@localhost>
Date   : 2021-01-27
Purpose: Chapter 08 - Find and replace strings
"""

import argparse
import os

# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

    parser = argparse.ArgumentParser(
        description='Apples and Bananas',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    parser.add_argument('text',
                        metavar='text',
                        type=str,
                        help='Input text or file')

    parser.add_argument('-v',
                        '--vowel',
                        help='The vowel to substitute, default (a)',
                        metavar='vowel',
                        type=str,
                        choices=['a','e','i','o','u'],
                        default='a')

    args = parser.parse_args()

    if os.path.isfile(args.text):
        args.text = open(args.text).read().rstrip()

    return args


# --------------------------------------------------
def main():
    """Find and replace strings"""

    args = get_args()
    text= args.text
    v = args.vowel

    vowels=['a','e','i','o','u']
    for vowel in vowels:
        text = text.replace(vowel,v)
        text = text.replace(vowel.upper(),v.upper())

    print(text)


# --------------------------------------------------
if __name__ == '__main__':
    main()
