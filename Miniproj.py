import os
#Creates a directory to store all the results
os.system("mkdir results")
os.system("mkdir results/SPAdes_output")
#Sets the output location for SPAdes with user input
os.system("vdb-config -i")
#Creates a log file to output to
outfile = open('results/miniproject.log', 'w')
#Uses SRAtoolkit to retrive the SRX5005282 Illumina reads from the resequencing of K-12 project
##Reads are single end
os.system("fastq-dump SRR8185310 --outdir ~/results")
##Puts the fastq files for the reads into spades and sets the outputs to results/SPAdes_output
os.system("~/SPAdes-3.15.4-Linux/bin/spades.py -s ~/results/SRR8185310.fastq -o ~/results/SPAdes_output")
##Reads in the SPAdes output contifs.fasta and splits it by > which seperates each contig into a different string
with open('results/SPAdes_output/contigs.fasta', "r+") as f:
    dnaS = f.read().split(">")
i = 1
count=0
length=0
#creates a new file to write the results of which contigs > 1000
newcontig = open("results/1000contigs.fasta", 'w')
## i loop that starts at 1 since dnaS[0] is empty
while i < len(dnaS):
    #Sets a temp variable to dnaS[i] but split by _ so it can retrive how length of the nucleotides
    temp = dnaS[i].split("_")
    #If the length of the nucleotides is >1000 it increases count adds the length to a sum of the length and outputs the contig to a file that contains only contigs >1000
    if int(temp[3]) > 1000:
        count+=1
        length+=int(temp[3])
        newcontig.write(">"+dnaS[i])
    i+=1
#Writes the results to the log file
outfile.write("There are "+str(count)+" contigs > 1000 in the assembly. \n")
outfile.write("There are "+str(length)+" bp in the assembly. \n")
#Outputs the predicited proteins for the genes in contigs
os.system("~/gms2_linux_64/gms2.pl --seq ~/results/1000contigs.fasta --genome-type auto --faa ~/results/protpredict")
##Creates a Blast database with the provided Ecoli.fasta
os.system("makeblastdb -in Ecoli.fasta -dbtype prot")
##Blasts the predicited protiens from gms2 against the created database and outputs to predicited_functionality
os.system("blastp -query ~/results/protpredict -db Ecoli.fasta -culling_limit 1 -out ~/results/predicted_functionality.csv -outfmt '10 qseqid sseqid pident qcovs'")
##Opens us the protpredict results and checks how many CDS were found and compares it to the CSD in the E.Coli and provides the difference
with open('results/protpredict', "r+") as r:
    prot = r.read().split(">")
final=prot[-1]
final=final.split(" ")
csd=int(final[0])-4140
##Writes the difference to the results log
outfile.write("GeneMarkS found "+str(csd)+" additional CDS than the RefSeq.")
