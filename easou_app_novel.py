# coding=utf-8
import requests
import json
import re
'''
下面三行可以解决大部分编码问题
'''
import sys
reload(sys)
sys.setdefaultencoding( "utf-8" )


class novel:
    def __init__(self):
        self.name=''
        self.gid=''
        self.nid=''
        self.chapter_list=[]

    def set_novel(self,name,gid,nid):
        self.name = unicode(name)
        self.gid = unicode(gid)
        self.nid =unicode(nid)

    def get_chapter(self):
        url = 'http://api.easou.com/api/bookapp/chapter_list.m?gid='+self.gid+'&nid='+self.nid+'&page_id=1&size=9999&cid=eef_'
        jsondata = requests.get(url).content
        # print jsondata
        jsonval = json.loads(jsondata)
        number = 0
        for val in jsonval['items']:
            chapter = val['chapter_name']
            # print chapter #test 输出全部章节名
            self.chapter_list.append(chapter) #章节名导入list
        # for i in self.chapter_list:
        #     print i #输出章节列表

    def get_chapter_content(self):
        giddata = ''
        niddata = ''
        chapter_name_data = ''
        sortdata = ''
        sequencedata = ''
        number = 0
        for select_chapter in self.chapter_list:
            number +=1
            giddata = giddata + str(self.gid) + '!@'
            niddata = niddata + str(self.nid) + '!@'
            chapter_name_data = chapter_name_data+unicode(select_chapter) + '!@'
            sortdata = sortdata + str(number) + '!@'
            sequencedata = sequencedata + str(number-1) + '!@'
            if number % 10 == 0:
                # print giddata ,'\n', niddata ,'\n', chapter_name_data,'\n',sortdata,'\n',sequencedata #输出多个变量的值
                self.postdata4downlaod(giddata,niddata,chapter_name_data,sortdata,sequencedata)
                giddata = ''
                niddata = ''
                chapter_name_data = ''
                sortdata = ''
                sequencedata = ''
            else:pass
        self.postdata4downlaod(giddata,niddata,chapter_name_data,sortdata,sequencedata)


    def postdata4downlaod(self,giddata,niddata,chapter_name_data,sortdata,sequencedata):
        # data = ('gid=2861249!@2861249!@2861249!@2861249!@2861249!@2861249!@2861249!@2861249!@2861249!@2861249&nid=14289062!@14289062!@14289062!@14289062!@14289062!@14289062!@14289062!@14289062!@14289062!@14289062&sort=81!@82!@83!@84!@85!@86!@87!@88!@89!@90&gsort=0!@0!@0!@0!@0!@0!@0!@0!@0!@0&chapter_name=耍流氓!@老牛吃嫩草（上）!@老牛吃嫩草（下）!@蛇打七寸!@小冤家!@你是我的!@情哥哥!@美羊羊和灰太狼!@小乖宝!@军训&sequence=80!@81!@82!@83!@84!@85!@86!@87!@88!@89')
        data = str('gid='+giddata[:-2:]+'&nid='+niddata[:-2:]+'&sort='+sortdata[:-2:]+'&gsort=0!@0!@0!@0!@0!@0!@0!@0!@0!@0&chapter_name='+chapter_name_data[:-2:]+'&sequence='+sequencedata[:-2:])
        # print data,'\n'
        headers = {'Content-Type':'application/x-www-form-urlencoded', 'Accept-Encoding': 'gzip'} #定义post的头信息
        url ='http://api.easou.com/api/bookapp/batch_chapter.m?cid=eef_&version=002&os=ios&udid=76fbeddf8b73c8b0fc065e2296b767579d8fda38&appverion=1018&ch=bnf1349_10388_001'
        jsondata = requests.post(url=url, data=data, headers=headers).content #字节方式的响应体，会自动为你解码 gzip 和 deflate 压缩
        # print jsondata,'\n','\n'
        jsonval = json.loads(jsondata)

        list_number = 0
        for val in jsonval['items']:
            novelfile=open('download_novel\\'+self.name+'.txt','a')
            list_number += 1
            chapter = val['chapter_name']
            content = val['content']
            novelfile.write(chapter)
            novelfile.write('\n\n')
            novelfile.write(content)
            novelfile.write('\n\n')
            print ('正在下载第', list_number ,'章')
            novelfile.close()




def search_novel():
    status = 0
    while status == 0:
        keyword = raw_input('请输入小说关键字：')
        page = '1'
        url = 'http://api.easou.com/api/bookapp/search.m?word='+keyword+'&page_id='+page+'&count=20&cid=eef_'
        result = requests.get(url).content
        # print result # test获取搜索页
        if 'guess_like_items":[]' in result :
            status = 1
            jsonval = json.loads(result) #用内置json库，读取json数据
            number = 1
            for val in jsonval['items']:
                print '序号：', number
                number +=1
                print '书名：', val['name']
                print '作者：', val['author'] ,'\n'
        else:
            print '找不到该小说，请重新搜索'
        while status == 1 :
            setnumber = raw_input('请输入需要推送的小说序号（输入0重新搜索）：')
            if setnumber == '0':
                status = 0
                break
            else:
                try:
                    # print jsonval['items'][int(setnumber)-1]['name'] #test 打印所选的小说名
                    gid = jsonval['items'][int(setnumber)-1]['gid']
                    nid = jsonval['items'][int(setnumber)-1]['nid']
                    name = jsonval['items'][int(setnumber)-1]['name']
                    return name,gid,nid
                except IndexError and ValueError:
                    print '输入序号有误，请重新输入'









(name,gid,nid)=search_novel()
print name, gid, nid # test 返回所选小说信息
Novel = novel()
Novel.set_novel(name=name,gid=gid,nid=nid)
Novel.get_chapter()
Novel.get_chapter_content()





