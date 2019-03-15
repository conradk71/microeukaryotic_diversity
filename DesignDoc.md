# Design Document
### Microeukaryotic Diversity


## Overview
First, we will construct  an 18S rRNA gene database from the Protist Reference Ribosomal database (PR2) to be used in mothur. The PR2 Database provides access to unicellular eukaryotic, Small SubUnit rRNA, and rDNA sequences with curated taxonomy. The database is focused on nuclear-encoded sequences of protists. However, Metazoa, land plants and macrosporic fungi, as well as eukaryotic organelles are also included because of their use in Next Generation Sequencing dataset analyses. Since our study focuses around protists and small eukaryotic fractions, the database will be curated for this purpose. The database will also have to be rewritten into the native languages mothur is written in, mainly C/C++, to be used for downstream analysis. Then, we will conduct analyses of sample sequence data using mothur following SOP. Mothur will screen the data for sequencing and PCR errors, process the improved sequences, and align them to the designed database. We will calculate alpha and beta diversities amongst other statistical analyses of the species’ diversity/density.

## Context
More to be added over the weekend.

## Goals and Non-Goals
To be discussed in depth on Sunday March 17th.

## Milestones
Will also be discussed and set out over the Sunday meeting.

## Proposed Solution
STEP 1: Format Files:
* **Convert all the SRR files of the sample into fasta format**

STEP 2: Mothur:
* **Run the files through the command line, which will conduct analyses including alpha and beta diversity**

STEP 3: Analyses
* **Do statistical analyses on the data using R**

STEP 4: Compile the analyses 

