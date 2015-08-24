# -*- coding:utf-8 -*-
import urllib2
import re


class novel_txt():
    '''
    获取所有章节的url并存入txt
    '''

    def get_searchkey(self):
        pass







    def get_urlcontent(self,url):
        try:
            request = urllib2.Request(url)#读取网页
            response = urllib2.urlopen(request)
            content = response.read().decode('utf-8','ignore')
            return  content
        except urllib2.HTTPError, e:
            print e.code
        except urllib2.URLError, e:
            print e.reason

    def get_booklist(self,search_content):
        pattern = re.compile('href="/w/novel/(.*?)/0.*?> (.*?)</a.*?searchAuthor/(.*?)_0_1.*?class="lastchapter">(.*?)</div>',re.S)
        #正则捕获，id，标题，作者，最新章节
        results = re.findall(pattern,search_content)#获取全部匹配项目
        number = 1
        bookid = [] #初始化小说list
        for item in results:
            bookid.append(str(item[0]))
            print str(number)+'\n'+item[1]+'\n'+item[2]+'\n'+item[3]+'\n'
            number += 1
        #print bookid  #测试小说list
        selcet_booknumber=int(raw_input('请选择需要推送的小说序号:'))-1
        return bookid[int(selcet_booknumber)]


    def get_book_catalog_url_list(self,select_bookid):
        '''
        :param select_bookid: 手动输入的小说序号
        :return:返回小说目录页的所有页list
        '''
        book_url_0='http://book.easou.com/w/novel/'+str(select_bookid)+'/0.html' #目录页面（不完整）
        book_url_0_content=self.get_urlcontent(book_url_0)
        pattern = re.compile(u'<span class="category"><a href="(.*?)/1_0\.html">\u67e5\u770b\u76ee\u5f55<',re.S)
        # 正则捕获完整目录页的网址
        result = re.findall(pattern,book_url_0_content)#获取完整目录页的网址
        book_catalog_start_url='http://book.easou.com'+str(result[0])+'/1_0.html'
        # 目录页面（完整）的第一页，可能有多页目录页，一页目录页有999章节
        book_catalog_start_url_content = self.get_urlcontent(book_catalog_start_url)
        pages = 2
        while 1:
            pattern = re.compile(str(pages)+'_0',re.S) #正则寻找页号url后缀
            page_result = re.search(pattern,book_catalog_start_url_content)#获取全部匹配项目
            if page_result:
                # print 'found page: '+str(pages)
                pages+=1
            else:
                print 'have '+str(pages-1)
                break
        book_catalog_end_url='http://book.easou.com'+str(result[0])+'/'+str(pages-1)+'_0.html'#目录页面最后页
        book_catalog_url_list=[]
        for page in range(1,pages):
            book_catalog_url_list.append('http://book.easou.com'+str(result[0])+'/'+str(page)+'_0.html')
        print book_catalog_url_list # 测试目录url_list
        return book_catalog_url_list


    def get_chapter_number(self,book_catalog_url_list):
        '''
        para：输入最终页面
        return:总章节数
        '''
        self.book_catalog_end_url_content = self.get_urlcontent(book_catalog_url_list[-1])
        for i in range((self.pages_number-1)*999+1,self.pages_number*999):
            pattern = re.compile('/'+str(i)+'\.html">(.*?)\.',re.S)
            result = re.search(pattern,self.book_catalog_end_url_content) # 是否有第i个章节
            if result:
                pass
                # print 'found NO.'+str(i) # 输出寻找过程
            else:
                break
        return i-1

    def get_chapter_list(self,chapter_number,):
        '''
        :para :book_chapter_number:
        :return:
        '''
        bookid_2_pattern = re.compile('<li><span><a class="common" href="/w/read/(.*?)/'+str((self.pages_number-1)*999+1)+'.html">'+str((self.pages_number-1)*999+1),re.S)
        bookid_2_result = re.search(bookid_2_pattern,self.book_catalog_end_url_content)
        if bookid_2_result:
            print bookid_2_result.group(1)

        book_chapter_list=[]
        for item in range (1,chapter_number+1):
            book_chapter_list.append('http://book.easou.com/w/read/'+str(bookid_2_result.group(1))+'/'+str(item)+'.html')
        return book_chapter_list


    def store_in_txt(self,chapter_url_list):
        '''
        :para:所有章节的url_list
        :return:将所有章节存入一个txt中
        '''
        chapter_content=self.get_urlcontent(chapter_url_list[0])
        print chapter_content
        pattern = re.compile('line-height(.*?) <div class="footerbar">',re.S)
        result = re.search(pattern,chapter_content)
        if result:
            print result.group(1)
        else:
            print 'none'
        # for i in chapter_url_list:
        #     print i


    def main(self):
        self.searchkey='斗破苍穹'   #搜索内容
        self.searchurl='http://book.easou.com/w/searchNovel/'+self.searchkey+'_0_1.html'  #搜索结果页
        self.search_content = self.get_urlcontent(self.searchurl)   #获取小说搜索页url内容
        self.select_bookid=self.get_booklist(self.search_content)   #获取小说搜索页小说字段，并打印
        print self.select_bookid #print 选择的小说id
        self.book_catalog_url_list = self.get_book_catalog_url_list(self.select_bookid) #获取小说目录页的url
        self.pages_number = len(self.book_catalog_url_list)
        self.chapter_number = self.get_chapter_number(self.book_catalog_url_list)
        print self.chapter_number
        chapter_url_list = self.get_chapter_list(self.chapter_number)
        self.store_in_txt(chapter_url_list)
        # print chapter_url_list[-1] #　测试打印最后章节的url






novel = novel_txt()
novel.main()