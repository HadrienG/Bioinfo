#!/usr/bin/env python
# -*- coding: utf-8 -*-

#syntax : python CTG.py COORDS_FILE Input.fasta Output.fasta
#time for the Mycoplasma mycoides genome : 0.513s
#The COORDS_FILE is generated with MUMmer3.22 by mapping contigs against a reference genome.

#revcomp has now moved to biobox.pyc
#fasts_formatter has now moved to biobox.pyc
import biobox
from sys import argv as argv

#the following function parse a tab-delimited file generated with MUMmer3.22
#result is a list of ordered contigs. the function add an _R tag to contig that should be reversed
def list_contigs(COORD_FILE):
	L=[] #name of the contigs
	S=[] #length of the contigs
	R=[] #positive value if reverse sequence / negative either
	f=open(COORD_FILE)
	for i in range(5):f.readline()
	for x in f.readlines(): 
		line=x.split("|")
		name=line[6]
		length=line[2]
		data=">"+name.split()[1]
		seqlen=int(length.split()[1])
		rev=int(line[1].split()[0])-int(line[1].split()[1])
		if data not in L:
			L.append(data)
			S.append(seqlen)
			R.append(rev)
		else:
			pos=L.index(data)
			if seqlen>S[pos]:
				L.pop(pos)
				S.pop(pos)
				R.pop(pos)
				L.append(data)
				S.append(seqlen)
				R.append(rev)
	new_L=[]
	for s,r in zip(L,R):
		if r>0:s=s+"_R"
		new_L.append(s)
	return new_L

#the following function	generate a fasta file based on the contig list generated above
def fasta_sorter(COORD_FILE,Input):
	biobox.fasta_formatter(Input,"/tmp/%s.format"%Input)
	D={}
	f=open("/tmp/%s.format"%Input)
	name=f.readline()
	seq=f.readline()
	while seq:
		D[name.rstrip()]=seq.rstrip() #Dictionnary syntax : D[name of the contig]='sequence'
		name=f.readline()
		seq=f.readline()
	order=list_contigs(COORD_FILE)
	of=open("/tmp/%s.sort"%Input,"w")
	for x in order:
		of.writelines(x)
		of.writelines("\n")
		if x.endswith("_R"):
			x=x[:-2] #remove the "_R" in order to retrieve the right key in D
			rc=biobox.rev_comp(D[x])
			of.writelines(rc)
		else:of.writelines(D[x])
		of.writelines("\n")
	of.close()


COORD_FILE=argv[1]
Input=argv[2]
Output=argv[3]
fasta_sorter(COORD_FILE,Input)
biobox.ctg_merger("/tmp/%s.sort"%Input,Output)


