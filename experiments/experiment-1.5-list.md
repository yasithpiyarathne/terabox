# https://www.terabox.com/api/list

### Request

```shell
curl 'https://www.terabox.com/api/list?app_id=250528&web=1&channel=dubox&clienttype=0&jsToken=8A14D63B1B122DF8F98558109DDF5DB4509ED215EE4EA0B9DE297C7D8A423991D6F171D2C5FAFC37C61C54172F88221912688A98A4E8750641B41417BB3EFFA1&dp-logid=58655600325954600015&order=time&desc=1&dir=%2F&num=100&page=1&showempty=0' \
  -H 'Accept: application/json, text/plain, */*' \
  -H 'Accept-Language: en-US,en;q=0.9' \
  -H 'Connection: keep-alive' \
  -H 'Content-Type: application/x-www-form-urlencoded' \
  -H 'Cookie: browserid=fTjwmhvyYzXgh0GuI4u7GxQrZ5Rw29SlLE69fh2SqigTr9vHrjRRuOVBzZI=; lang=en; __bid_n=1894a18c489bb3f5b74207; _ga=GA1.1.490507614.1689165293; g_state={"i_l":0}; ndus=YyTtnC7teHuibUJkw3vAneWrxIgSxBWriTudMHPm; csrfToken=7PLZE_YtmYQEWU7o2Gqv8mnW; ndut_fmt=33C9A43AB77F53FDBD45DC0AE9E521B1F79CB3B4F3EEA33B70AAC41DF1618052; ab_sr=1.0.1_MWJmMTIyMjg0NzRhMDIzZjRlM2FiMzgyMTA1YTU0ZDIyNTRkOTEzZDkyYzdmOGUyYTAwMTg4NDllNGQyNTJmMzViZTU0YmNlZmU4Y2RlZjMwNmEyYjQzZTQ0OWY3ZWQwNDI3NjljNDFkYzNjNGQ2MGFmYzljOTg2YThmYjIzZDEyNjQ1MzM4ZTBjMmI3ZjM2YjgyNjJjMmZlNTE5MjNkMg==; _ga_06ZNKL8C2E=GS1.1.1689603635.5.1.1689603821.55.0.0' \
  -H 'Referer: https://www.terabox.com/main?category=all' \
  -H 'Sec-Fetch-Dest: empty' \
  -H 'Sec-Fetch-Mode: cors' \
  -H 'Sec-Fetch-Site: same-origin' \
  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.82' \
  -H 'X-Requested-With: XMLHttpRequest' \
  -H 'sec-ch-ua: "Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"' \
  -H 'sec-ch-ua-mobile: ?0' \
  -H 'sec-ch-ua-platform: "Windows"' \
  --compressed
```

### Request Params

```json
{
    "app_id": "250528",
    "web":  "1",
    "channel":  "dubox",
    "clienttype":  "0",
    "jsToken": "8A14D63B1B122DF8F98558109DDF5DB4509ED215EE4EA0B9DE297C7D8A423991D6F171D2C5FAFC37C61C54172F88221912688A98A4E8750641B41417BB3EFFA1",
    "dp-logid": "58655600325954600015",
    "order":  "time",
    "desc":  "1",
    "dir":  "/",
    "num":  "100",
    "page":  "1",
    "showempty":  "0"
}
```

### Request Headers

