#!/usr/bin/env python3

import argparse
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("-f", help = "Please input your file")
    args = parser.parse_args()

    input_file = args.f

    f = pd.read_csv(input_file, sep=',', low_memory=False)

    df = pd.DataFrame(f)
    df.set_index('name_on_tree', inplace=True)

    print(df['SNP_counts'].max())
    print(df['SNP_counts'].min())
    print(df['SNP_counts'].mean())
    print(df['SNP_counts'].median())

    fig = plt.figure(figsize=(30,10))

    ax = fig.add_subplot(111)

    width = 0.3

    df.SNP_counts.plot(kind='bar', color='pink', ax=ax, width=width, position=1)

    ax.set_ylabel('SNP Count', fontsize=16)
    ax.set_xlabel('Sequence', fontsize=16)
    #plt.title('Histogram of ', fontsize=12)
    #trans_patch = mpatches.Patch(color='pink', label='Transmembrane Protein')
    #plt.legend(handles=[trans_patch], frameon=False, fontsize=16)
    plt.xticks(fontsize=16)
    plt.yticks(fontsize=16)
    plt.tight_layout()
    plt.savefig('25kSNP_SNPCount_Results.png')
if __name__ == "__main__":
    main()
