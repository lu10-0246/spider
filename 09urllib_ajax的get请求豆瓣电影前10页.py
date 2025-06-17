import urllib.request
import urllib.parse
# https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start=0&limit=20 第一页
# https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start=20&limit=20 第二页
# https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action=&start=40&limit=20 第三页
#start=(page-1)*20
def create_request(page):
    base_url='https://movie.douban.com/j/chart/top_list?type=10&interval_id=100%3A90&action='
    data={
        'start':'(page-1)*20',
        'limit':20
    }
    data=urllib.parse.urlencode(data)
    url=base_url+data
    # print(url)
    header={
        'user-agent':
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36'
    }
    request = urllib.request.Request(url=url, headers=header)
    return request
def get_content(request):
    response = urllib.request.urlopen(request)
    content=response.read().decode('utf-8')
    return content
def down_load(page,content):
    with open('douban_'+str(page)+'.json','w',encoding='utf-8') as fp:
        fp.write(content)
#程序入口
if __name__=='__main__':
    start_page=int(input("请输入起始页码"))
    end_page=int(input("请输入结束的页码"))
    #每一页都有自己的请求定制
    for page in range(start_page,end_page+1):
        # print(page)
        request=create_request(page)
        #获取响应的数据
        content=get_content(request)
        #下载
        down_load(page,content)




