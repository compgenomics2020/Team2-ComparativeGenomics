# Comparative Genomics
# Objective
*  We are going to do comparative genomic analysis, including Average Nucleotide Identity, SNP-based phylogenomics, and MLST.

# Installations and Setup
## ANI

## MLST

## SNP Typing
### Installing Ksnp3.1
	wget https://sourceforge.net/projects/ksnp/files/kSNP3.1_Linux_package.zip
	unzip kSNP3.1_Linux_package.zip
* Input file format: <path/to/isolate_n.fasta> \t <isolate_ID>
	kSNP3 –in <input_file> -k 25 outdir <output_directory> -ML
#### Next, the source code needs to be modified to allow local access without sudo permissions

### Determining optimal value of k
#### First, the ksnp program kSNP3.1_Linux_package/kSNP/jellyfish must be exported to $PATH and copied to usr/bin
#### Next, a copy of the text file with all the paths to fasta files must be created
#### Run MakeFasta with text file as input and name of output file to concatenate all inputs to a single fasta
	MakeFasta <input_file.txt> <output_file.fasta>
#### Run Kchooser on generated fasta file
	Kchooser <all_genomes.fasta>
#### If optimal K is 31, the`n K likely plateaued at a specific percentage. Check Kchooser.report and rerun with asymptotic percentage as cutoff (ex. 95.8%)
	Kchooser <all_genomes.fasta> 0.958
### Creating phylogenetic tree
	kSNP3 -in <input_file> -k 25 -outdir <output_directory> -ML 
