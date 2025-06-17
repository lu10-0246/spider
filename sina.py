#新浪财经
import pandas as pd
from selenium import webdriver
# browser=webdriver.Chrome()
#无界面模式
# chrome_options=webdriver.ChromeOptions()
# chrome_options.add_argument('--headless')
# browser=webdriver.Chrome(options=chrome_options)

# browser.get("https://finance.sina.com.cn/realstock/company/sh600519/nc.shtml")
# data=browser.page_source
# print(data)

#上证综合指数
# import re
# p_price='<div id="price" class=".*?">(.*?)</div>'
# price=re.findall(p_price,data)
# print(price)

#市盈率
# p_pe='<th>市盈率<sup>TTM</sup>：</th>.*?<td>(.*?)</td>'
# pe=re.findall(p_pe,data,re.S)
# print(pe)

#获取api
# import requests
# url="http://hq.sinajs.cn/list=sh600519"
# res=requests.get(url).text
# print(res)

# Tushare直接获取股票数据
#tushare pro
import tushare as ts
import pandas as pd
# api获取从https://www.tushare.pro/官网进入后 个人主页 接口token
# pro=ts.pro_api("53ab72cf65edb3a61836011b93eb836550186f819158ec6cf35d5799")
# df=pro.daily(ts_code='600519.SH',start_date='20250101',end_date='20250524')
# df['trade_date']=pd.to_datetime(df['trade_date'])
# print(df)

# pandas 里的read_html()函数快速获取网页表格 requests用法
# import pandas as pd
# url="https://vip.stock.finance.sina.com.cn/q/go.php/vInvestConsult/kind/dzjy/index.phtml"
# table=pd.read_html(url,encoding='gbk')[0]
# print(table)
# table.to_excel('新浪财经大宗交易数据信息.xlsx',index=False)

#新浪财经资产负债表获取 selenium
from selenium import webdriver
chrome=webdriver.Chrome()
url="https://vip.stock.finance.sina.com.cn/corp/go.php/vFD_FinanceSummary/stockid/600519/displaytype/4.phtml"
chrome.get(url)
data=chrome.page_source
print(data)
import pandas as pd
table=pd.read_html(data)
for i in range(len(table)):
    print(i)
    print(table[i])
#上面获取到的页码
df=table[1]
print(df)
df.columns=df.iloc[0] #设置表头为原表格的第一行
df=df[1:] #从第二行开始整数据
df=df.dropna() #删除含有空值的行
print(df)
