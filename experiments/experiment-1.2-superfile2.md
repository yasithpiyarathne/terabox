# https://c-jp.terabox.com/rest/2.0/pcs/superfile2 #first

### Request

```shell
curl 'https://c-jp.terabox.com/rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=dubox&clienttype=0&web=1&logid=MTY4OTYwMzYzNTgxNjAuODU5Mzg2NDE0OTQ4MTc4OQ==&path=%2Fpexels-felix-mittermeier-957040.jpg&uploadid=P1-MTAuMjUyLjcxLjQ0OjE2ODk2MDM2NjQ6OTIwMjI3MTcwODk2NDE5NDg2NA==&uploadsign=0&partseq=0' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundarycDXuXHaP3Nihj77H' \
  -H 'Cookie: browserid=fTjwmhvyYzXgh0GuI4u7GxQrZ5Rw29SlLE69fh2SqigTr9vHrjRRuOVBzZI=; __bid_n=1894a18c489bb3f5b74207; _ga=GA1.1.490507614.1689165293; ndus=YyTtnC7teHuibUJkw3vAneWrxIgSxBWriTudMHPm; ab_sr=1.0.1_MWJmMTIyMjg0NzRhMDIzZjRlM2FiMzgyMTA1YTU0ZDIyNTRkOTEzZDkyYzdmOGUyYTAwMTg4NDllNGQyNTJmMzViZTU0YmNlZmU4Y2RlZjMwNmEyYjQzZTQ0OWY3ZWQwNDI3NjljNDFkYzNjNGQ2MGFmYzljOTg2YThmYjIzZDEyNjQ1MzM4ZTBjMmI3ZjM2YjgyNjJjMmZlNTE5MjNkMg==; _ga_06ZNKL8C2E=GS1.1.1689603635.5.1.1689603669.26.0.0' \
  -H 'Origin: https://www.terabox.com' \
  -H 'Referer: https://www.terabox.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82' \
  -H 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw $'------WebKitFormBoundarycDXuXHaP3Nihj77H\r\nContent-Disposition: form-data; name="file"; filename="blob"\r\nContent-Type: application/octet-stream\r\n<DATA>-----WebKitFormBoundarycDXuXHaP3Nihj77H--\r\n' \
  --compressed
```
### Request Params

```json
{
    "method": "upload",
    "app_id": "250528",
    "channel": "dubox",
    "clienttype": "0",
    "web": "1",
    "logid": "MTY4OTYwMzYzNTgxNjAuODU5Mzg2NDE0OTQ4MTc4OQ==",
    "path":  "/pexels-felix-mittermeier-957040.jpg",
    "uploadid":  "P1-MTAuMjUyLjcxLjQ0OjE2ODk2MDM2NjQ6OTIwMjI3MTcwODk2NDE5NDg2NA==",
    "uploadsign":   "0",
    "partseq":  "0"
}
```

### Request Headers

```http
POST /rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=dubox&clienttype=0&web=1&logid=MTY4OTYwMzYzNTgxNjAuODU5Mzg2NDE0OTQ4MTc4OQ==&path=%2Fpexels-felix-mittermeier-957040.jpg&uploadid=P1-MTAuMjUyLjcxLjQ0OjE2ODk2MDM2NjQ6OTIwMjI3MTcwODk2NDE5NDg2NA==&uploadsign=0&partseq=0 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: keep-alive
Content-Length: 4194496
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarycDXuXHaP3Nihj77H
Cookie: browserid=fTjwmhvyYzXgh0GuI4u7GxQrZ5Rw29SlLE69fh2SqigTr9vHrjRRuOVBzZI=; __bid_n=1894a18c489bb3f5b74207; _ga=GA1.1.490507614.1689165293; ndus=YyTtnC7teHuibUJkw3vAneWrxIgSxBWriTudMHPm; ab_sr=1.0.1_MWJmMTIyMjg0NzRhMDIzZjRlM2FiMzgyMTA1YTU0ZDIyNTRkOTEzZDkyYzdmOGUyYTAwMTg4NDllNGQyNTJmMzViZTU0YmNlZmU4Y2RlZjMwNmEyYjQzZTQ0OWY3ZWQwNDI3NjljNDFkYzNjNGQ2MGFmYzljOTg2YThmYjIzZDEyNjQ1MzM4ZTBjMmI3ZjM2YjgyNjJjMmZlNTE5MjNkMg==; _ga_06ZNKL8C2E=GS1.1.1689603635.5.1.1689603669.26.0.0
Host: c-jp.terabox.com
Origin: https://www.terabox.com
Referer: https://www.terabox.com/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
```

