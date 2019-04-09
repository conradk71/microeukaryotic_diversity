import subprocess
import os

def Preprocess(input_file): 
    prefetch = "prefetch "
    dump = "fastq-dump "
    cwd = os.getcwd()
    exists = os.path.isfile(cwd+"/"+input_file)
    #checks if input file is in current path, redundant code since can't run the definition without it but whatever
    if exists:
        #read each line of input file for SRA#, check if SRA files already exist in path
        with open (input_file) as fp:
            line = fp.readline()
            try:
                exists2 = os.path.isfile(cwd+"/"+line)
                if exists2:
                #if the SRA file exists in cwd, run fastq dump
                    subprocess.run(dump + line)
                else:
                #else, prefetch and fastq dump the file
                    subprocess.run(prefetch + line)
                    subprocess.run(dump + line)
            except:
                print("Unexpected Error")
    else:
        print ("Requires Input File of SRA files in Current Path")