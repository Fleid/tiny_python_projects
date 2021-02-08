#!/usr/bin/env python3
"""
Author : fleide <fleide@localhost>
Date   : 2021-02-05
Purpose: Rock the Casbah
"""

import argparse
import os
import random
import string

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
    random.seed(args.seed)

    num_mutations = round(len(args.text) * args.mutations)
    alpha = ''.join(sorted(string.ascii_letters + string.punctuation))
    indexes = random.sample(range(len(args.text)), num_mutations)

    mutated = args.text
    for i in indexes:
        mutation = random.choice(alpha.replace(mutated[i],'')) #removing the current char from the options
        mutated = mutated[:i]+mutation+mutated[i+1:]


    print(f'You said: "{args.text}"')
    print(f'I heard : "{mutated}"')

# --------------------------------------------------
if __name__ == '__main__':
    main()
