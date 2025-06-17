import urllib.request
url="http://www.baidu.com"
header={
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }
request=urllib.request.Request(url=url,headers=header)
#handle buile_opener open
#获取handler对象
handler=urllib.request.HTTPHandler()
#获取opener对象
opener=urllib.request.build_opener(handler)
#调用open方法
response=opener.open(request)
content=response.read().decode('utf-8')
print(content)