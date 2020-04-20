# Comparative Genomics
# Objective
*  We are going to do comparative genomic analysis, including Average Nucleotide Identity, SNP-based phylogenomics, and MLST.

# Installations and Setup
## ANI
### Installing FastANI
### git clone https://github.com/ParBLiSS/FastANI (Please install git first if you do not have it. For linux (sudo apt install git) and MacOS (brew install github, also install xcode-tools before you run brew))
#### This software requires c++11 to build, which is available in GCC >= 4.8 (on linux) and Clang >= 3.3 (on mac). It has the following denpendencies:
-------------
   - Autoconf ( http://www.gnu.org/software/autoconf/ )
   - either...
       GNU Scientific Library ( http://www.gnu.org/software/gsl/ )
     or..
       Boost Library ( http://www.boost.org ) (see "-with-boost" below)
   - Zlib ( included with OS X and most Linuxes, http://www.zlib.net ) *
   - C++ compiler with C++11 and openmp support
       Note for macOS users: Use "libomp" to link openmp with Clang
       libomp is available through brew ( https://formulae.brew.sh/formula/libomp )
Configure Steps:
------
   ./bootstrap.sh
   ./configure [--prefix=...] [--with-gsl=...] [--with-boost=...]
   make


Products:
---------
   - Executable fastANI
   
### tutorial
Produce help page. Quickly check the software usage and available command line options.
$ ./fastANI -h
One to One. Compute ANI between single query and single reference genome:
	
	./fastANI -q [QUERY_GENOME] -r [REFERENCE_GENOME] -o [OUTPUT_FILE] 
	
Here QUERY_GENOME and REFERENCE_GENOME are the query genome assemblies in fasta or multi-fasta format.

One to Many. Compute ANI between single query genome and multiple reference genomes:
	
	./fastANI -q [QUERY_GENOME] --rl [REFERENCE_LIST] -o [OUTPUT_FILE]
	
For above use case, REFERENCE_LIST should be a file containing directory paths to reference genomes, one per line.

Many to Many. When there are multiple query genomes and multiple reference genomes:


	$ ./fastANI --ql [QUERY_LIST] --rl [REFERENCE_LIST] -o [OUTPUT_FILE]


### FastANI wrapper

For our website, we will produce a python wrapper which used subprocess call to call FastANI, check input file, parameters passed to FastANI via the wrapper and also whether FastANI executable exist in the our conda working environment. You can just install it  through conda if you do not want to compile it from source.

	conda install -c bioconda fastANI

For the fastANI_wrapper.py you can just run it by typing
	
	python fastANI_wrapper.py <input directory pat> <output directory path> <databast path>
	

This script will: first, calculate pairwise anverage nucleitide identity among the samples you offered. Second, compare all the offered genomes to a reference genome and returen the highest ANI value in the reference genome and the taxonomy information of reference genome with highst ANI value. the input directory contains all the contig files you are going to calculate. Those files must be in a fasta format. the ourput directory will be used to store all the results. By default the database path is Campylobacter genome database with ~2000 complete genomes that were downloaded and then mannualy curated.

For the output directory, file with .txt will be used for visualization by running the following code
	
	python fastANI_output_to_distance_matrix.py <three_column_pairwise_ANI_file_from_the_wrapper> >> distance matrix_file_name.txt

For visualize_ANI.py
	
	python FastANI_heatmap.py <distance_matrix_file_name.txt path> <output directory>

This script will generate a heatmap of pairwise ANI vaules.



## MLST
### Installing MLST
	conda install -c bioconda mlst
### Running MLST

	mlst --csv --legacy --scheme --campylobacter <input_fasta_file> > <mlst_output_csv>

* We use the campylobacter scheme from PubMLST database for running the tool
* Input file format: Contig fasta files
* For our website we have a python wrapper script that checks the input files, output directory and calls MLST on the campylobacter scheme.
 
### Visualising MLST results for the website

#### We have a python scripts that creates a simple visualisation of the mlst results, depicting the STs detected and the sample names belonging to each ST
	python3 mlst_viz.py <mlst_output_csv> <output_directory>
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
