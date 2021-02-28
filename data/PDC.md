## PDC

* URL: https://proteomic.datacommons.cancer.gov/pdc/
* Open/Controlled: open (for now)
* API: https://pdc.cancer.gov/data-dictionary/dictionary.html and https://proteomic.datacommons.cancer.gov/data-dictionary/apidocumentation.html
* DRS Server: see the [DRS 1.1 Transition within NCPI](https://docs.google.com/document/d/1Wf4enSGOEXD5_AE-uzLoYqjIp5MnePbZ6kYTVFp1WoM/edit#heading=h.qiwlmit3m9) guide, PDC uses the CRDC DRS server

### Description

"The objectives of the National Cancer Institute’s Proteomic Data Commons (PDC) are (1) to make cancer-related proteomic datasets easily accessible to the public, and (2) facilitate multiomic integration in support of precision medicine through interoperability with other resources.

The PDC was developed to advance our understanding of how proteins help to shape the risk, diagnosis, development, progression, and treatment of cancer. In-depth analysis of proteomic data allows us to study both how and why cancer develops and to devise ways of personalizing treatment for patients using precision medicine."

### Available Datasets

* Clinical Proteomic Tumor Analysis Consortium (53 Studies)
* Georgetown Proteomics Research Program (1 Study)
* International Cancer Proteogenome Consortium (8 Studies)
* Pediatric Brain Tumor Atlas - CBTN (2 Studies)
* Quantitative digital maps of tissue biopsies (1 Study)

### Tech Details

You can get signed URLs from Amazon using:

```
curl --remote-name --remote-header-name 'https://nci-crdc.datacommons.io/ga4gh/drs/v1/objects/00040a6f-b7e5-4e5c-ab57-ee92a0ba8201' \
  --header "Authorization: Bearer $token"
  
{
   "name" : "",   "checksums" : [      {         "checksum" : "ac69203ae2b2c8b9bbec2dbfeecc8de4",
         "type" : "md5"
      }
   ],
   "mime_type" : "application/json",
   "created_time" : "2021-01-22T12:16:49.554299",
   "self_uri" : "drs://nci-crdc.datacommons.io/dg.4DFC/00040a6f-b7e5-4e5c-ab57-ee92a0ba8201",
   "version" : "d637c4f2",
   "aliases" : [],
   "contents" : [],
   "description" : null,
   "size" : 46456768,
   "form" : "object",
   "updated_time" : "2021-01-22T12:16:49.554305",
   "access_methods" : [
      {
         "region" : "",
         "access_id" : "s3",         "type" : "s3",         "access_url" : {            "url" : "s3://pdcdatastore/studies/262/mzml/20151104-P50-20ug-s35.mzML.gz"
         }      }   ],   "id" : "dg.4DFC/00040a6f-b7e5-4e5c-ab57-ee92a0ba8201"
}


curl --remote-name --remote-header-name 'https://nci-crdc.datacommons.io/ga4gh/drs/v1/objects/00040a6f-b7e5-4e5c-ab57-ee92a0ba8201/access/s3' \
  --header "Authorization: Bearer $token"
  
# this returns a JSON with a signed URL:
{"url":"https://pdcdatastore.s3.amazonaws.com/studies/262/mzml/20151104-P50-20ug-s35.mzML.gz..." }
  
```

See [email](https://mail.google.com/mail/u/3/?zx=rkmgl6cqlnby#label/0+Triage/FMfcgxwLsJtCSRXDZwbvvJGJzfJJXNWL) with details


