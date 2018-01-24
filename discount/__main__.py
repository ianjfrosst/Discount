#!/usr/bin/env python3

import sys
import argparse
import discount.parser

if __name__ == "__main__":
    print("Version:", sys.version)

    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('--infile', '-i', default='tests/test.md')
    arg_parser.add_argument('--outfile', '-o')

    args = arg_parser.parse_args()

    file_in = open(args.infile, 'r')
    file_out = open(args.outfile, 'w') if args.outfile else sys.stdout
    discount.parser.parse(file_in, file_out)


else:
    raise Exception("Error: imported __main__ as module")