### Response

```json
{
    "md5":"4d810aa20f190c120cc7652d3a28b5c8",
    "partseq":0,
    "request_id":4590586496904938667,"uploadid":"P1-MTAuMjUyLjcxLjQ0OjE2ODk2MDM2NjQ6OTIwMjI3MTcwODk2NDE5NDg2NA=="
}
```

### Response Headers

```http
HTTP/1.1 200 OK
Date: Mon, 17 Jul 2023 14:23:26 GMT
Content-Type: text/html;charset=utf8
Connection: keep-alive
x-bs-version: e100fb530c9eaadccdec7d8fa9c01cc7
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: HEAD, GET, OPTIONS, PUT, POST, DELETE
Access-Control-Allow-Origin: https://www.terabox.com
x-bs-client-ip: MTEyLjEzNC43Mi4xNzY=
x-bs-file-size: 4194304
x-poms-part-key: e100fb530c9eaadccdec7d8fa9c01cc7
x-bs-meta-crc32: 3590152141
Content-MD5: 4d810aa20f190c120cc7652d3a28b5c8
Access-Control-Expose-Headers: Accept-Ranges, Content-Range, Content-Length, ETag, x-bs-request-id
Access-Control-Allow-Headers: Range, Origin, Content-Type, Accept, Content-Length
x-bs-request-id: MTAuMjUyLjE0My4yMzA6MjA0NTo0NTkwNTg2NDk2OTA0OTM4NjY3OjIwMjMtMDctMTcgMjI6MjE6MDc=
Content-Length: 164
Status: 200
Server: TERABOX UI
```

# https://c-jp.terabox.com/rest/2.0/pcs/superfile2 #last

### Request

```shell
curl 'https://c-jp.terabox.com/rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=dubox&clienttype=0&web=1&logid=MTY4OTYwMzYzNTgxNjAuODU5Mzg2NDE0OTQ4MTc4OQ==&path=%2Fpexels-felix-mittermeier-957040.jpg&uploadid=P1-MTAuMjUyLjcxLjQ0OjE2ODk2MDM2NjQ6OTIwMjI3MTcwODk2NDE5NDg2NA==&uploadsign=0&partseq=2' \
  -H 'Accept: */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryg23Y9XyrNtZxiBaJ' \
  -H 'Cookie: browserid=fTjwmhvyYzXgh0GuI4u7GxQrZ5Rw29SlLE69fh2SqigTr9vHrjRRuOVBzZI=; __bid_n=1894a18c489bb3f5b74207; _ga=GA1.1.490507614.1689165293; ndus=YyTtnC7teHuibUJkw3vAneWrxIgSxBWriTudMHPm; ab_sr=1.0.1_MWJmMTIyMjg0NzRhMDIzZjRlM2FiMzgyMTA1YTU0ZDIyNTRkOTEzZDkyYzdmOGUyYTAwMTg4NDllNGQyNTJmMzViZTU0YmNlZmU4Y2RlZjMwNmEyYjQzZTQ0OWY3ZWQwNDI3NjljNDFkYzNjNGQ2MGFmYzljOTg2YThmYjIzZDEyNjQ1MzM4ZTBjMmI3ZjM2YjgyNjJjMmZlNTE5MjNkMg==; _ga_06ZNKL8C2E=GS1.1.1689603635.5.1.1689603671.24.0.0' \
  -H 'Origin: https://www.terabox.com' \
  -H 'Referer: https://www.terabox.com/' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-site' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82' \
  -H 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw $'------WebKitFormBoundaryg23Y9XyrNtZxiBaJ\r\nContent-Disposition: form-data; name="file"; filename="blob"\r\nContent-Type: application/octet-stream\r\n<DATA>\r\n------WebKitFormBoundaryg23Y9XyrNtZxiBaJ--\r\n' \
  --compressed
```

