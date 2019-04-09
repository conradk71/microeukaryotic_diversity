# Design Document
### Microeukaryotic Diversity


## Overview
The composition and diversity of microeukaryotic communities in freshwater ecosystems is an area of study that is lagging behind many other domains of ecological exploration. The study that this project aims to complete is an in depth analysis of the microeukaryotic diversity of nearshore waters of Lake Michigan. All samples were collected at four beaches along the Northern Chicago shore line. All testing of this wrapper will focus around the use of 18S rRNA amplicon data collected from Searle et al. Amplicon data will be processed using wrapper for mothur and tools such as R or biopython.

## Context
Amplicon data a vital tool for ecologists. By using 18S rRNA amplicon data, we will be able to carry out taxonomic
classification and phylogenetic analysis of the microeukaryotic communities present in the Chicago near shore waters. While
amplicon data is useful, it is important to keep in mind that this data should be used to inform/guide hypothesis and study
aims rather than be a final answer. 
~~First, we will construct  an 18S rRNA gene database from the Protist Reference Ribosomal database (PR2) to be used in 
mothur. The PR2 Database provides access to unicellular eukaryotic, Small SubUnit rRNA, and rDNA sequences with curated 
taxonomy. The database is focused on nuclear-encoded sequences of protists. However, Metazoa, land plants and macrosporic 
fungi, as well as eukaryotic organelles are also included because of their use in Next Generation Sequencing dataset analyses. 
Since our study focuses around protists and small eukaryotic fractions, the database will be curated for this purpose. The 
database will also have to be rewritten into the native languages mothur is written in, mainly C/C++, to be used for 
downstream analysis.~~ 
We will begin our analysis of the data using the tool mothur, following the MiSeq SOP. Mothur will screen the data for
sequencing and PCR errors, process the improved sequences, and align them using the SILVA database. We are going to use the 
18S rRNA accession for *Sacchromyces cerevisiae* and the primer sequences used in the study (EUK1181 (5′-TTA ATT TGA CTC AAC RCG GG-3′ & EUK1624 (5′-CGG GCG GTG TGT ACA AAG G-3′)) to trim the silva database for our desired regions of interest.

We will calculate alpha and beta diversities amongst other statistical analyses of the species’ diversity/density.

Previously, research was conducted using eukaryotes analyzed from oil sands tailing ponds sediment and surface water. 


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

