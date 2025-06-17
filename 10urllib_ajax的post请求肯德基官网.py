#第一页
# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 1
# pageSize: 10

#第二页
# https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname
# cname: 北京
# pid:
# pageIndex: 2
# pageSize: 10

import urllib.request
import urllib.parse

def create_request(page):
    base_url = "https://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=cname"
    data={
        'cname': '北京',
        'pid':'',
        'pageIndex': page,
        'pageSize': 10
    }
    #post请求必须编码
    data=urllib.parse.urlencode(data).encode('utf-8')
    header = {
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }
    request=urllib.request.Request(url=base_url,headers=header,data=data)
    return request
def get_content(request):
    response=urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content
def down_load(page,content):
    with open('kfc_'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)
if __name__=="__main__":
    start_page=int(input("请输入起始页码"))
    end_page=int(input("请输入结束页码"))
    for page in range(start_page,end_page+1):
        # print(page)
        #请求定制
        request=create_request(page)
        #内容响应
        content=get_content(request)
        #下载
        down_load(page,content)
