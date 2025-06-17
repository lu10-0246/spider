import urllib.request
url="http://www.baidu.com/s?wd=ip"
header={
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }
request=urllib.request.Request(url=url,headers=header)
proxies={
    #协议：主机+端口
    'http':'192.168.200.1:2356'
}
#handle buile_opener open
handler=urllib.request.ProxyHandler(proxies=proxies)
opener=urllib.request.build_opener(handler)
response=opener.open(request)
content=response.read().decode('utf-8')
print(content)