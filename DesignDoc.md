# Design Document
### Microeukaryotic Diversity


## Overview
First, we will construct  an 18S rRNA gene database from the Protist Reference Ribosomal database (PR2) to be used in mothur. The PR2 Database provides access to unicellular eukaryotic, Small SubUnit rRNA, and rDNA sequences with curated taxonomy. The database is focused on nuclear-encoded sequences of protists. However, Metazoa, land plants and macrosporic fungi, as well as eukaryotic organelles are also included because of their use in Next Generation Sequencing dataset analyses. Since our study focuses around protists and small eukaryotic fractions, the database will be curated for this purpose. The database will also have to be rewritten into the native languages mothur is written in, mainly C/C++, to be used for downstream analysis. Then, we will conduct analyses of sample sequence data using mothur following SOP. Mothur will screen the data for sequencing and PCR errors, process the improved sequences, and align them to the designed database. We will calculate alpha and beta diversities amongst other statistical analyses of the species’ diversity/density.

## Context
More to be added over the weekend.

## Goals and Non-Goals
Goals:
* Determine proper files for database input files
* Curate a well focussed database that can be used to efficiently target the “small eukaryotic fractions” that the study aims to identify
  * Short Term
* Create a pipeline to process data in mothur and output only relevant files for further downstream processing


## Milestones
* Download the database by end of class on 3/19
* Determine plans for processing of the database once downloaded
  * File type
  * Removal of extraneous data
* Download all SRA data files from Searle et al.
  * Using prefetch and fastqdump, retrieve all study data by end of class on 3/19 
* Begin processing
* Test PR2 Database format for compatibility with mothur using a subset of sample data by end of week 3/26  

## Proposed Solution
STEP 1: Format Files:
* **Convert all the SRR files of the sample into fasta format**

STEP 2: Mothur:
* **Run the files through the command line, which will conduct analyses including alpha and beta diversity**

STEP 3: Analyses
* **Do statistical analyses on the data using R**

STEP 4: Compile the analyses 

