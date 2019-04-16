
# coding: utf-8

# In[ ]:

import os
from subprocess import call

directory = os.popen('pwd').read().rstrip()

current_direct = (directory + '/Mothur_Output/')

os.system('mkdir ' + current_direct)

os.chdir(current_direct)

call(['mothur','#make.file(inputdir=., type=fastq, prefix=stability)'])

call(['mothur','#make.contigs(file=stability.files, processors=8)'])

call(['mothur','#summary.seqs(fasta=stability.trim.contigs.fasta)'])

call(['mothur','#screen.seqs(fasta=stability.trim.contigs.fasta, group=stability.contigs.groups, maxambig=0, maxlength=486)'])

call(['mothur','#unique.seqs(fasta=stability.trim.contigs.good.fasta)'])

call(['mothur','#count.seqs(name=stability.trim.contigs.good.names, group=stability.contigs.good.groups)'])

call(['mothur','#summary.seqs(count=stability.trim.contigs.good.count_table)'])

call(['mothur','#align.seqs(fasta=scerevisiae_v7_v8.fasta, reference=silva.nr_v132.align)'])

call(['mothur','#summary.seqs(fasta=scerevisiae_v7_v8.align)'])

call(['mothur','#pcr.seqs(fasta=silva.nr_v132.align, start=29689, end=42545, keepdots=F)'])

call(['mothur','#summary.seqs(fasta=silva.nr_v132.pcr.align)'])

call(['mothur','#align.seqs(fasta=stability.trim.contigs.good.unique.fasta, reference=silva.nr_v132.pcr.align)'])

call(['mothur','#summary.seqs(fasta=stability.trim.contigs.good.unique.align, count=stability.trim.contigs.good.count_table)'])

call(['mothur','#screen.seqs(fasta=stability.trim.contigs.good.unique.align, count=stability.trim.contigs.good.count_table, summary=stability.trim.contigs.good.unique.$

call(['mothur','#summary.seqs(fasta=current, count=current)'])

