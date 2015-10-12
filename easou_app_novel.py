# coding=utf-8
import requests
import json
import simplejson

class novel:
    def __init__(self):
        self.name=''
        self.gid=''
        self.nid=''

    def setnovel(self,name,gid,nid):
        self.name = name
        self.gid = gid
        self.nid =nid





def search_novel():
    keyword = raw_input('请输入小说关键字：')
    page = '1'
    url = 'http://api.easou.com/api/bookapp/search.m?word='+keyword+'&page_id='+page+'&count=20&cid=eef_'
    result = requests.get(url).content
    # print result
    jsonval = json.loads(result)
    number = 1
    for val in jsonval['items']:
        print '序号：',
        print number
        number +=1
        print '书名：',
        print val['name']
        print '作者：',
        print val['author']
        print
search_novel()












# 显示全部章节
# gid='14672722'
# nid='14812023'
# url = 'http://api.easou.com/api/bookapp/chapter_list.m?gid='+gid+'&nid='+nid+'&page_id=1&size=9999&cid=eef_'
# r = requests.get(url)
# print (r.content)









# data = ('gid=2861249%21%402861249%21%402861249%21%402861249%21%402861249%21%402861249%21%402861249%21%402861249%21%402861249%21%402861249&nid=14289062%21%4014289062%21%4014289062%21%4014289062%21%4014289062%21%4014289062%21%4014289062%21%4014289062%21%4014289062%21%4014289062&sort=81%21%4082%21%4083%21%4084%21%4085%21%4086%21%4087%21%4088%21%4089%21%4090&gsort=0%21%400%21%400%21%400%21%400%21%400%21%400%21%400%21%400%21%400&chapter_name=%25E8%2580%258D%25E6%25B5%2581%25E6%25B0%2593%21%40%25E8%2580%2581%25E7%2589%259B%25E5%2590%2583%25E5%25AB%25A9%25E8%258D%2589%25EF%25BC%2588%25E4%25B8%258A%25EF%25BC%2589%21%40%25E8%2580%2581%25E7%2589%259B%25E5%2590%2583%25E5%25AB%25A9%25E8%258D%2589%25EF%25BC%2588%25E4%25B8%258B%25EF%25BC%2589%21%40%25E8%259B%2587%25E6%2589%2593%25E4%25B8%2583%25E5%25AF%25B8%21%40%25E5%25B0%258F%25E5%2586%25A4%25E5%25AE%25B6%21%40%25E4%25BD%25A0%25E6%2598%25AF%25E6%2588%2591%25E7%259A%2584%21%40%25E6%2583%2585%25E5%2593%25A5%25E5%2593%25A5%21%40%25E7%25BE%258E%25E7%25BE%258A%25E7%25BE%258A%25E5%2592%258C%25E7%2581%25B0%25E5%25A4%25AA%25E7%258B%25BC%21%40%25E5%25B0%258F%25E4%25B9%2596%25E5%25AE%259D%21%40%25E5%2586%259B%25E8%25AE%25AD&sequence=80%21%4081%21%4082%21%4083%21%4084%21%4085%21%4086%21%4087%21%4088%21%4089'
#         )
# headers = {'Content-Type':'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip'}
# url ='http://api.easou.com/api/bookapp/batch_chapter.m?cid=eef_&version=002&os=ios&udid=76fbeddf8b73c8b0fc065e2296b767579d8fda38&appverion=1018&ch=bnf1349_10388_001'
# r = requests.post(url=url, data=data, headers=headers)
# print(r.content)   #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩

