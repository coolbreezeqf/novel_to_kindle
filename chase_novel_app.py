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
        self.keyword='斗破苍穹'
        self.chapterlist =[]
        pass




    def get_novelid(self):
        '''
        以命令行形式获取输入关键字,返回小说ID
        '''
        novellist_url='http://api.zhuishushenqi.com/book/fuzzy-search?query=斗破苍穹'
        # novellist_url=unicode(novellist_url,'utf-8') #修改编码模式
        search_content=requests.get(novellist_url)
        # print search_content
        print search_content.json()






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
