## GMKF

* URL:
* Open/Controlled:
* API:
* DRS Server: see the [DRS 1.1 Transition within NCPI](https://docs.google.com/document/d/1Wf4enSGOEXD5_AE-uzLoYqjIp5MnePbZ6kYTVFp1WoM/edit#heading=h.qiwlmit3m9) guide
* Identifiers:

### Description

### Available Datasets

### Tech Details

An open access file from Pediatric Brain Tumor Atlas: CBTTC.

```
% curl -s -o - https://data.kidsfirstdrc.org/ga4gh/drs/v1/objects/fdc1a34e-556f-4964-b24a-38ed29960498 | json_pp
{
   "form" : "object",
   "aliases" : [],
   "name" : "ad45e585-d356-4d8b-97cd-4e050418754c.mutect2_somatic.PASS.vep.vcf.gz",
   "contents" : [],
   "self_uri" : "drs://data.kidsfirstdrc.org/fdc1a34e-556f-4964-b24a-38ed29960498",
   "created_time" : "2019-07-23T18:02:01.643362",
   "updated_time" : "2019-07-23T18:02:01.643375",
   "size" : 2527333,
   "description" : null,
   "id" : "fdc1a34e-556f-4964-b24a-38ed29960498",
   "version" : "eab69119",
   "access_methods" : [
      {
         "type" : "s3",
         "access_url" : {
            "url" : "s3://kf-study-us-east-1-prd-sd-bhjxbdqk/harmonized/simple-variants/ad45e585-d356-4d8b-97cd-4e050418754c.mutect2_somatic.PASS.vep.vcf.gz"
         },
         "region" : "",
         "access_id" : "s3"
      }
   ],
   "mime_type" : "application/json",
   "checksums" : [
      {
         "type" : "etag",
         "checksum" : "e57afbbed369fb769b4d657a42d560a5"
      }
   ]
}
```

Getting a signed URL:


```
  token=$(<gmkf-token-text-file.txt)

  curl --remote-name --remote-header-name 'https://data.kidsfirstdrc.org/ga4gh/drs/v1/objects/fdc1a34e-556f-4964-b24a-38ed29960498/access/s3' \
    --header "X-Auth-Token: $token"
```

This doesn't work... I think I need to 1) request an access token using my bearer token and 2) then request the signed URL with the access token.

```
curl 'https://kf-key-manager.kf-strides.org/token?fence=gen3' \
  -H 'authority: kf-key-manager.kf-strides.org' \
  -H 'accept: application/json, text/plain, */*' \
  -H "authorization: Bearer $token" \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36' \
  -H 'origin: https://portal.kidsfirstdrc.org' \
  -H 'sec-fetch-site: cross-site' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://portal.kidsfirstdrc.org/' \
  -H 'accept-language: en-US,en;q=0.9' \
  --compressed

  curl 'https://data.kidsfirstdrc.org/user/data/download/fdc1a34e-556f-4964-b24a-38ed29960498' \
  -H 'Connection: keep-alive' \
  -H 'Authorization: Bearer $token2' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36' \
  -H 'Accept: */*' \
  -H 'Origin: https://portal.kidsfirstdrc.org' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://portal.kidsfirstdrc.org/' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  --compressed

----

  curl 'https://kf-key-manager.kf-strides.org/token?fence=gen3' \
  -H 'authority: kf-key-manager.kf-strides.org' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'authorization: Bearer ...' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36' \
  -H 'origin: https://portal.kidsfirstdrc.org' \
  -H 'sec-fetch-site: cross-site' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://portal.kidsfirstdrc.org/' \
  -H 'accept-language: en-US,en;q=0.9' \
  --compressed

  curl 'https://kf-key-manager.kf-strides.org/refresh?fence=gen3' \
  -X 'POST' \
  -H 'authority: kf-key-manager.kf-strides.org' \
  -H 'content-length: 0' \
  -H 'accept: application/json, text/plain, */*' \
  -H 'authorization: Bearer ...' \
  -H 'user-agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36' \
  -H 'origin: https://portal.kidsfirstdrc.org' \
  -H 'sec-fetch-site: cross-site' \
  -H 'sec-fetch-mode: cors' \
  -H 'sec-fetch-dest: empty' \
  -H 'referer: https://portal.kidsfirstdrc.org/' \
  -H 'accept-language: en-US,en;q=0.9' \
  --compressed

  # response
  {"access_token":"...","refresh_token":"..."}

  curl 'https://data.kidsfirstdrc.org/user/data/download/fdc1a34e-556f-4964-b24a-38ed29960498' \
  -H 'Connection: keep-alive' \
  -H 'Authorization: Bearer ...' \
  -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 11_2_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36' \
  -H 'Accept: */*' \
  -H 'Origin: https://portal.kidsfirstdrc.org' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Referer: https://portal.kidsfirstdrc.org/' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  --compressed
```

LEFT OFF WITH: it's not clear how I can get the gen3 refresh token --> access token --> DRS 1.1 request for a signed URL... seems like there's a portal token involved here that I don't understand.  And the refresh token coming back is not the gen3 token but a kids first one?
