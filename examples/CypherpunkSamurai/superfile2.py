import requests

cookies = {
    'browserid': 'DC92xGMqqIx7bbsfHbUrfJcTjCaM5UYN1RIM7hryxTb6S84rwr2RkY2N-Ss=',
    'ndus': 'YSJIa8TteHuiIVhhRNQKVCcBfa_BEOLXWdUkmu3w',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept': '*/*',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'multipart/form-data; boundary=---------------------------36090081722035748343393853072',
    'Origin': 'https://www.terabox.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.terabox.com/',
    # 'Cookie': 'browserid=DC92xGMqqIx7bbsfHbUrfJcTjCaM5UYN1RIM7hryxTb6S84rwr2RkY2N-Ss=; ndus=YSJIa8TteHuiIVhhRNQKVCcBfa_BEOLXWdUkmu3w',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-site',
    'DNT': '1',
    'Sec-GPC': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = {
    'method': 'upload',
    'app_id': '250528',
    'channel': 'dubox',
    'clienttype': '0',
    'web': '1',
    'path': '/test2.txt',
    'uploadid': 'N1-NDIuMTEwLjEyOC43OjE2MzcyNjg2MDc6NTU1MjMyODk4NDkxNzg5ODA0',
    'uploadsign': '0',
    'partseq': '0',
}

data = '-----------------------------36090081722035748343393853072^'

response = requests.post(
    'https://c-all.terabox.com/rest/2.0/pcs/superfile2',
    params=params,
    cookies=cookies,
    headers=headers,
    data=data,
)