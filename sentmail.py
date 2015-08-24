# -*- coding: UTF-8 -*-
#coding=utf-8
import smtplib
import email.mime.text
import email.mime.multipart
import email.Encoders
import email.MIMEBase
import os.path

class Sendemail():
    '''
    发送邮件模块
    '''
    def __init__(self,username,password,usersmtp,fromwhere,towhere,title):
        #初始化邮件头属性
        self.username=username
        self.password=password
        self.usersmtp=usersmtp
        self.msg = email.mime.multipart.MIMEMultipart()
        self.msg['from']=fromwhere      #发件邮箱
        self.msg['to']=towhere       #收件邮箱
        self.msg['subject']=title   #设置邮件标题

    def set_emailbody(self,content):
        self.body = email.mime.text.MIMEText(content,_subtype='plain',_charset='gb2312')   #设置邮件正文
        self.msg.attach(self.body)

    def set_attachfile(self,):
    #遍历sendlist文件夹，将其中内容作为附件
        for parent,dirnames,filenames in os.walk('sendlist'):
            for i in range(len(filenames)):
                print 'send '+filenames[i]
                self.part = email.MIMEBase.MIMEBase('application', 'octet-stream')
                self.part.set_payload(open(parent+'\\'+filenames[i],'rb').read()) #同级目录下文件，也可使用绝对路径
                email.Encoders.encode_base64(self.part)
                self.part.add_header('Content-Disposition', 'attachment',filename=filenames[i])#修改附件头
                self.msg.attach(self.part)

    def sendemail(self):#发送邮件
        try:
            s = smtplib.SMTP()
            s.connect(self.usersmtp)
            s.login(self.username,self.password)#XXX为用户名，XXXXX为密码
            s.sendmail(self.msg['from'], self.msg['to'],self.msg.as_string())
            s.quit()
            print 'success'
        except Exception, e:
            print 'faild \n'+str(e)


if __name__ == '__main__':
    test = Sendemail('13901619126','yang0311','smtp.163.com','13901619126@163.com','475785388@qq.com','hello,class')
    test.set_emailbody('yes i can')
    test.set_attachfile()
    test.sendemail()