### Requeat Headers

```http
POST /rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=dubox&clienttype=0&web=1&logid=MTY4OTYwMzYzNTgxNjAuODU5Mzg2NDE0OTQ4MTc4OQ==&path=%2Fpexels-felix-mittermeier-957040.jpg&uploadid=P1-MTAuMjUyLjcxLjQ0OjE2ODk2MDM2NjQ6OTIwMjI3MTcwODk2NDE5NDg2NA==&uploadsign=0&partseq=2 HTTP/1.1
Accept: */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: keep-alive
Content-Length: 2749837
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryg23Y9XyrNtZxiBaJ
Cookie: browserid=fTjwmhvyYzXgh0GuI4u7GxQrZ5Rw29SlLE69fh2SqigTr9vHrjRRuOVBzZI=; __bid_n=1894a18c489bb3f5b74207; _ga=GA1.1.490507614.1689165293; ndus=YyTtnC7teHuibUJkw3vAneWrxIgSxBWriTudMHPm; ab_sr=1.0.1_MWJmMTIyMjg0NzRhMDIzZjRlM2FiMzgyMTA1YTU0ZDIyNTRkOTEzZDkyYzdmOGUyYTAwMTg4NDllNGQyNTJmMzViZTU0YmNlZmU4Y2RlZjMwNmEyYjQzZTQ0OWY3ZWQwNDI3NjljNDFkYzNjNGQ2MGFmYzljOTg2YThmYjIzZDEyNjQ1MzM4ZTBjMmI3ZjM2YjgyNjJjMmZlNTE5MjNkMg==; _ga_06ZNKL8C2E=GS1.1.1689603635.5.1.1689603671.24.0.0
Host: c-jp.terabox.com
Origin: https://www.terabox.com
Referer: https://www.terabox.com/
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-site
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
```

### Response

```json
{
    "md5":"72639b005f1a92bebc0bbfb3a80f8072",
    "partseq":2,
    "request_id":4590587576306931473,"uploadid":"P1-MTAuMjUyLjcxLjQ0OjE2ODk2MDM2NjQ6OTIwMjI3MTcwODk2NDE5NDg2NA=="
}
```

### Response Headers

```http
HTTP/1.1 200 OK
Date: Mon, 17 Jul 2023 14:22:58 GMT
Content-Type: text/html;charset=utf8
Connection: keep-alive
x-bs-version: 7248e9a3e38eda705091acfae7b25379
Access-Control-Allow-Credentials: true
Access-Control-Allow-Methods: HEAD, GET, OPTIONS, PUT, POST, DELETE
Access-Control-Allow-Origin: https://www.terabox.com
x-bs-client-ip: MTEyLjEzNC43Mi4xNzY=
x-bs-file-size: 2749645
x-poms-part-key: 7248e9a3e38eda705091acfae7b25379
x-bs-meta-crc32: 3740421796
Content-MD5: 72639b005f1a92bebc0bbfb3a80f8072
Access-Control-Expose-Headers: Accept-Ranges, Content-Range, Content-Length, ETag, x-bs-request-id
Access-Control-Allow-Headers: Range, Origin, Content-Type, Accept, Content-Length
x-bs-request-id: MTAuMjUyLjE0Mi4yMDE6MjAwNTo0NTkwNTg3NTc2MzA2OTMxNDczOjIwMjMtMDctMTcgMjI6MjE6MTE=
Content-Length: 164
Status: 200
Server: TERABOX UI
```