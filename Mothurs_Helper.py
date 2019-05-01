from itertools import product
import itertools
from Bio import SeqIO
from Bio.Seq import Seq
import os
import logging

def download_references():
    os.system("wget ftp://ftp.ncbi.nlm.nih.gov/refseq/TargetedLoci/Fungi/fungi.18SrRNA.fna.gz")
    os.system("gunzip fungi.18SrRNA.fna.gz")
    os.system("wget https://github.com/pr2database/pr2database/releases/download/4.11.1/pr2_version_4.11.1_mothur.fasta.gz")
    os.system("gunzip pr2_version_4.11.1_mothur.fasta.gz")
    os.system("wget https://github.com/pr2database/pr2database/releases/download/4.11.1/pr2_version_4.11.1_mothur.tax.gz")
    os.system("gunzip pr2_version_4.11.1_mothur.tax.gz")
    os.system("wget https://www.mothur.org/w/images/9/98/Silva.bacteria.zip")
    os.system("unzip Silva.bacteria.zip")

def Preprocess(input_SRA):
    path = input("Please input the path to your local installation of SRA Toolkit")
    ##path = "~/sratoolkit.2.9.0-centos_linux64/bin/"
    #need to find a way to avoid hard coding this, unfortunately can be difficult depending on installation of SRA toolkit
    prefetch = "prefetch "
    dump = "fastq-dump "
    cwd = os.getcwd()
    exists = os.path.isfile(cwd+"/"+input_SRA)
    #checks if input file is in current path, redundant code since can't run the definition without it but whatever
    if exists:
        #read each line of input file for SRA#, check if SRA files already exist in path
        with open (input_SRA) as fp:
            content = fp.read().splitlines()
        for line in content:
            exists2 = os.path.isfile(cwd+"/"+line)
            if exists2:
            #if the SRA file exists in cwd, run fastq dump
                logging.info("File: %s found, dumping", line)
                #subprocess.run(path + dump + line)
                os.system(path + dump + line)
                os.system()
                #subprocess command is erroring out, however the exact system call it makes works fine when manually
                #inputted into the shell...need to figure this out
            else:
            #else, prefetch and fastq dump the file
                #subprocess.run(path + prefetch + line)
                os.system(path + prefetch + line)
                logging.info("Prefetching: %s", line)
                #subprocess.run(path + dump + line)
                os.system(path + dump + line)
                logging.info("Dumping: %s", line)
    else:
        logging.error("Requires Input File of SRA files in Current Directory")
        print ("Requires Input File of SRA files in Current Path")

#definition to transcribe ambiguous bases
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
    print("Aligning Primers")
    inFile = "fungi.18SrRNA.fna"
    indices = list()
    ambigs = list()
    with open(input_file) as fp:
        #read primers into list content
        content = fp.read().splitlines()
        pr2len = len(content[1])
        #reverse complement of reverse primer
        rv = Seq(content[1])
        rc = rv.reverse_complement()
        content[1] = str(rc)

        for i in range(len(content)):
            for j in content[i]:
                #logic to replace ambiguous bases and fill the list with possible transcriptions
                if ( (j != "A") and (j !="T") and (j !="C") and (j != "G") ):
                    print ("Ambig Found: Converting and Testing")
                    results = tr_ambig(content[i])
                    results = list(results)
                    ambigs += results

    #append possible transcriptions to content list
    for i in range(len(ambigs)):
        content.append(ambigs[i])
    #attempting to find primers
    fw=open("Scerevisiae.fasta",'w')
    for record in SeqIO.parse(inFile,'fasta'):
        if record.id == "NG_063315.1":
            for i in range(len(content)):
                if (record.seq.find(content[i]) != -1):
                    print("Primer Found")
                    index = 0
                    index = record.seq.find(content[i])
                    indices.append(index)
                    print(indices)
            #logic to break loop, take min and max
            if (len(indices)==2):
                start = min(indices)
                end = max(indices) + pr2len
                record.seq = record.seq[start:end]
                SeqIO.write(record,fw,'fasta')
                print("Variable Region Identified")
                break
            break
            fw.close()

def run_mothur():
    path = os.getcwd()
    src=open("stability.batch","r")
    fline="set.dir = (input ="+path+")\n" #Prepending input directory for mother for batch file
    oline=src.readlines()
    #Here, we prepend the string we want to on first line
    oline.insert(0,fline)
    src.close()
    #We again open the file in WRITE mode
    src=open("stability.batch","w")
    src.writelines(oline)
    src.close()
    os.system("mothur stability.batch")
    
def run_R_scripts():
    os.system("Rscript Dendro.R")
def setup();
    path = os.getcwd()
    os.mkdir(path+'/Mothurs_Helper')
    os.chdir(path+'/Mothurs_Helper')
    path = os.getcwd()

setup()
path = os.getcwd()

print("Do you want to run the Mothurs_Helper with Test data? \n")
test = input("y/n?\n")
if test == "y":
    input_SRA = "sra_test.txt"
    input_file = "primer_test.txt"

else:
    print("For the following input files, make sure you have one element per line. Include the file ending '.txt'")
    print("These files should be located in the directory ~/18S_Mothur_Wrapper")
    input_SRA = input("Please enter the name of the text file containing your desired SRR files \n")
    input_file = input("Please enter the name of the text file containing your sequencing primers \n")

download_references()
Preprocess(input_SRA)
AlignPrimers(input_file)
run_mothur()
print("Please change the working directory of your installation of R to the ~/Mothurs_Helper \n")
rscript = input("Have you done this? y/n? \n")
if rscript == "y":
    run_R_scripts()
else:
    print("Please change the working directory of your installation of R to the ~/Mothurs_Helper \n")
