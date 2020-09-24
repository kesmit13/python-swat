#!/usr/bin/env python

'''
Return a random hostname from the specified collection of names

'''

import argparse
import itertools
import os
import random
import re
import sys


def main(args):
    ''' Main routine '''
    out = []
    for arg in args.host_expr:
        parts = [x for x in re.split(r'(?:\[|\])', arg) if x]

        for i, part in enumerate(parts):
            if ',' in part:
                parts[i] = re.split(r'\s*,\s*', part)
            elif re.match(r'^\d+\-\d+$', part):
                start, end = part.split('-')
                width = len(start)
                start = int(start)
                end = int(end)
                parts[i] = [('%%0%sd' % width) % x for x in range(start, end + 1)]
            else:
                parts[i] = [part]

        out += list(''.join(x) for x in itertools.product(*parts))

    print(random.choice(out))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__.strip())

    parser.add_argument('host_expr', type=str, metavar='hostname-expr', nargs='+',
                        help='hostname expression (ex. myhost[01-06].com)')

    args = parser.parse_args()

    main(args)
