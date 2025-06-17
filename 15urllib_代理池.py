import urllib.request
proxies_pool=[
    {'http':'172.129.0.1:3306'},
    {'http':'192.168.31.121:2356'}
]
import random
proxies=random.choice(proxies_pool)

url="http://www.baidu.com/s?wd=ip"
header={
'user-agent':
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
}
request=urllib.request.Request(url,header)
handler=urllib.request.ProxyHandler(proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
content=response.read().decode('utf-8')
print(content)