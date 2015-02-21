#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Written by Hadrien Gourlé. Feel free to use and modify"""

import random
import argparse


def parser():
	Description = "Reservoir sampling for NGS Data."
	parser = argparse.ArgumentParser(description=Description)
	parser.add_argument(
						"infile",
						help="Input file",
						metavar="[file.fastq]"
						)
	parser.add_argument(
						"--outfile",
						"-o",
						default="sample.fastq",
						help="Output File (default: %(default)s)"
						)
	parser.add_argument(
						"--size",
						"-s",
						type=int,
						default=10,
						help="Desired size of the sample (default: %(default)s)",
						metavar="[int]"
						)

	args = parser.parse_args()
	return args

def sampling(args):
	Infile = open(args.infile, "r")
	Outfile = open(args.outfile, "w")
	Size = args.size
	Samples = []

	random.seed(1.2345)
	Nreads = sum(1 for _ in Infile)/4
	Samples = sorted([random.randint(0, Nreads-1) for s in xrange(Size)])

	x = 0
	Infile = open(args.infile)
	for sample in sorted(Samples):
		while x < sample:
			x += 1
			for i in range(4):
				Infile.readline()
		for i in range(4):
			Outfile.write(Infile.readline())
		x += 1
	Infile.close()
	Outfile.close()


def main():
	args=parser()
	sampling(args)


if __name__ == '__main__':
	main()
