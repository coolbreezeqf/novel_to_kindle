# -*- coding:utf-8 -*-
#coding:utf-8
__author__ = 'cheng'

import urllib2
import json
import re
import requests
import lxml.html
from lxml import etree

class Novel():
    def __init__(self):
        '''
        初始化内部共享变量
        '''
        self.keyword='斗破苍穹'
        self.chapter_url_list = []
        self.chapter_title_list =[]



    def show_searchresult(self,start_number,search_json,):
        if start_number < len(search_json['books']):
            for novel_number in range(start_number,len(search_json['books'])):
                print u'序号：'+str(novel_number+1)
                print u'书名：'+json.dumps(search_json['books'][int(novel_number)]['title'],ensure_ascii=False,indent=2)
                print u'作者：'+json.dumps(search_json['books'][int(novel_number)]['author'],ensure_ascii=False,indent=2)
                print u'简介：'+json.dumps(search_json['books'][int(novel_number)]['shortIntro'],ensure_ascii=False,indent=2)
                print
                if novel_number-start_number == 9:
                    break
        else:
            print '请输入 - 返回上一页'



    def get_novelID(self):
        '''
        以命令行形式获取输入关键字,返回小ID
        '''
        novellist_url='http://api.zhuishushenqi.com/book/fuzzy-search?query='+str(self.keyword)
        # novellist_url=unicode(novellist_url,'utf-8') #修改编码模式
        search_html=requests.get(novellist_url).text #获取搜索页内容
        # print search_content #测试获取网页内容
        search_json = json.loads(search_html)
        start_number = 0
        self.show_searchresult(start_number,search_json)
        select_number=int(raw_input('请选择需要推送的小说序号(输入 + ，显示下一页,输入 - ，显示上一页):'))
        while True:
            if select_number in range(1,11):
                self.novelID = search_json['books'][select_number-1]['_id']
                self.novel_name = search_json['books'][select_number-1]['title']
                print self.novelID
                print self.novel_name
                break
            elif select_number == 0 or -1:
                if select_number == 0:
                    start_number += 10
                elif select_number == -1:
                    start_number -= 10
                self.show_searchresult(start_number,search_json)
                select_number=int(raw_input('请选择需要推送的小说序号(输入 + ，显示下一页,输入 - ，显示上一页):'))


    def get_chapterlist(self):
        '''
        通过小ID，获取小说章节的list
        '''
        chapterlist_url = 'http://api.zhuishushenqi.com/mix-toc/'+self.novelID
        chapterlist_json = requests.get(chapterlist_url).json()
        self.get_chapter_text('http://read.qidian.com/BookReader/2094528,34305712.aspx')


        # print len(chapterlist_json['mixToc']['chapters']) #测试总章节数
        # for chapter_number in range(len(chapterlist_json['mixToc']['chapters'])):
        '''
        循环打开各章节url
        '''
        #     chapter_title = chapterlist_json['mixToc']['chapters'][int(chapter_number)]['title']
        #     chapter_url =  chapterlist_json['mixToc']['chapters'][int(chapter_number)]['link']
        #     self.chapter_title_list.append(chapter_title)
        #     self.chapter_url_list.append(chapter_url)
        #     self.get_chapter_content(chapter_url)
        #     f=open('chapter_url_list.txt','w')
        #     f.write(str(self.chapter_url_list))
        #     f.close()
        #     f=open('chapter_titile_list.txt','w')
        #     f.write(str(self.chapter_url_list))
        #     f.close()


    def get_chapter_text(self,chapter_url):
        '''
        使用爬虫，将小说各章节内容爬下来
        '''
        if 'http://read.qidian.com/' in chapter_url:#遇到起点网站的抓取方式
            pattern = re.compile('http://read.qidian.com/BookReader/(.*?)\.aspx',re.S)
            result = re.findall(pattern,chapter_url)
            print result
            chapterID = result[0].replace(',','/')
            #　print chapterID
            chapter_text_url = 'http://files.qidian.com/Author1/'+str(chapterID)+'.txt'
            chapter_text_html = requests.get(chapter_text_url)
            chapter_text_html.encoding='gbk'#编码为gbk
            #对正文进行修补
            chapter_text = chapter_text_html.text
            chapter_text =chapter_text.replace("document.write('",' ',1)
            chapter_text =chapter_text.replace("<p>",'\n')
            print chapter_text
            # f = open('1.txt','w')
            # f.write(str(chapter_text))
            # f.close()



if __name__ == '__main__':
    novel1 = Novel()
    novel1.get_novelID()
    novel1.get_chapterlist()

