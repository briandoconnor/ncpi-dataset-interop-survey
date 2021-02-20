# Data Sources

## Template

* URL:
* Open/Controlled:
* API:
* DRS Server: see the [DRS 1.1 Transition within NCPI](https://docs.google.com/document/d/1Wf4enSGOEXD5_AE-uzLoYqjIp5MnePbZ6kYTVFp1WoM/edit#heading=h.qiwlmit3m9) guide
* Identifiers:

### Description

### Available Datasets

### Tech Details


## PDC

* URL:
* Open/Controlled:
* API:

### Description:

### Tech Details

See [email](https://mail.google.com/mail/u/3/?zx=rkmgl6cqlnby#label/0+Triage/FMfcgxwLsJtCSRXDZwbvvJGJzfJJXNWL) with details


## GDC

* URL: https://gdc.cancer.gov/
* Open/Controlled: Both
* API: https://portal.gdc.cancer.gov/auth/api/v0/graphql?hash=7a8ca53aa9b15e4f28abb180a692893e
* DRS Server: see the [DRS 1.1 Transition within NCPI](https://docs.google.com/document/d/1Wf4enSGOEXD5_AE-uzLoYqjIp5MnePbZ6kYTVFp1WoM/edit#heading=h.qiwlmit3m9) guide
* Identifiers: DataGUIDs that can be resolved via https://dataguids.org, no prefix registered in https://identifiers.org

### Description:

"The NCI's Genomic Data Commons (GDC) provides the cancer research community with a unified data repository that enables data sharing across cancer genomic studies in support of precision medicine.

The GDC supports several cancer genome programs at the NCI Center for Cancer Genomics (CCG), including The Cancer Genome Atlas (TCGA) and Therapeutically Applicable Research to Generate Effective Treatments (TARGET)."

### Tech Details

The GDC has a well-defined [API](https://gdc.cancer.gov/developers/gdc-application-programming-interface-api)
and lots of [documentation](https://docs.gdc.cancer.gov/API/Users_Guide/Getting_Started/) on how to use it.

The entity types you can query on:
* projects
* cases
* files
* annotations
* data (data download)
* manifest
* slicing (for BAMs)

There's also a [GraphQL endpoint](https://docs.gdc.cancer.gov/API/Users_Guide/GraphQL_Examples/) that can be queried.

I ended up not using their documented API endpoints because the two stats I
needed (dataset size and participants) was more easily accessible via the API
that powers the GDC portal.

#### Notable Programs

* TCGA
* TARGET
* GENIE
* CMI
* BEATAML1.0
* CGCI
* CPTAC
* CTSP
* FM
* HCMI
* MMRF
* NCICCR
* OHSU
* ORGANOID
* VAREPOP
* WCDT

#### Identifiers & DRS

So everything in GDC gets a UUID that can be resolved via 1) DataGUIDS.org or
2) their DRS 1.1 server.

Examples:

##### Open Access

An open access RNASeq file: https://portal.gdc.cancer.gov/files/84d49bb4-5df5-4af3-8a24-e08fd6d67aff

84d49bb4-5df5-4af3-8a24-e08fd6d67aff

https://dataguids.org/ga4gh/dos/v1/dataobjects/84d49bb4-5df5-4af3-8a24-e08fd6d67aff

And this resolves to something pre-DRS 1.1. Notice a signed URL:

```
{
  "data_object": {
    "checksums": [
      {
        "checksum": "d66fe371fd42fcd10396f3d6440732c3",
        "type": "md5"
      }
    ],
    "created": "2019-07-18T00:32:33.936721",
    "description": "",
    "id": "84d49bb4-5df5-4af3-8a24-e08fd6d67aff",
    "mime_type": "",
    "name": null,
    "size": 304288,
    "updated": "2019-07-18T00:32:33.936727",
    "urls": [
      {
        "url": "gs://gdc-organoid-pancreatic-phs001611-open/84d49bb4-5df5-4af3-8a24-e08fd6d67aff/40c3d223-a76c-4433-a18a-ca45d03072fa.FPKM.txt.gz"
      },
      {
        "url": "https://api.gdc.cancer.gov/data/84d49bb4-5df5-4af3-8a24-e08fd6d67aff"
      },
      {
        "url": "s3://gdc-organoid-pancreatic-phs001611-2-open/84d49bb4-5df5-4af3-8a24-e08fd6d67aff/40c3d223-a76c-4433-a18a-ca45d03072fa.FPKM.txt.gz"
      }
    ],
    "version": "4a9d86ba"
  }
}
```

You can get a DRS 1.1 response with:

https://dataguids.org/ga4gh/drs/v1/objects/84d49bb4-5df5-4af3-8a24-e08fd6d67aff

```
{
   "access_methods":[
      {
         "access_id":"gs",
         "access_url":{
            "url":"gs://gdc-organoid-pancreatic-phs001611-open/84d49bb4-5df5-4af3-8a24-e08fd6d67aff/40c3d223-a76c-4433-a18a-ca45d03072fa.FPKM.txt.gz"
         },
         "region":"",
         "type":"gs"
      },
      {
         "access_id":"https",
         "access_url":{
            "url":"https://api.gdc.cancer.gov/data/84d49bb4-5df5-4af3-8a24-e08fd6d67aff"
         },
         "region":"",
         "type":"https"
      },
      {
         "access_id":"s3",
         "access_url":{
            "url":"s3://gdc-organoid-pancreatic-phs001611-2-open/84d49bb4-5df5-4af3-8a24-e08fd6d67aff/40c3d223-a76c-4433-a18a-ca45d03072fa.FPKM.txt.gz"
         },
         "region":"",
         "type":"s3"
      }
   ],
   "aliases":[

   ],
   "checksums":[
      {
         "checksum":"d66fe371fd42fcd10396f3d6440732c3",
         "type":"md5"
      }
   ],
   "contents":[

   ],
   "created_time":"2019-07-18T00:32:33.936721",
   "description":null,
   "did":"ga4gh/drs/v1/objects/84d49bb4-5df5-4af3-8a24-e08fd6d67aff",
   "form":"object",
   "from_index_service":{
      "host":"https://nci-crdc.datacommons.io/index/",
      "name":"NCI CRDC"
   },
   "id":"84d49bb4-5df5-4af3-8a24-e08fd6d67aff",
   "mime_type":"application/json",
   "name":null,
   "self_uri":"drs://nci-crdc.datacommons.io/84d49bb4-5df5-4af3-8a24-e08fd6d67aff",
   "size":304288,
   "updated_time":"2019-07-18T00:32:33.936727",
   "version":"4a9d86ba"
}
```

Now, resolving with DRS using settings from the DRS 1.1 info doc above:

https://nci-crdc.datacommons.io/ga4gh/drs/v1/objects/84d49bb4-5df5-4af3-8a24-e08fd6d67aff


```
{
   "access_methods":[
      {
         "access_id":"gs",
         "access_url":{
            "url":"gs://gdc-organoid-pancreatic-phs001611-open/84d49bb4-5df5-4af3-8a24-e08fd6d67aff/40c3d223-a76c-4433-a18a-ca45d03072fa.FPKM.txt.gz"
         },
         "region":"",
         "type":"gs"
      },
      {
         "access_id":"https",
         "access_url":{
            "url":"https://api.gdc.cancer.gov/data/84d49bb4-5df5-4af3-8a24-e08fd6d67aff"
         },
         "region":"",
         "type":"https"
      },
      {
         "access_id":"s3",
         "access_url":{
            "url":"s3://gdc-organoid-pancreatic-phs001611-2-open/84d49bb4-5df5-4af3-8a24-e08fd6d67aff/40c3d223-a76c-4433-a18a-ca45d03072fa.FPKM.txt.gz"
         },
         "region":"",
         "type":"s3"
      }
   ],
   "aliases":[

   ],
   "checksums":[
      {
         "checksum":"d66fe371fd42fcd10396f3d6440732c3",
         "type":"md5"
      }
   ],
   "contents":[

   ],
   "created_time":"2019-07-18T00:32:33.936721",
   "description":null,
   "form":"object",
   "id":"84d49bb4-5df5-4af3-8a24-e08fd6d67aff",
   "mime_type":"application/json",
   "name":null,
   "self_uri":"drs://nci-crdc.datacommons.io/84d49bb4-5df5-4af3-8a24-e08fd6d67aff",
   "size":304288,
   "updated_time":"2019-07-18T00:32:33.936727",
   "version":"4a9d86ba"
}
```

##### Controlled Access

Looking at a controlled access example that I have access to (Target):

https://portal.gdc.cancer.gov/files/f810592a-c69d-4d6b-ad44-ca1377892231

https://nci-crdc.datacommons.io/ga4gh/drs/v1/objects/f810592a-c69d-4d6b-ad44-ca1377892231

```
{
   "access_methods":[
      {
         "access_id":"gs",
         "access_url":{
            "url":"gs://gdc-target-phs000218-controlled/f810592a-c69d-4d6b-ad44-ca1377892231/78c0661e-be41-43a8-aa3d-592b6297d601.gdc_liftover.vcf.gz"
         },
         "region":"",
         "type":"gs"
      },
      {
         "access_id":"https",
         "access_url":{
            "url":"https://api.gdc.cancer.gov/data/f810592a-c69d-4d6b-ad44-ca1377892231"
         },
         "region":"",
         "type":"https"
      },
      {
         "access_id":"s3",
         "access_url":{
            "url":"s3://target-controlled/f810592a-c69d-4d6b-ad44-ca1377892231/78c0661e-be41-43a8-aa3d-592b6297d601.gdc_liftover.vcf.gz"
         },
         "region":"",
         "type":"s3"
      }
   ],
   "aliases":[

   ],
   "checksums":[
      {
         "checksum":"0f125c67c6a10c75f207735a2dcc5d98",
         "type":"md5"
      }
   ],
   "contents":[

   ],
   "created_time":"2019-01-17T03:05:09.783363",
   "description":null,
   "form":"object",
   "id":"f810592a-c69d-4d6b-ad44-ca1377892231",
   "mime_type":"application/json",
   "name":null,
   "self_uri":"drs://nci-crdc.datacommons.io/f810592a-c69d-4d6b-ad44-ca1377892231",
   "size":413212211,
   "updated_time":"2019-01-17T03:05:09.783371",
   "version":"48c0a855"
}
```

To access the URL you need the token downloadable from the GDC website once you
login with your eRA Commons ID.  I have access to this file as part of TARGET
since I'm dbGaP approved for that project. So I downloaded my token as
`gdc-token-text-file.txt` and then used it like the following to download
the file.

```
  token=$(<gdc-token-text-file.txt)

  curl --remote-name --remote-header-name 'https://api.gdc.cancer.gov/data/f810592a-c69d-4d6b-ad44-ca1377892231' \
    --header "X-Auth-Token: $token"
```

And that allowed me to download this controlled file using DRS 1.1.  
Although the DRS response wasn't enough information

This does not work with "Authorization: Bearer" tokens:

```
curl --remote-name --remote-header-name 'https://api.gdc.cancer.gov/data/f810592a-c69d-4d6b-ad44-ca1377892231' --header "Authorization: Bearer $token"
```

The end result is a file that says "Your token is invalid or expired. Please get a new token from GDC Data Portal."


## 1000 Genomes

* URL: https://www.internationalgenome.org/data/
* Open/Controlled: Open
* API: https://www.internationalgenome.org/data-portal/data-collection
* DRS Server: NA
* Identifiers: SRA/ENA accessions but individual files via URLs not GUIDs, see [doc](https://www.internationalgenome.org/category/meta-data/)

### Description:

"The International Genome Sample Resource (IGSR) was established to ensure the ongoing usability of data generated by the 1000 Genomes Project and to extend the data set. More information is available about the IGSR."

"The 1000 Genomes Project ran between 2008 and 2015, creating the largest public catalogue of human variation and genotype data. As the project ended, the Data Coordination Centre at EMBL-EBI has received continued funding from the Wellcome Trust to maintain and expand the resource. The International Genome Sample Resource (IGSR) was set up to do this with the following aims:

Ensure the future access to and usability of the 1000 Genomes reference data
Incorporate additional published genomic data on the 1000 Genomes samples
Expand the data collection to include new populations not represented in the 1000 Genomes Project"

### Tech Details

No public API but here's the API that powers their website:

https://www.internationalgenome.org/api/beta/data-collection/_search

Ultimately, all roads lead back to an FTP site that houses their data.  There
isn't the concept of a GUID per file as far as I can tell.  So really it's the
path in the FTP site that gives semantic meaning to the file and it's ID.
So there isn't an easy way to take a GUID and resolve it to a given file.
