# mini-project
## Introduction
This is a python wrapper to be used in Ubuntu intended to Assemble single unpaired reads from fastq files, remove the short contigs, predict their protien sequence and blast them against a database to find matches.
It does this by grabbing the reads from NCBI useing SRAtoolkit and assembling the genomes using SPAdes. The output contig file is than parsed with python and contigs with bp counts of <1000 are removed. These filtered contig are than used in GeneMarkS-2 to predict their coding region are are blasted using pblast using an provided .fasta file database in order to find the best matches between the two and write the results to a CSV and well as check the differencs in the CDS numbers from the GeneMarkS-2 and the database.
# Dependences
All files must be accessable from the home file
## SRAtoolkit untill
Download the SRAtoolkit from https://github.com/ncbi/sra-tools/wiki/02.-Installing-SRA-Toolkit and install using the Ubuntu installation instructions up to step 4.
## SPAdes
https://github.com/ablab/spades
To download and install spades run these commands from your home directory
```
    wget http://cab.spbu.ru/files/release3.15.4/SPAdes-3.15.4-Linux.tar.gz
    tar -xzf SPAdes-3.15.4-Linux.tar.gz
```
## GeneMarkS2
Download GeneMarkS2 and a key from http://exon.gatech.edu/GeneMark/license_download.cgi..
Unpack the tar file in your home directory and gunzip the key and copy it to your home directory using.
```
 tar -xf gms2_linux_64.tar.gz
 gunzip gm_key_64.gz
 cp gm_key_64 ~/.gmhmmp2_key
```
If you downloaded the 32 bit version jst replace the 64 with 32.

# Install and Running through the test data
Download both the Miniproj.py and Ecoli.fasta and place them in your home folder.
While in the home file you can start the python wrapper by inputting.
```
python3 Miniproj.py
```
This will start the wrapper and bring up the SPAdes config. Navigate over to cache by pressing C, hit o to chose the location of user repositry and set it to your home file /results/SPAdes_output using enter to confirm and tab and arrows to navigate between options.

This will be the only user input nessecary, the program will run through the retrived test data.
# Results
The output log will be found in your home directoy /results as miniproject.log.

This log will contain how many contigs were greater than 1000bp, the total bp's of all contigs with greater than 1000bp and the number of CSD found from GeneMarkS compared to  the RefSeq.

The /results will also contain the protien predicitons from GeneMarkS, a fasta file containg the contigs over 1000bp, the fastq file retrived using the SRAtoolkit and the comparison of the protien predicitons and refseq in a csv called predicted_functionality formatted as Query sequence ID, Subject sequence ID, % Identity, % Query Coverage.
