#!/usr/bin/env python3

import argparse
import subprocess
import requests
import json
import sys
import os
import requests
import pandas as pd


def main():
    print ("test")
    parser = argparse.ArgumentParser(description='Process JSON file.')
    parser.add_argument('--json')
    parser.add_argument('--tsv')
    args = parser.parse_args()
    if len(sys.argv) == 0:
        parser.print_help()
    if args.json:
        with open(args.json, 'r') as f:
            d = json.load(f)
        # print (json.dumps(d))
        for key in d:
            print (key + "\t" + d[key])

    if args.tsv:
        pd.read_csv(args.tsv, header=0, sep='\t')

    query_1000_genomes()



def query_1000_genomes():
    print ("Querying 1000G")
    response = json.loads(requests.get("https://www.internationalgenome.org/api/beta/data-collection/_search").text)
    print (response)

if __name__ == '__main__':
    main()
