#!/usr/bin/env python3

import argparse
import subprocess
import requests
import json
import sys
import os
import requests
import pandas as pd
import ftplib
import ftputil
import fnmatch


def main():
    print ("DATASET SIZES...")
    parser = argparse.ArgumentParser(description='Process JSON file.')
    parser.add_argument('--json')
    parser.add_argument('--tsv')
    args = parser.parse_args()
    if len(sys.argv) <= 1:
        parser.print_help()
    if args.json:
        with open(args.json, 'r') as f:
            d = json.load(f)
        # print (json.dumps(d))
        for key in d:
            print (key + "\t" + d[key])
    if args.tsv:
        df = pd.read_csv(args.tsv, header=0, sep='\t')
        print (df)

        # now calculate 1000Genomes
        #ftp_size_1000_genomes()
        new_df = df.query('Code == "1000G"', inplace=False)
        print(type(new_df['Participants'].iloc[0]) == str)
        print (type(new_df['Participants'].iloc[0]))
        print (new_df['Participants'].iloc[0])
        print(type(new_df['Size'].iloc[0]) == str)
        print(float(new_df['Participants'].iloc[0]) <= 0)
        print(float(new_df['Size'].iloc[0]) <= 0)
        if type(new_df['Participants'].iloc[0]) == str or type(new_df['Size'].iloc[0]) == str or float(new_df['Participants'].iloc[0]) <= 0 or float(new_df['Size'].iloc[0]) <= 0:
            set_dataframe(df, '1000G', count_1000_genomes(), quick_size_1000_genomes())

        # GDC
        new_df = df.query('Code == "GDC"', inplace=False)
        if type(new_df['Participants'].iloc[0]) == str or type(new_df['Size'].iloc[0]) == str or float(new_df['Participants'].iloc[0]) <= 0 or float(new_df['Size'].iloc[0]) <= 0:
            set_dataframe(df, 'GDC', count_gdc_genomes(), size_gdc_genomes())

        # print summary
        print(df)
        # write output file
        df.to_csv(args.tsv, sep='\t', index=False)

def count_gdc_genomes():
    return(0)

def size_gdc_genomes():
    return(0)

def set_dataframe(df, code, participants, size):
    print("Setting dataframe: "+code)
    df['Participants'] = (df.apply(lambda x: participants if x['Code']==code else x['Participants'], axis=1))
    df['Size'] = (df.apply(lambda x: size if x['Code']==code else x['Size'], axis=1))

def quick_size_1000_genomes():
    # left off here, pull the current.tree doc and parse
    #host = ftputil.FTPHost('ftp.1000genomes.ebi.ac.uk','anonymous','')
    #host.download("/vol1/ftp/current.tree", "current.tree")
    #host.close()
    filename = 'current.tree'
    df = pd.read_csv(filename, header=None, sep='\t')
    total = df.iloc[:, 2:3].sum()
    s = df.iloc[:, 2:3]
    #print (s)
    #print ("Total bytes: "+str(total.values[0]))
    return(total.values[0])


def ftp_size_1000_genomes():
    print("Calculating file sized for 1000G")
    host = ftputil.FTPHost('ftp.1000genomes.ebi.ac.uk','anonymous','') # ftp host info
    recursive = host.walk("/vol1/ftp/data_collections",topdown=True,onerror=None) # recursive search
    for root,dirs,files in recursive:
        for name in files:
            fullpath = host.path.join(root, name)
            size = host.path.getsize(fullpath)
            writepath = fullpath + " " +str(size) + "\n"
            #print(writepath)

def count_1000_genomes():
    print ("Querying 1000G")
    total_sample_count = 0
    response = json.loads(requests.get("https://www.internationalgenome.org/api/beta/data-collection/_search").text)
    #print (response)
    for hit in response['hits']['hits']:
        #print(hit['_source']['samples']['count'])
        total_sample_count += hit['_source']['samples']['count']
    #print ("total samples: "+str(total_sample_count))
    return(int(total_sample_count))

if __name__ == '__main__':
    main()
