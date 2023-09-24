# https://www.terabox.com/api/create

### Request

```shell
curl 'https://www.terabox.com/api/create?isdir=0&rtype=1&bdstoken=e322bda4a177b65e85928509397ab792&app_id=250528&web=1&channel=dubox&clienttype=0&jsToken=8A14D63B1B122DF8F98558109DDF5DB4509ED215EE4EA0B9DE297C7D8A423991D6F171D2C5FAFC37C61C54172F88221912688A98A4E8750641B41417BB3EFFA1&dp-logid=58655600325954600014' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: browserid=fTjwmhvyYzXgh0GuI4u7GxQrZ5Rw29SlLE69fh2SqigTr9vHrjRRuOVBzZI=; lang=en; __bid_n=1894a18c489bb3f5b74207; _ga=GA1.1.490507614.1689165293; g_state={"i_l":0}; ndus=YyTtnC7teHuibUJkw3vAneWrxIgSxBWriTudMHPm; csrfToken=7PLZE_YtmYQEWU7o2Gqv8mnW; ndut_fmt=33C9A43AB77F53FDBD45DC0AE9E521B1F79CB3B4F3EEA33B70AAC41DF1618052; ab_sr=1.0.1_MWJmMTIyMjg0NzRhMDIzZjRlM2FiMzgyMTA1YTU0ZDIyNTRkOTEzZDkyYzdmOGUyYTAwMTg4NDllNGQyNTJmMzViZTU0YmNlZmU4Y2RlZjMwNmEyYjQzZTQ0OWY3ZWQwNDI3NjljNDFkYzNjNGQ2MGFmYzljOTg2YThmYjIzZDEyNjQ1MzM4ZTBjMmI3ZjM2YjgyNjJjMmZlNTE5MjNkMg==; _ga_06ZNKL8C2E=GS1.1.1689603635.5.1.1689603821.55.0.0' \
  -H 'Origin: https://www.terabox.com' \
  -H 'Referer: https://www.terabox.com/main?category=all' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --data-raw 'path=%2Fpexels-felix-mittermeier-957040.jpg&size=11138253&uploadid=P1-MTAuMjUyLjcxLjQ0OjE2ODk2MDM2NjQ6OTIwMjI3MTcwODk2NDE5NDg2NA%3D%3D&target_path=%2F&block_list=%5B%224d810aa20f190c120cc7652d3a28b5c8%22%2C%222a0d47a18db5fe540f8b84368f403e08%22%2C%2272639b005f1a92bebc0bbfb3a80f8072%22%5D&local_mtime=1689345573' \
  --compressed
```

### Request Params

```json
{
    "isdir":  "0",
    "rtype": "1",
    "bdstoken": "e322bda4a177b65e85928509397ab792",
    "app_id": "250528",
    "web": "1",
    "channel":  "dubox",
    "clienttype": "0",
    "jsToken": "8A14D63B1B122DF8F98558109DDF5DB4509ED215EE4EA0B9DE297C7D8A423991D6F171D2C5FAFC37C61C54172F88221912688A98A4E8750641B41417BB3EFFA1",
    "dp-logid":  "58655600325954600014"
}
```

### Request Headers

```http
POST /api/create?isdir=0&rtype=1&bdstoken=e322bda4a177b65e85928509397ab792&app_id=250528&web=1&channel=dubox&clienttype=0&jsToken=8A14D63B1B122DF8F98558109DDF5DB4509ED215EE4EA0B9DE297C7D8A423991D6F171D2C5FAFC37C61C54172F88221912688A98A4E8750641B41417BB3EFFA1&dp-logid=58655600325954600014 HTTP/1.1
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: keep-alive
Content-Length: 311
Content-Type: application/x-www-form-urlencoded
Cookie: browserid=fTjwmhvyYzXgh0GuI4u7GxQrZ5Rw29SlLE69fh2SqigTr9vHrjRRuOVBzZI=; lang=en; __bid_n=1894a18c489bb3f5b74207; _ga=GA1.1.490507614.1689165293; g_state={"i_l":0}; ndus=YyTtnC7teHuibUJkw3vAneWrxIgSxBWriTudMHPm; csrfToken=7PLZE_YtmYQEWU7o2Gqv8mnW; ndut_fmt=33C9A43AB77F53FDBD45DC0AE9E521B1F79CB3B4F3EEA33B70AAC41DF1618052; ab_sr=1.0.1_MWJmMTIyMjg0NzRhMDIzZjRlM2FiMzgyMTA1YTU0ZDIyNTRkOTEzZDkyYzdmOGUyYTAwMTg4NDllNGQyNTJmMzViZTU0YmNlZmU4Y2RlZjMwNmEyYjQzZTQ0OWY3ZWQwNDI3NjljNDFkYzNjNGQ2MGFmYzljOTg2YThmYjIzZDEyNjQ1MzM4ZTBjMmI3ZjM2YjgyNjJjMmZlNTE5MjNkMg==; _ga_06ZNKL8C2E=GS1.1.1689603635.5.1.1689603821.55.0.0
Host: www.terabox.com
Origin: https://www.terabox.com
Referer: https://www.terabox.com/main?category=all
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: cors
Sec-Fetch-Site: same-origin
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82
X-Requested-With: XMLHttpRequest
sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"
sec-ch-ua-mobile: ?0
sec-ch-ua-platform: "Windows"
```

### Response

```json
{
    "ctime":1689603818,
    "from_type":1,
    "fs_id":289274241396020,
    "isdir":0,
    "md5":"8dbacbd86v6d72ab2fa59731530e6a28",
    "mtime":1689603818,
    "path":"\/pexels-felix-mittermeier-957040.jpg","size":"11138253",
    "errno":0,
    "name":"\/pexels-felix-mittermeier-957040.jpg",
    "category":3
}
```

### Response Headers

```http
HTTP/1.1 200 OK
Date: Mon, 17 Jul 2023 14:23:38 GMT
Content-Type: application/json; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
Vary: Accept-Encoding
yld: 9202313031197315255
Cache-Control: no-cache
X-Powered-By: DuboxServer
P3P: CP=" OTI DSP COR IVA OUR IND COM "
yme: ZIGW+Ss3QEsWdTEHUmr/tG1MvuUZShzxqApNwyaLpdf4Ew44IefnrHsW3A==
Server: nginx
logid: 9202313031197315255
Flow-level: 3
Content-Encoding: gzip
```