#!/usr/bin/env python
# -*- coding: utf-8 -*-

##### Written by Hadrien Gourlé. Feel free to use and modify #####
Description="Script that gives you the reverse complement of a sequence."
import argparse

parser=argparse.ArgumentParser(description=Description)
parser.add_argument("filetype",choices=["s","f"],
help="Filetype. Can be a fasta containing several sequences (f) or a single sequence passed to stdin (s)",metavar="[s], [f]")
parser.add_argument("Input",help="Input Sequence(s)", metavar="[Sequence]")

def rev_comp(s):
	bases={"a":"t","c":"g","g":"c","t":"a","y":"r","r":"y","w":"w","s":"s","k":"m","m":"k","n":"n","A":"T","C":"G",
	"G":"C","T":"A","Y":"R","R":"Y","W":"W","S":"S","K":"M","M":"K","N":"N"}
	seqlist=list(s)
	complist=[bases[b] for b in seqlist]
	comp="".join(complist)
	rcomp=comp[::-1] #extended slices method to reverse a string
	return rcomp

##Concatenate sequences -- easier for multifasta --
def fasta_formatter(Input):
	L=[]
	f=open(Input)
	for x in f.readlines():
		if x.startswith(">"):
			L.append("\n")
			L.append(x)
		else : 
			L.append(x.strip())
	Output="".join(L)
	return Output[1:]

def main():
	args=parser.parse_args()
	if args.filetype=="s":
		print rev_comp(args.Input)
	else:
		Fasta=fasta_formatter(args.Input).split("\n")
		for Seq in Fasta:
			if Seq[0]==">":print Seq
			else:print rev_comp(Seq) 

if __name__ == '__main__':
	main()