```http
GET /api/list?app_id=250528&web=1&channel=dubox&clienttype=0&jsToken=8A14D63B1B122DF8F98558109DDF5DB4509ED215EE4EA0B9DE297C7D8A423991D6F171D2C5FAFC37C61C54172F88221912688A98A4E8750641B41417BB3EFFA1&dp-logid=58655600325954600015&order=time&desc=1&dir=%2F&num=100&page=1&showempty=0 HTTP/1.1
Accept: application/json, text/plain, */*
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Cookie: browserid=fTjwmhvyYzXgh0GuI4u7GxQrZ5Rw29SlLE69fh2SqigTr9vHrjRRuOVBzZI=; lang=en; __bid_n=1894a18c489bb3f5b74207; _ga=GA1.1.490507614.1689165293; g_state={"i_l":0}; ndus=YyTtnC7teHuibUJkw3vAneWrxIgSxBWriTudMHPm; csrfToken=7PLZE_YtmYQEWU7o2Gqv8mnW; ndut_fmt=33C9A43AB77F53FDBD45DC0AE9E521B1F79CB3B4F3EEA33B70AAC41DF1618052; ab_sr=1.0.1_MWJmMTIyMjg0NzRhMDIzZjRlM2FiMzgyMTA1YTU0ZDIyNTRkOTEzZDkyYzdmOGUyYTAwMTg4NDllNGQyNTJmMzViZTU0YmNlZmU4Y2RlZjMwNmEyYjQzZTQ0OWY3ZWQwNDI3NjljNDFkYzNjNGQ2MGFmYzljOTg2YThmYjIzZDEyNjQ1MzM4ZTBjMmI3ZjM2YjgyNjJjMmZlNTE5MjNkMg==; _ga_06ZNKL8C2E=GS1.1.1689603635.5.1.1689603821.55.0.0
Host: www.terabox.com
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
{"errno":0,"guid_info":"","list":[{"tkbind_id":0,"owner_type":0,"category":3,"real_category":"","isdir":0,"server_filename":"pexels-felix-mittermeier-957040.jpg","unlist":0,"oper_id":4400726073869,"server_ctime":1689603818,"extent_tinyint7":0,"wpfile":0,"owner_id":0,"local_mtime":1689345573,"size":11138253,"server_mtime":1689603818,"md5":"e6c6bf448c998ebfdaa5a7c72e86d256","share":0,"path":"\/pexels-felix-mittermeier-957040.jpg","from_type":1,"local_ctime":1689603818,"play_forbid":0,"pl":0,"thumbs":{"icon":"https:\/\/data.terabox.com\/thumbnail\/e6c6bf448c998ebfdaa5a7c72e86d256?fid=4400726073869-250528-289274241396020&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-ctuq051u%2bPwJ8cWew0t8VJqv1W0%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c60_u60&quality=100&vuk=4400726073869&ft=image","url3":"https:\/\/data.terabox.com\/thumbnail\/e6c6bf448c998ebfdaa5a7c72e86d256?fid=4400726073869-250528-289274241396020&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-ctuq051u%2bPwJ8cWew0t8VJqv1W0%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c850_u580&quality=100&vuk=4400726073869&ft=image","url2":"https:\/\/data.terabox.com\/thumbnail\/e6c6bf448c998ebfdaa5a7c72e86d256?fid=4400726073869-250528-289274241396020&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-ctuq051u%2bPwJ8cWew0t8VJqv1W0%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c360_u270&quality=100&vuk=4400726073869&ft=image","url1":"https:\/\/data.terabox.com\/thumbnail\/e6c6bf448c998ebfdaa5a7c72e86d256?fid=4400726073869-250528-289274241396020&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-ctuq051u%2bPwJ8cWew0t8VJqv1W0%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c140_u90&quality=100&vuk=4400726073869&ft=image"},"server_atime":0,"fs_id":289274241396020},{"tkbind_id":0,"owner_type":0,"category":5,"real_category":"","isdir":0,"md5":"5277068968032af616e7e4cc86f1d3c2","oper_id":4400726073869,"fs_id":785525597377807,"server_atime":0,"server_ctime":1689589989,"play_forbid":0,"wpfile":0,"extent_tinyint7":0,"local_mtime":1689589989,"size":110628872,"from_type":1,"share":0,"pl":0,"path":"\/VirtualBox-7.0.8-156879-Win.exe","local_ctime":1689589989,"server_filename":"VirtualBox-7.0.8-156879-Win.exe","server_mtime":1689589989,"owner_id":0,"unlist":0},{"tkbind_id":0,"server_mtime":1689588089,"category":4,"unlist":0,"isdir":0,"wpfile":0,"local_mtime":1689588089,"share":0,"pl":0,"docpreview":"https:\/\/data.terabox.com\/doc\/f9baa9c2060c4d19b49169e9e475d133?fid=4400726073869-250528-761953408070172&time=1689603820&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-3zSazryWeVkl5jfO3GxGSWpe7fI%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0","owner_type":0,"real_category":"","server_ctime":1689588089,"extent_tinyint7":0,"owner_id":0,"thumbs":{"url3":"https:\/\/data.terabox.com\/thumbnail\/f9baa9c2060c4d19b49169e9e475d133?fid=4400726073869-250528-761953408070172&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-CY9AXPPEFVq3J%2bm62AtgOEXKSSY%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c850_u580&quality=100","url2":"https:\/\/data.terabox.com\/thumbnail\/f9baa9c2060c4d19b49169e9e475d133?fid=4400726073869-250528-761953408070172&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-CY9AXPPEFVq3J%2bm62AtgOEXKSSY%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c360_u270&quality=100","url1":"https:\/\/data.terabox.com\/thumbnail\/f9baa9c2060c4d19b49169e9e475d133?fid=4400726073869-250528-761953408070172&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-CY9AXPPEFVq3J%2bm62AtgOEXKSSY%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c140_u90&quality=100"},"size":913,"lodocpreview":"https:\/\/data.terabox.com\/doc\/f9baa9c2060c4d19b49169e9e475d133?fid=4400726073869-250528-761953408070172&time=1689603820&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-3zSazryWeVkl5jfO3GxGSWpe7fI%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&type=pdf&from=lo","fs_id":761953408070172,"from_type":1,"path":"\/README-cloudshell.txt","local_ctime":1689588089,"play_forbid":0,"server_filename":"README-cloudshell.txt","md5":"f9baa9c2060c4d19b49169e9e475d133","oper_id":4400726073869,"server_atime":0},{"tkbind_id":0,"owner_type":0,"category":6,"real_category":"","isdir":0,"md5":"6c881f759e1c40814eb9ee4e32945815","oper_id":4400726073869,"fs_id":1056928453142258,"server_atime":0,"server_ctime":1689587861,"play_forbid":0,"wpfile":0,"extent_tinyint7":0,"local_mtime":1689587861,"size":360,"from_type":1,"share":0,"pl":0,"path":"\/setup_20230717_175741.py","local_ctime":1689587861,"server_filename":"setup_20230717_175741.py","server_mtime":1689587861,"owner_id":0,"unlist":0},{"tkbind_id":0,"owner_type":0,"category":6,"real_category":"","isdir":0,"md5":"6c881f759e1c40814eb9ee4e32945815","oper_id":4400726073869,"fs_id":1091328538384527,"server_atime":0,"server_ctime":1689587806,"play_forbid":0,"wpfile":0,"extent_tinyint7":0,"local_mtime":1689587806,"size":360,"from_type":1,"share":0,"pl":0,"path":"\/setup_20230717_175646.py","local_ctime":1689587806,"server_filename":"setup_20230717_175646.py","server_mtime":1689587806,"owner_id":0,"unlist":0},{"tkbind_id":0,"owner_type":0,"category":6,"real_category":"","isdir":0,"md5":"6c881f759e1c40814eb9ee4e32945815","oper_id":4400726073869,"fs_id":626275629108297,"server_atime":0,"server_ctime":1689586805,"play_forbid":0,"wpfile":0,"extent_tinyint7":0,"local_mtime":1689586805,"size":360,"from_type":1,"share":0,"pl":0,"path":"\/setup.py","local_ctime":1689586805,"server_filename":"setup.py","server_mtime":1689586805,"owner_id":0,"unlist":0},{"tkbind_id":0,"server_mtime":1689165495,"category":4,"unlist":0,"isdir":0,"wpfile":0,"local_mtime":1687189010,"share":0,"pl":0,"docpreview":"https:\/\/data.terabox.com\/doc\/704265289ceff6d959f125302cde283b?fid=4400726073869-250528-387216323924241&time=1689603820&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-Q9%2fPl3AKRCN2FuLVV9%2frY9tFxwg%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0","owner_type":0,"real_category":"","server_ctime":1689165495,"extent_tinyint7":0,"owner_id":0,"thumbs":{"url3":"https:\/\/data.terabox.com\/thumbnail\/704265289ceff6d959f125302cde283b?fid=4400726073869-250528-387216323924241&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-vcv0efWGxETI7vFBAm2jATcHoDM%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c850_u580&quality=100","url2":"https:\/\/data.terabox.com\/thumbnail\/704265289ceff6d959f125302cde283b?fid=4400726073869-250528-387216323924241&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-vcv0efWGxETI7vFBAm2jATcHoDM%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c360_u270&quality=100","url1":"https:\/\/data.terabox.com\/thumbnail\/704265289ceff6d959f125302cde283b?fid=4400726073869-250528-387216323924241&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-vcv0efWGxETI7vFBAm2jATcHoDM%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c140_u90&quality=100"},"size":249356,"lodocpreview":"https:\/\/data.terabox.com\/doc\/704265289ceff6d959f125302cde283b?fid=4400726073869-250528-387216323924241&time=1689603820&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-Q9%2fPl3AKRCN2FuLVV9%2frY9tFxwg%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&type=pdf&from=lo","fs_id":387216323924241,"from_type":1,"path":"\/Asking permission for sportsmeet with expenses.pdf","local_ctime":1689165495,"play_forbid":0,"server_filename":"Asking permission for sportsmeet with expenses.pdf","md5":"704265289ceff6d959f125302cde283b","oper_id":4400726073869,"server_atime":0},{"tkbind_id":0,"server_mtime":1689165349,"category":4,"unlist":0,"isdir":0,"wpfile":0,"local_mtime":1678949703,"share":0,"pl":1,"docpreview":"https:\/\/data.terabox.com\/doc\/2e1a64e0bff2a48a372ddaefb4ef4ffa?fid=4400726073869-250528-21204795336438&time=1689603820&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-itnP9%2bJDIgXmcOg1im62dgnhouc%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0","owner_type":0,"real_category":"","server_ctime":1682860233,"extent_tinyint7":0,"owner_id":0,"thumbs":{"url3":"https:\/\/data.terabox.com\/thumbnail\/2e1a64e0bff2a48a372ddaefb4ef4ffa?fid=4400726073869-250528-21204795336438&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-%2bCPYggqEVwtz5wR47oL2Z099xhc%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c850_u580&quality=100","url2":"https:\/\/data.terabox.com\/thumbnail\/2e1a64e0bff2a48a372ddaefb4ef4ffa?fid=4400726073869-250528-21204795336438&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-%2bCPYggqEVwtz5wR47oL2Z099xhc%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c360_u270&quality=100","url1":"https:\/\/data.terabox.com\/thumbnail\/2e1a64e0bff2a48a372ddaefb4ef4ffa?fid=4400726073869-250528-21204795336438&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-%2bCPYggqEVwtz5wR47oL2Z099xhc%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&time=1689602400&size=c140_u90&quality=100"},"size":1203,"lodocpreview":"https:\/\/data.terabox.com\/doc\/2e1a64e0bff2a48a372ddaefb4ef4ffa?fid=4400726073869-250528-21204795336438&time=1689603820&rt=pr&sign=FDTAER-DCb740ccc5511e5e8fedcff06b081203-itnP9%2bJDIgXmcOg1im62dgnhouc%3d&expires=8h&chkbd=0&chkv=0&dp-logid=9202313395135682352&dp-callid=0&type=pdf&from=lo","fs_id":21204795336438,"from_type":3,"path":"\/TeraBoxQuickStartGuide.pdf","local_ctime":1682860233,"play_forbid":0,"server_filename":"TeraBoxQuickStartGuide.pdf","md5":"2e1a64e0bff2a48a372ddaefb4ef4ffa","oper_id":0,"server_atime":0}],"request_id":9202313395135682352,"guid":0}
```

### Response Headers

```http
HTTP/1.1 200 OK
Date: Mon, 17 Jul 2023 14:23:39 GMT
Content-Type: application/json; charset=UTF-8
Transfer-Encoding: chunked
Connection: keep-alive
Vary: Accept-Encoding
yld: 9202313395135682352
Cache-Control: no-cache
X-Powered-By: DuboxServer
P3P: CP=" OTI DSP COR IVA OUR IND COM "
yme: ZIGW+Ss3QEsWdTEHUmr/tG1MvuUZSxz0qQpNwyKK
Server: nginx
logid: 9202313395135682352
Flow-level: 3
Content-Encoding: gzip
```