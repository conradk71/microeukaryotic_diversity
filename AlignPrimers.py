#degenerate primers
from Bio import SeqIO
from Bio.Seq import Seq
from Bio import motifs
from Bio.SeqUtils import nt_search
from Bio.Data import CodonTable
from itertools import product
import itertools
from Bio import Alphabet 
from Bio.Alphabet import IUPAC
from Bio.Data import IUPACData 

inFile = open('NG_063315.1.fasta','r')               

#definition to switch ambiguous bases
def tr_ambig(s):
    ambig = {"R": ["A", "G"], "V":["A", "C", "G"], "Y": ["C", "T"], "S": ["C", "G"], "W": ["A", "T"], "K": ["G", "T"], "M":["A", "C"], "B":["C","G","T"], "D":["A", "G", "T"], "H":["A", "C", "T"]}
    groups = itertools.groupby(s, lambda char:char not in ambig)
    splits = []
    for b,group in groups:
        if b:
            splits.extend([[g] for g in group])
        else:
            for nuc in group:
                splits.append(ambig[nuc])
    answer = [''.join(p) for p in itertools.product(*splits)]
    return answer

#definition to perform alignment of primers and extract variable region
def AlignPrimers(input_file):
    indices = list()
    ambigs = list()
    with open(input_file) as fp:
        content = fp.read().splitlines()
        pr2len = len(content[1])
        rv = Seq(content[1])
        rc = rv.reverse_complement()
        content[1] = str(rc)

        for i in range(len(content)):
            for j in content[i]:
                if ( (j != "A") and (j !="T") and (j !="C") and (j != "G") ):
                    print ("Ambig Found: Converting and Testing")
                    results = tr_ambig(content[i])
                    results = list(results)
                    ambigs += results
                    ##for k in range(len(results)):
                        ##i = int(i)
                        ##content.insert(i,results[k])
    
    for i in range(len(ambigs)):
        content.append(ambigs[i])
    
    fw=open("Scervisiae.fasta",'w')
    for record in SeqIO.parse(inFile,'fasta'):
        for i in range(len(content)):
            if (record.seq.find(content[i]) != -1):
                print("Primer Found")
                index = 0
                index = record.seq.find(content[i])
                indices.append(index)
    
    if (len(indices)==2):
        start = min(indices)
        end = max(indices) + pr2len
        record.seq = record.seq[start:end]
        SeqIO.write(record,fw,'fasta')
        print("Variable Region Identified")
    fw.close()
         
            
AlignPrimers("primer_test.txt")