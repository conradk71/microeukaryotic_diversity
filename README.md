# microeukaryotic_diversity
The ecological impacts of microeukaryotes in marine systems is well documented and understood. However, the microeukaryotic communities that are endogenous to freshwater systems are significantly understudied with respect to their marine counterparts. It is known that microeukaryotes play key roles in nutrient cycling, bioremediation, and higher eukaryotic nutrition. Gaining a better understanding of these organisms through analyses of species richness and diversity will allow researchers to begin to more accurately characterize specific roles in ecological processes. One common method for beginning such ecological studies is analysis of 18S rRNA data. Therefore, our project aims to build a pipeline that will automate the execution of the amplicon sequence data analysis tool mothur (Kozich et al. 2013).

## Author
* **Paul J. Risteca, Anusha Gangani, and Conrad Kurowski**

## Version
1.0

## Dependencies
* **Python 3**
* **Linux**
* **R 3.5.2 **
* **Mothur v1.41.3**
* **sratoolkit 2.9.0**



## Installing

You must clone the repository in command line to install. Copy the command below.
Pathing may vary for sratoolkit and R may vary by system. You may be asked to input or change the paths for these programs. 
If using test data, please move these files from test_data folder into the Mothurs_Helper folder.
```
https://github.com/tilld4wn/microeukaryotic_diversity.git
```

## Proper Input
* The input for this wrapper include two text files. One text file contains desired SRA accessions. The second contains sequencing primers used. These should be formatted with one entry per line. 
* You may also choose to use included test data.  
**EXAMPLE INPUT FROM TEST DATA FILE**
```
SRR2381067
SRR1342593


TTAATTTGACTCAACRCGGG
CGGGCGGTGTGTACAAAGG
```

## Running Main 
To run, follow all preceding instructions and enter the following command in your terminal:
```
python3 Mothurs_Helper.py 
```

The sample data should run in about 5 hours on 8 cores.

## Future Development/Improvements
* This wrapper is quite crude and could use some modifications to run more efficiently. 
* Additionally, I would like to improve user input functionality.

