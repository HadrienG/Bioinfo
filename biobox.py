#!/usr/bin/env python
# -*- coding: utf-8 -*-

# "useful" bioinformatics tools

#Reverse complement of a sequence (input must be a string)
def rev_comp(s):
	bases={"a":"t","c":"g","g":"c","t":"a","y":"r","r":"y","w":"w","s":"s","k":"m","m":"k","n":"n","A":"T","C":"G",
	"G":"C","T":"A","Y":"R","R":"Y","W":"W","S":"S","K":"M","M":"K","N":"N"}
	seqlist=list(s)
	complist=[bases[b] for b in seqlist]
	comp="".join(complist)
	rcomp=comp[::-1] #extended slices method to reverse a string
	return rcomp

#Concatenate the sequences lines of a fasta file into only one for each entry (Input must be a fasta file, Output the name of the file that will be created)
def fasta_formatter(Input,Output):
	L=[]
	f=open(Input)
	for x in f.readlines():
		if x.startswith(">"):
			L.append("\n")
			L.append(x)
		else : 
			L.append(x.strip())
	newfasta="".join(L)
	of=open(Output,"w")
	of.writelines(newfasta[1:])
	of.close()

#merge contigs and put 5Ns between them (Input=fasta)
def ctg_merger(Input,Output):
	N="".join(["N" for x in range(5)])
	f=open(Input)
	of=open(Output,"w")
	name_ctg=f.readline()
	seq=f.readline()
	of.writelines(">assembly\n")
	while seq:
		of.writelines(seq)
		of.writelines(N)
		name_ctg=f.readline()
		seq=f.readline()
	of.close()