import requests

cookies = {
    'browserid': 'DC92xGMqqIx7bbsfHbUrfJcTjCaM5UYN1RIM7hryxTb6S84rwr2RkY2N-Ss=',
    'lang': 'en_US',
    'G_ENABLED_IDPS': 'google',
    '__stripe_mid': 'db6a0f0a-8f8c-41e6-93f5-d92c8849f31653ae5c',
    'ndus': 'YSJIa8TteHuiIVhhRNQKVCcBfa_BEOLXWdUkmu3w',
    'PANWEB': '1',
}

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64; rv:94.0) Gecko/20100101 Firefox/94.0',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'en-US,en;q=0.5',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'X-Requested-With': 'XMLHttpRequest',
    'Origin': 'https://www.terabox.com',
    'Connection': 'keep-alive',
    'Referer': 'https://www.terabox.com/disk/home',
    # 'Cookie': 'browserid=DC92xGMqqIx7bbsfHbUrfJcTjCaM5UYN1RIM7hryxTb6S84rwr2RkY2N-Ss=; lang=en_US; G_ENABLED_IDPS=google; __stripe_mid=db6a0f0a-8f8c-41e6-93f5-d92c8849f31653ae5c; ndus=YSJIa8TteHuiIVhhRNQKVCcBfa_BEOLXWdUkmu3w; PANWEB=1',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'DNT': '1',
    'Sec-GPC': '1',
    'Pragma': 'no-cache',
    'Cache-Control': 'no-cache',
}

params = {
    'isdir': '0',
    'rtype': '1',
    'channel': 'dubox',
    'web': '1',
    'app_id': '250528',
    'clienttype': '0',
    'bdstoken': '49785c4158da93b4ed3d7619c49e76a4',
}

data = {
    'path': '/test2.txt',
    'size': '19',
    'uploadid': 'N1-NDIuMTEwLjEyOC43OjE2MzcyNjg2MDc6NTU1MjMyODk4NDkxNzg5ODA0',
    'target_path': '/',
    'block_list': '["a5890ace30a3e84d9118196c161aeec2"]',
    'local_mtime': '1637268601',
}

response = requests.post('https://www.terabox.com/api/create', params=params, cookies=cookies, headers=headers, data=data)