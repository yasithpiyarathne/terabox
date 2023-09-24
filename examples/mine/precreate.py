import requests

cookies = {
    'browserid': 'fTjwmhvyYzXgh0GuI4u7GxQrZ5Rw29SlLE69fh2SqigTr9vHrjRRuOVBzZI=',
    'lang': 'en',
    '__bid_n': '1894a18c489bb3f5b74207',
    '_ga': 'GA1.1.490507614.1689165293',
    'g_state': '{"i_l":0}',
    'ndus': 'YyTtnC7teHuiv8Gf5y1R_uIB-JFxxPkN4IAy1KZ7',
    'csrfToken': '2WlTxeDpkvb75TnuD8Mrhrvu',
    'ndut_fmt': '2953ACDE765F7DA3B3FD61967EBB8CAA13650639E34F94BF353FC8B8A97AFD27',
    'ab_sr': '1.0.1_MWM0MDc5ZDNmNmYwMDI5YjMyZWZkZTg0ODIxOWJmY2JjNzFlZjE2NWZkYzVlZGEyZmY1N2ZhN2FiM2I2NzJhNjlkN2YzNWM1NTc1MTcxMDljOGIyMDUwM2M5NWZmMzJhYjI4NzAwNzRmYmU5MGE0NjQ1MGUxMWMzMzk1MzU1MWI5MDUwZGZkYWZjMmZhZmE4ZDg0Njc0ZWNjNWJlMWJiZA==',
    '_ga_06ZNKL8C2E': 'GS1.1.1689212402.2.1.1689212633.11.0.0',
}

headers = {
    'Accept': 'application/json, text/plain, */*',
    'Accept-Language': 'en-US,en;q=0.9',
    'Connection': 'keep-alive',
    'Content-Type': 'application/x-www-form-urlencoded',
    # 'Cookie': 'browserid=fTjwmhvyYzXgh0GuI4u7GxQrZ5Rw29SlLE69fh2SqigTr9vHrjRRuOVBzZI=; lang=en; __bid_n=1894a18c489bb3f5b74207; _ga=GA1.1.490507614.1689165293; g_state={"i_l":0}; ndus=YyTtnC7teHuiv8Gf5y1R_uIB-JFxxPkN4IAy1KZ7; csrfToken=2WlTxeDpkvb75TnuD8Mrhrvu; ndut_fmt=2953ACDE765F7DA3B3FD61967EBB8CAA13650639E34F94BF353FC8B8A97AFD27; ab_sr=1.0.1_MWM0MDc5ZDNmNmYwMDI5YjMyZWZkZTg0ODIxOWJmY2JjNzFlZjE2NWZkYzVlZGEyZmY1N2ZhN2FiM2I2NzJhNjlkN2YzNWM1NTc1MTcxMDljOGIyMDUwM2M5NWZmMzJhYjI4NzAwNzRmYmU5MGE0NjQ1MGUxMWMzMzk1MzU1MWI5MDUwZGZkYWZjMmZhZmE4ZDg0Njc0ZWNjNWJlMWJiZA==; _ga_06ZNKL8C2E=GS1.1.1689212402.2.1.1689212633.11.0.0',
    'Origin': 'https://www.terabox.com',
    'Referer': 'https://www.terabox.com/main?category=all',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.79',
    'X-Requested-With': 'XMLHttpRequest',
    'sec-ch-ua': '"Not.A/Brand";v="8", "Chromium";v="114", "Microsoft Edge";v="114"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'app_id': '250528',
    'web': '1',
    'channel': 'dubox',
    'clienttype': '0',
    'jsToken': '8A14D63B1B122DF8F98558109DDF5DB4B5C791351BA5817BE167F5385A8778E9F0149B427C1DC8655435BBB77EB0EA899439DABEC7E20CB91FF2A261A61CBF50',
    'dp-logid': '31664100925114430012',
}

data = {
    'path': '/hi.txt',
    'autoinit': '1',
    'target_path': '/',
    'block_list': '["5910a591dd8fc18c32a8f3df4fdc1761"]',
    'local_mtime': '1689190692',
}

response = requests.post('https://www.terabox.com/api/precreate', params=params, cookies=cookies, headers=headers, data=data)