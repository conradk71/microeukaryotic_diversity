import subprocess
import os
import logging

logging.basicConfig(filename='PreProcess.log',level=logging.DEBUG)

def Preprocess(input_file):
    path = "~/sratoolkit.2.9.0-centos_linux64/bin/"
    #need to find a way to avoid hard coding this, unfortunately can be difficult depending on installation of SRA toolkit
    prefetch = "prefetch "
    dump = "fastq-dump "
    cwd = os.getcwd()
    exists = os.path.isfile(cwd+"/"+input_file)
    #checks if input file is in current path, redundant code since can't run the definition without it but whatever
    if exists:
        #read each line of input file for SRA#, check if SRA files already exist in path
        with open (input_file) as fp:
            line = fp.readline()
            line = line.rstrip()
            exists2 = os.path.isfile(cwd+"/"+line)
            if exists2:
            #if the SRA file exists in cwd, run fastq dump
                logging.info("File: %s found, dumping", line)
                #subprocess.run(path + dump + line)
                os.system(path + dump + line)
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
        logging.error("Requires Input File of SRA files in Current Path")
        print ("Requires Input File of SRA files in Current Path")

Preprocess("sra_test.txt")
