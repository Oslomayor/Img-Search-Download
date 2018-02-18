# 11:01 PM, Feb 18th, 2018 @ home,Shangyu
# 图片搜索引擎
# 输入关键词，批量下载匹配的图片
# 通过图片爬虫实现
#




# 中文转GBK编码
def keyword2gbk(keyword):
    return str(keyword.encode('gbk')).strip('b\'').replace('\\x', '%')
