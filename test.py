#coding=utf-8
import requests
import re


chapter_url='http://read.qidian.com/BookReader/2094528,34366302.aspx'
pattern = re.compile('http://read.qidian.com/BookReader/(.*?)\.aspx',re.S)
result = re.findall(pattern,chapter_url)
# print result[0]
chapterID = result[0].replace(',','/')
#　print chapterID
chapter_text_url = 'http://files.qidian.com/Author1/'+str(chapterID)+'.txt'
chapter_text_html = requests.get(chapter_text_url)
chapter_text_html.encoding='gbk'#重新解码为gbk

print chapter_text_html.text

