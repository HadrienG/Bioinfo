#!/usr/bin/env/python3
# -*- coding: utf-8 -*-


import argparse
import re
from Bio import SeqIO
from Bio.Seq import Seq
from Bio.SeqRecord import SeqRecord
from Bio.Alphabet import IUPAC


def _get_args():
    description = 'find rRNAs, tRNAs annd mtRNAs in a gff and extract dna \
    sequences from an associated fasta file'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
                        '--gff',
                        '-g',
                        help='gff file',
                        required=True
                        )
    parser.add_argument(
                        '--fasta',
                        '-f',
                        help='fasta file',
                        required=True
                        )
    parser.add_argument(
                        '--output',
                        '-o',
                        help='output file',
                        required=True
                        )
    args = parser.parse_args()
    return args


def extract_pos_from_gff(gff):
    """This function parses a gff file and extract the positions of any RNAs
    annotated with the format [a-zA-Z]{1,2}RNA (rRNA, tRNA, mtRNA, ...)

    Arg(s):
        gff         a gff file

    Returns:
        RNAs_dic   a dictionnary of the format {id: (description,start,end)}"""
    regex = re.compile('\t[a-zA-Z]{1,2}RNA')
    RNAs_dic = {}
    with open(gff, 'r') as gff_file:
        for line in gff_file:
            if re.search(regex, line):
                feature = line.rstrip().split('\t')
                id = feature[8].split(';')[0]
                name = feature[8].split(';')[1]
                RNAs_dic[id] = (name, feature[3], feature[4])
    return(RNAs_dic)


def extract_rna_sequences(dict, fasta, output):
    """This function extract sequences from a fasta file and writes them to a file

    Arg(s):
        dic         a dictionnary of the format {id: (description,start,end)}
        fasta       a fasta file

    Returns:
        0"""
    with open(fasta, 'r') as f, open(output, 'w') as output:
        fasta_file = SeqIO.parse(f, 'fasta')
        for record in fasta_file:
            for id, attr in dict.items():
                seq = SeqRecord(
                                Seq(str(record.seq[int(attr[1]):int(attr[2])]),
                                    IUPAC.unambiguous_dna
                                    ),
                                id=id,
                                description=attr[0]
                                )
                SeqIO.write(seq, output, "fasta")
    return 0


def main():
    arguments = _get_args()
    positions = extract_pos_from_gff(arguments.gff)
    extract_rna_sequences(positions, arguments.fasta, arguments.output)

if __name__ == '__main__':
    main()
