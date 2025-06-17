from lxml import etree
#解析本地文件
# etree.parse()
#解析服务器响应文件
# etree.HTML()

tree=etree.parse("18解析_xpath的基本使用.html")
#读取的文件只允许双标签
# print(tree)

    #路径查询
#//所有子孙节点  /子节点
#获取ul下的所有li
# li_list=tree.xpath("//ul/li/text()")
    #谓词查询
#查找所有带有id属性的li标签
# li_list=tree.xpath("//ul/li[@id]/text()")
#查找带有id属性为“1”的li标签  注意引号的使用
# li_list=tree.xpath("//ul/li[@id='l1']/text()")
    #属性查询
#查找带有id属性为“1”的li标签 的class的属性值
# li_list=tree.xpath("//ul/li[@id='l1']/@class")
    #模糊查询
#查询id中包含l的li标签
# li_list=tree.xpath("//ul/li[contains(@id,'l')]/text()")
#查询id的值以l开头的li标签
# li_list=tree.xpath("//ul/li[starts-with(@id,'c')]/text()")
    #逻辑查询
#查询id为l1或class为c1的
# li_list=tree.xpath("//ul/li[@id='l1' and @class='c1']/text()")
li_list=tree.xpath("//ul/li[@id='l1']/text() | //ul/li[@id='l2']/text()")
print(li_list)
print(len(li_list))

