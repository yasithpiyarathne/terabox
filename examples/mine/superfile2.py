import requests

cookies = {
    'browserid': 'fTjwmhvyYzXgh0GuI4u7GxQrZ5Rw29SlLE69fh2SqigTr9vHrjRRuOVBzZI=',
    '__bid_n': '1894a18c489bb3f5b74207',
    '_ga': 'GA1.1.490507614.1689165293',
    'ndus': 'YyTtnC7teHuiv8Gf5y1R_uIB-JFxxPkN4IAy1KZ7',
    'ab_sr': '1.0.1_MWM0MDc5ZDNmNmYwMDI5YjMyZWZkZTg0ODIxOWJmY2JjNzFlZjE2NWZkYzVlZGEyZmY1N2ZhN2FiM2I2NzJhNjlkN2YzNWM1NTc1MTcxMDljOGIyMDUwM2M5NWZmMzJhYjI4NzAwNzRmYmU5MGE0NjQ1MGUxMWMzMzk1MzU1MWI5MDUwZGZkYWZjMmZhZmE4ZDg0Njc0ZWNjNWJlMWJiZA==',
    '_ga_06ZNKL8C2E': 'GS1.1.1689212402.2.1.1689212633.11.0.0',
}

headers = {
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'multipart/form-data; boundary=----WebKitFormBoundary6mcMLSDVW7FDz6Gu',
    # 'Cookie': 'browserid=fTjwmhvyYzXgh0GuI4u7GxQrZ5Rw29SlLE69fh2SqigTr9vHrjRRuOVBzZI=; __bid_n=1894a18c489bb3f5b74207; _ga=GA1.1.490507614.1689165293; ndus=YyTtnC7teHuiv8Gf5y1R_uIB-JFxxPkN4IAy1KZ7; ab_sr=1.0.1_MWM0MDc5ZDNmNmYwMDI5YjMyZWZkZTg0ODIxOWJmY2JjNzFlZjE2NWZkYzVlZGEyZmY1N2ZhN2FiM2I2NzJhNjlkN2YzNWM1NTc1MTcxMDljOGIyMDUwM2M5NWZmMzJhYjI4NzAwNzRmYmU5MGE0NjQ1MGUxMWMzMzk1MzU1MWI5MDUwZGZkYWZjMmZhZmE4ZDg0Njc0ZWNjNWJlMWJiZA==; _ga_06ZNKL8C2E=GS1.1.1689212402.2.1.1689212633.11.0.0',
    'Origin': 'https://www.terabox.com',
    'Referer': 'https://www.terabox.com/',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

data = '------WebKitFormBoundary6mcMLSDVW7FDz6Gu\r\nContent-Disposition: form-data; name="file"; filename="blob"\r\nContent-Type: application/octet-stream\r\n\r\nhello\r\n------WebKitFormBoundary6mcMLSDVW7FDz6Gu--\r\n'

response = requests.post(
    'https://c-jp.terabox.com/rest/2.0/pcs/superfile2?method=upload&app_id=250528&channel=dubox&clienttype=0&web=1&logid=MTY4OTIxMjYwODI5NjAuNzc4NDE0MDAyOTUxNTU5OA==&path=%2Fhi.txt&uploadid=N1-MTEyLjEzNC43Mi42NToxNjg5MjEyNjI5OjkwOTczMDQxNDQxODA2NzcyMTY=&uploadsign=0&partseq=0',
    cookies=cookies,
    headers=headers,
    data=data,
)