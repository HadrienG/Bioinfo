#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
from Bio import SeqIO


def get_args():
    Description = 'RNA fasta to DNA fasta'
    parser = argparse.ArgumentParser(description=Description)
    parser.add_argument(
        'input',
        help='Input file',
    )
    args = parser.parse_args()
    return args


def rna_to_dna(input):
    with open(input, 'r') as f:
        rna = SeqIO.parse(f, "fasta")
        for record in rna:
            name, seq = record.id, str(record.seq)
            print('>%s\n%s' % (name, seq.replace('U', 'T')))


def main():
    args = get_args()
    rna_to_dna(args.input)


if __name__ == '__main__':
    main()
