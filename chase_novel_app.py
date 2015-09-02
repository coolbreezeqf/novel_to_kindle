# -*- coding:utf-8 -*-
#coding:utf-8
__author__ = 'cheng'

import urllib2
import json
import re
import requests


class Novel():
    def __init__(self):
        '''
        初始化内部共享变量
        '''
        self.keyword='测试'
        self.chapterlist =[]
        pass




    def get_novelid(self):
        '''
        以命令行形式获取输入关键字,返回小说ID
        '''
        novellist_url='http://api.zhuishushenqi.com/book/fuzzy-search?query='+str(self.keyword)
        # novellist_url=unicode(novellist_url,'utf-8') #修改编码模式
        search_content=requests.get(novellist_url).text #获取搜索页内容
        # print search_content #测试获取网页内容
        search_json = json.loads(search_content)
        start_number=0




        for novel_number in range(len(search_json['books'])):
            print u'序号：'+str(novel_number+1)
            print u'书名：'+json.dumps(search_json['books'][int(novel_number)]['title'],ensure_ascii=False,indent=2)
            print u'作者：'+json.dumps(search_json['books'][int(novel_number)]['author'],ensure_ascii=False,indent=2)
            if novel_number-start_number == 8:break
            print
        selcet_number=int(raw_input('请选择需要推送的小说序号:'))



    def get_chapterlist(self):
        '''
6        通过小说ID，获取小说章节页的url
        '''
        pass

    def get_content(self):
        '''
        使用爬虫，将小说各章节内容爬下来
        '''

novel1 = Novel()
novel1.get_novelid()
novel1.get_chapterlist()
novel1.get_content()
