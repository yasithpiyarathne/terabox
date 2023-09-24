# Upload a File

```shell

curl "https://www.terabox.com/api/precreate?channel=dubox&web=1&app_id=250528&clienttype=0&bdstoken=49785c4158da93b4ed3d7619c49e76a4" -X POST -H "User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0" -H "Accept: application/json, text/javascript, */*; q=0.01" -H "Accept-Language: en-US,en;q=0.5" --compressed -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With: XMLHttpRequest" -H "Origin: https://www.terabox.com" -H "Connection: keep-alive" -H "Referer: https://www.terabox.com/disk/home" -H "Cookie: browserid=DC92xGMqqIx7bbsfHbUrfJcTjCaM5UYN1RIM7hryxTb6S84rwr2RkY2N-Ss=; lang=en_US; G_ENABLED_IDPS=google; __stripe_mid=db6a0f0a-8f8c-41e6-93f5-d92c8849f31653ae5c; ndus=YSJIa8TteHuiIVhhRNQKVCcBfa_BEOLXWdUkmu3w; PANWEB=1" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" -H "DNT: 1" -H "Sec-GPC: 1" -H "Pragma: no-cache" -H "Cache-Control: no-cache" --data-raw "path="%"2Ftest2.txt&autoinit=1&target_path="%"2F&block_list="%"5B"%"225910a591dd8fc18c32a8f3df4fdc1761"%"22"%"5D&local_mtime=1637268601"

```

```shell
curl "https://c-all.terabox.com/rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=dubox&clienttype=0&web=1&path="%"2Ftest2.txt&uploadid=N1-NDIuMTEwLjEyOC43OjE2MzcyNjg2MDc6NTU1MjMyODk4NDkxNzg5ODA0&uploadsign=0&partseq=0" -X OPTIONS -H "User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0" -H "Accept: */*" -H "Accept-Language: en-US,en;q=0.5" --compressed -H "Access-Control-Request-Method: POST" -H "Referer: https://www.terabox.com/" -H "Origin: https://www.terabox.com" -H "Connection: keep-alive" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-site" -H "DNT: 1" -H "Sec-GPC: 1" -H "Pragma: no-cache" -H "Cache-Control: no-cache"
```

```shell

curl "https://c-all.terabox.com/rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=dubox&clienttype=0&web=1&path="%"2Ftest2.txt&uploadid=N1-NDIuMTEwLjEyOC43OjE2MzcyNjg2MDc6NTU1MjMyODk4NDkxNzg5ODA0&uploadsign=0&partseq=0" -X POST -H "User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0" -H "Accept: */*" -H "Accept-Language: en-US,en;q=0.5" --compressed -H "Content-Type: multipart/form-data; boundary=---------------------------36090081722035748343393853072" -H "Origin: https://www.terabox.com" -H "Connection: keep-alive" -H "Referer: https://www.terabox.com/" -H "Cookie: browserid=DC92xGMqqIx7bbsfHbUrfJcTjCaM5UYN1RIM7hryxTb6S84rwr2RkY2N-Ss=; ndus=YSJIa8TteHuiIVhhRNQKVCcBfa_BEOLXWdUkmu3w" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-site" -H "DNT: 1" -H "Sec-GPC: 1" -H "Pragma: no-cache" -H "Cache-Control: no-cache" --data-binary "-----------------------------36090081722035748343393853072"^

"Content-Disposition: form-data; name=""file""; filename=""blob"""^

"Content-Type: application/octet-stream"^

""^

"-----------------------------36090081722035748343393853072--"^

""
```

```shell

curl "https://www.terabox.com/api/create?isdir=0&rtype=1&channel=dubox&web=1&app_id=250528&clienttype=0&bdstoken=49785c4158da93b4ed3d7619c49e76a4" -X POST -H "User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0" -H "Accept: application/json, text/javascript, */*; q=0.01" -H "Accept-Language: en-US,en;q=0.5" --compressed -H "Content-Type: application/x-www-form-urlencoded; charset=UTF-8" -H "X-Requested-With: XMLHttpRequest" -H "Origin: https://www.terabox.com" -H "Connection: keep-alive" -H "Referer: https://www.terabox.com/disk/home" -H "Cookie: browserid=DC92xGMqqIx7bbsfHbUrfJcTjCaM5UYN1RIM7hryxTb6S84rwr2RkY2N-Ss=; lang=en_US; G_ENABLED_IDPS=google; __stripe_mid=db6a0f0a-8f8c-41e6-93f5-d92c8849f31653ae5c; ndus=YSJIa8TteHuiIVhhRNQKVCcBfa_BEOLXWdUkmu3w; PANWEB=1" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" -H "DNT: 1" -H "Sec-GPC: 1" -H "Pragma: no-cache" -H "Cache-Control: no-cache" --data-raw "path="%"2Ftest2.txt&size=19&uploadid=N1-NDIuMTEwLjEyOC43OjE2MzcyNjg2MDc6NTU1MjMyODk4NDkxNzg5ODA0&target_path="%"2F&block_list="%"5B"%"22a5890ace30a3e84d9118196c161aeec2"%"22"%"5D&local_mtime=1637268601"

```

## List

```shell

curl "https://www.terabox.com/api/list?order=time&desc=1&showempty=0&web=1&page=1&num=100&dir="%"2F&t=0.09737982273278334&channel=dubox&web=1&app_id=250528&clienttype=0&bdstoken=49785c4158da93b4ed3d7619c49e76a4" -H "User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0" -H "Accept: application/json, text/javascript, */*; q=0.01" -H "Accept-Language: en-US,en;q=0.5" --compressed -H "X-Requested-With: XMLHttpRequest" -H "Connection: keep-alive" -H "Referer: https://www.terabox.com/disk/home" -H "Cookie: browserid=DC92xGMqqIx7bbsfHbUrfJcTjCaM5UYN1RIM7hryxTb6S84rwr2RkY2N-Ss=; lang=en_US; G_ENABLED_IDPS=google; __stripe_mid=db6a0f0a-8f8c-41e6-93f5-d92c8849f31653ae5c; ndus=YSJIa8TteHuiIVhhRNQKVCcBfa_BEOLXWdUkmu3w; PANWEB=1" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" -H "DNT: 1" -H "Sec-GPC: 1" -H "Pragma: no-cache" -H "Cache-Control: no-cache"

```

## Checks

```shell
curl "https://www.terabox.com/api/quota?checkexpire=1&checkfree=1&channel=dubox&web=1&app_id=250528&clienttype=0&bdstoken=49785c4158da93b4ed3d7619c49e76a4" -H "User-Agent: Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0" -H "Accept: application/json, text/javascript, */*; q=0.01" -H "Accept-Language: en-US,en;q=0.5" --compressed -H "X-Requested-With: XMLHttpRequest" -H "Connection: keep-alive" -H "Referer: https://www.terabox.com/disk/home" -H "Cookie: browserid=DC92xGMqqIx7bbsfHbUrfJcTjCaM5UYN1RIM7hryxTb6S84rwr2RkY2N-Ss=; lang=en_US; G_ENABLED_IDPS=google; __stripe_mid=db6a0f0a-8f8c-41e6-93f5-d92c8849f31653ae5c; ndus=YSJIa8TteHuiIVhhRNQKVCcBfa_BEOLXWdUkmu3w; PANWEB=1" -H "Sec-Fetch-Dest: empty" -H "Sec-Fetch-Mode: cors" -H "Sec-Fetch-Site: same-origin" -H "DNT: 1" -H "Sec-GPC: 1" -H "Pragma: no-cache" -H "Cache-Control: no-cache"
```