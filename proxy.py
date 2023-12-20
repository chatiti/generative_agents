import requests

def test_proxy(proxy):
    url = 'https://github.com/penghuima/awesome-serverless-papers?tab=readme-ov-file#ccfb'  # 你可以替换为你要测试的网站 URL

    proxies = {
        'http': proxy,
        'https': proxy
    }

    try:
        response = requests.get(url, proxies=proxies, timeout=5)
        response.raise_for_status()  # 检查是否有错误状态码
        print(f"Proxy {proxy} is working. Response code: {response.status_code}")
    except requests.RequestException as e:
        print(f"Proxy {proxy} is not working. Error: {e}")

# 替换为你的代理地址（格式为 'http://ip:port' 或 'https://ip:port'）
proxy_list = [
    '1.94.30.47:3128',
    '101.132.25.152:91',
    '117.187.18.136:3128',
    '117.71.132.124:8089'
    '117.160.250.132:80',
    '117.160.250.132:8899',
    '117.160.250.130:80',
    '117.160.250.133:8899',
    '117.158.146.215:9091',
    '117.160.250.130:8899',
    '222.88.167.22:9002',
    '218.57.210.186:9002',
    '221.230.216.200:7788',
    '101.34.30.200:8081'
]

# 打印代理列表
for proxy_to_test in proxy_list:
    # 调用测试函数
    test_proxy("http://"+proxy_to_test)



