import urllib.request
import urllib.parse
#v2transapi
url='https://fanyi.baidu.com/v2transapi?from=en&to=zh'
header={
    'user-agent':
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36 Edg/134.0.0.0',
    'cookie':
    'BAIDUID_BFESS=782CDBE42EADC8B59F4C4A2FBC3A317D:FG=1; BDUSS=XlIcjQzcUxxT0YxU09RdEdTOTNLNHRFa0dGblZQR3JyU0lsLWsyaUtEVUlyQU5vSVFBQUFBJCQAAAAAAQAAAAEAAAAtICCFbHVsYWx1bGFsZTAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgf3GcIH9xnN; BDUSS_BFESS=XlIcjQzcUxxT0YxU09RdEdTOTNLNHRFa0dGblZQR3JyU0lsLWsyaUtEVUlyQU5vSVFBQUFBJCQAAAAAAQAAAAEAAAAtICCFbHVsYWx1bGFsZTAwAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAgf3GcIH9xnN; __bid_n=195b3dd4a6f92166732420; RT="z=1&dm=baidu.com&si=27170818-6f0d-420e-86c2-f8db30694dbc&ss=m8k81xtm&sl=3&tt=4rw&bcn=https%3A%2F%2Ffclog.baidu.com%2Flog%2Fweirwood%3Ftype%3Dperf&ld=x3g"; smallFlowVersion=old; Hm_lvt_64ecd82404c51e03dc91cb9e8c025574=1742648889; REALTIME_TRANS_SWITCH=1; FANYI_WORD_SWITCH=1; HISTORY_SWITCH=1; SOUND_SPD_SWITCH=1; SOUND_PREFER_SWITCH=1; Hm_lpvt_64ecd82404c51e03dc91cb9e8c025574=1742649300; ab_sr=1.0.1_ODAzZjRjZTVlY2JkNjRjNzcyN2FmYjQ5NDZlYTI2YWY4ZWI3ZDU2NzY5YWFlZGZmN2IxNTRiNzZhYmI0ZDdkZTQzMmNkZjVhZjFhMDBmNWZjNDg1OGRiZGE4OWU3MTg1MTQwZjYwNmIwNzA4MjNiMjE2Y2Y0ZmM5NWYyMTNiOThjODcwZGQ1ZjQzYzM5OGZlMjY2NDE1NzI0NmZkZWJmM2Y5NWIwNjRmMWUzNDNmYmZlMzgxMDJjM2YwODNjOGU4'
}
data={
    'from': 'en',
    'to': 'zh',
    'query': 'love',
    'transtype': 'realtime',
    'simple_means_flag': '3',
    'sign': '198772.518981',
    'token': '17cedc0325ee76b5e88365ce7a784533',
    'domain': 'common',
    'ts': '1742649304240'
}
data=urllib.parse.urlencode(data).encode('utf-8')
# print(data)
request=urllib.request.Request(url=url,data=data,headers=header)
# print(request)
response=urllib.request.urlopen(request)
# print(response)
content=response.read().decode('utf-8')
# print(content)
import json
obj=json.loads(content)
print(obj)