#!/usr/bin/env python3

def main():
    '''
    Insert argparse code that populates the following variables
     - reads directory
     
    '''
    # Argparse code

import argparse
import os 

parser=argparse.ArgumentParser()

parser.add_argument("-input","--file_directory",help="this is the input file directory")

args=parser.parse_args()

local = args.file_directory

#os.system("cd "+local+str(sample_file[0])+"/")
#os.chdir(local+str(sample_file[0])+"/")

#ss=['CGT2321', 'CGT2477', 'CGT2483', 'CGT2491', 'CGT2761', 'CGT2164', 'CGT2704', 'CGT2049', 'CGT2211', 'CGT2060', 'CGT2448', 'CGT2779', 'CGT2867', 'CGT2730', 'CGT2224', 'CGT2998', 'CGT2564', 'CGT2726', 'CGT2235', 'CGT2490', 'CGT2348', 'CGT2798', 'CGT2550', 'CGT2347', 'CGT2149', 'CGT2486', 'CGT2278']
ss=['CGT2103', 'CGT2378', 'CGT2582', 'CGT2681', 'CGT2795', 'CGT2054', 'CGT2587', 'CGT2330', 'CGT2849', 'CGT2202', 'CGT2406', 'CGT2901', 'CGT2907', 'CGT2682', 'CGT2877', 'CGT2371', 'CGT2123', 'CGT2648', 'CGT2375', 'CGT2282', 'CGT2260', 'CGT2984', 'CGT2902']

for i in ss:
	os.system("cd "+local+str(i))
	#print(os.listdir(local+i))
	all_input=os.listdir(local+i)
	print(all_input)
	for j in all_input:
		if j =='contigs.fasta':
			os.system("cp "+local+i+"/"+str(j)+" contigs_file/"+str(i)+".fasta")
			print(os.getcwd())
	os.system("cd ..")

if __name__ == "__main__":
    main()