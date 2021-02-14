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


# References:
# excellent tool to convert cURLs from Chrome to Python Code: https://curl.trillworks.com/#

def main():
    print ("DISCOVERING DATASET SIZES...")
    print ("============================")
    parser = argparse.ArgumentParser(description='Process JSON file.')
    parser.add_argument('--tsv', help='A TSV file 6 columns, the first is "Code", the last two are "Participants" and "Size" respectively. The file will be overwritten with updated participants and size counts for each source missing one or both.')
    args = parser.parse_args()

    if len(sys.argv) <= 1:
        parser.print_help()

    if args.tsv:
        df = pd.read_csv(args.tsv, header=0, sep='\t')

        # 1000Genomes
        print ("CALCULATING 1000 GENOMES...")
        new_df = df.query('Code == "1000G"', inplace=False)
        if type(new_df['Participants'].iloc[0]) == str or type(new_df['Size'].iloc[0]) == str or float(new_df['Participants'].iloc[0]) <= 0 or float(new_df['Size'].iloc[0]) <= 0:
            set_dataframe(df, '1000G', count_1000_genomes(), quick_size_1000_genomes())
        else:
            print ("...VALUES EXIST FOR SIZE AND CASES, SKIPPING")

        # GDC
        print ("CALCULATING GDC...")
        new_df = df.query('Code == "GDC"', inplace=False)
        if type(new_df['Participants'].iloc[0]) == str or type(new_df['Size'].iloc[0]) == str or float(new_df['Participants'].iloc[0]) <= 0 or float(new_df['Size'].iloc[0]) <= 0:
            set_dataframe(df, 'GDC', count_gdc(), size_gdc())
        else:
            print ("...VALUES EXIST FOR SIZE AND CASES, SKIPPING")

        # print summary
        print("SUMMARY...")
        print(df)
        # write output file
        df.to_csv(args.tsv, sep='\t', index=False)

def count_gdc():

    cookies = {
        's_fid': '4F07B824B355E38A-1F0C5E4445D357AA',
        's_vi': '[CS]v1|2FD017E70515F859-40000AA0AFFF7E32[CE]',
        '_CEFT': 'Q%3D%3D%3D',
        '_ga': 'GA1.2.1008060774.1610047601',
        '_hjid': '6f4e6b64-a70c-46d9-8b37-58b4914fd847',
        '_ce.s': 'v11.rlc~1610155667701',
        's_cc': 'true',
        '_gid': 'GA1.3.491641052.1613262819',
        'NCI-Warning': 'true',
        '_gat_GSA_ENOR0': '1',
        'gpv_pn': 'portal.gdc.cancer.gov%2F',
        's_sq': '%5B%5BB%5D%5D',
        's_ppv': '100%7C0',
    }

    headers = {
        'Connection': 'keep-alive',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        'Content-Type': 'application/json',
        'Accept': '*/*',
        'Origin': 'https://portal.gdc.cancer.gov',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://portal.gdc.cancer.gov/',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    params = (
        ('hash', 'e0e73077c16f871b9d26487a1770a070'),
    )

    data = '{"query":"query PortalSummary_relayQuery {\\n viewer {\\n projects {\\n aggregations {\\n primary_site {\\n buckets {\\n key\\n }\\n }\\n }\\n hits(first: 0) {\\n total\\n }\\n }\\n repository {\\n cases {\\n hits(first: 0) {\\n total\\n }\\n }\\n files {\\n hits(first: 0) {\\n total\\n }\\n }\\n }\\n explore {\\n genes {\\n hits(first: 0) {\\n total\\n }\\n }\\n ssms {\\n hits(first: 0) {\\n total\\n }\\n }\\n }\\n }\\n}\\n","variables":{}}'

    response = requests.post('https://portal.gdc.cancer.gov/auth/api/v0/graphql/PortalSummary', headers=headers, params=params, cookies=cookies, data=data)
    # print(response.text)
    struct = json.loads(response.text)
    case_size = struct['data']['viewer']['repository']['cases']['hits']['total']
    return(case_size)

def size_gdc():
    cookies = {
        's_fid': '4F07B824B355E38A-1F0C5E4445D357AA',
        's_vi': '[CS]v1|2FD017E70515F859-40000AA0AFFF7E32[CE]',
        '_CEFT': 'Q%3D%3D%3D',
        '_ga': 'GA1.2.1008060774.1610047601',
        '_hjid': '6f4e6b64-a70c-46d9-8b37-58b4914fd847',
        '_ce.s': 'v11.rlc~1610155667701',
        's_cc': 'true',
        '_gid': 'GA1.3.491641052.1613262819',
        'NCI-Warning': 'true',
        'gpv_pn': 'portal.gdc.cancer.gov%2Frepository',
        's_sq': '%5B%5BB%5D%5D',
        '_gat_GSA_ENOR0': '1',
        's_ppv': '100%7C0',
    }

    headers = {
        'Connection': 'keep-alive',
        'Accept': '*/*',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 11_1_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.146 Safari/537.36',
        'Content-Type': 'application/json',
        'Origin': 'https://portal.gdc.cancer.gov',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Dest': 'empty',
        'Referer': 'https://portal.gdc.cancer.gov/repository',
        'Accept-Language': 'en-US,en;q=0.9',
    }

    params = (
        ('hash', 'fdee50a77629dcae5e288f87c9596155'),
    )

    data = '{"id":"q1","query":"query Queries($first_0:Int\u0021,$offset_1:Int\u0021) {viewer {...F2}} fragment F0 on CaseAggregations {demographic__ethnicity {buckets {doc_count,key}},demographic__gender {buckets {doc_count,key}},demographic__race {buckets {doc_count,key}},demographic__vital_status {buckets {doc_count,key}},disease_type {buckets {doc_count,key}},primary_site {buckets {doc_count,key}},project__project_id {buckets {doc_count,key}},project__program__name {buckets {doc_count,key}}} fragment F1 on FileAggregations {cases__project__project_id {buckets {doc_count,key}},cases__primary_site {buckets {doc_count,key}},data_category {buckets {doc_count,key}},data_type {buckets {doc_count,key}},experimental_strategy {buckets {doc_count,key}},data_format {buckets {doc_count,key}},access {buckets {doc_count,key}}} fragment F2 on Root {cart_summary {_aggregations1TAxVJ:aggregations {fs {value}}},repository {cases {_aggregations2LbddX:aggregations(aggregations_filter_themselves:true) {...F0},_hits1ATaID:hits(score:\\"annotations.annotation_id\\",first:$first_0,offset:$offset_1) {total}},files {_aggregations2LbddX:aggregations(aggregations_filter_themselves:true) {...F1},_hits2bK9cM:hits(first:$first_0,offset:$offset_1) {total}}}}","variables":{"first_0":20,"offset_1":0}}'

    response = requests.post('https://portal.gdc.cancer.gov/auth/api/v0/graphql?hash=fdee50a77629dcae5e288f87c9596155', headers=headers, cookies=cookies, data=data)
    # print(response.text)
    struct = json.loads(response.text)
    file_size_struct = struct['data']['viewer']['cart_summary']
    file_size_keys = list(file_size_struct.keys())
    file_size = file_size_struct[file_size_keys[0]]['fs']['value']
    return(file_size)

def set_dataframe(df, code, participants, size):
    print("SETTING DATAFRAME VALUES FOR: "+code)
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
