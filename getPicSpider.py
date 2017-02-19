# -*- coding:utf-8 -*-
# Edit by Henry
# First Edited 2017-2-17 Fri
# Second Edited 2017-2-19 Sun 21:06

import urllib
import urllib2
import re
import MySQLdb


class Spider:
    def __init__(self):
        self.siteURL = 'http://www.socwall.com/wallpapers/page:'
    def getPage(self,pageNum):
        # url = self.siteURL + "/page=" + str(pageIndex)
        url = self.siteURL+pageNum
        print 'pageNum:', pageNum
        print 'The url you input is: ', url
        #Act as a browser
        HDs = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
            #-----------This rest of the data is unnecessary---------------
            # 'Accept - Encoding':' gzip, deflate, sdch',
            # 'Accept - Language':'en - US, en;q = 0.8',
            # 'Connection':'keep - alive',
            # 'Host':'ping.chartbeat.net',
            # 'Referer':'http://www.socwall.com/wallpapers/page:1/'
        }
        request = urllib2.Request(url,headers= HDs)
        # response = urllib2.urlopen(request)
        # return response.read().decode('gbk')
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError, e:
            #Get the reason and exit
            print e.code
            print e.reason
            exit()
        return response.read().decode('gbk')
        # return response.read()


    def getContents(self,pageNum):
        page = self.getPage(pageNum)
        #print 'Page content is: ',page
        #pattern = re.compile(r'src="(.*?)"', re.S|re.M)
        #pattern = re.compile('<img style="width: 290px; height: 260px;" src="/images/wallpapers/(.*?)">',re.S)
        #items = re.findall(pattern, page)

        #res_url = r'src="(.*?)"'
        res_url = r'<li class="wallpaper wallpaper.*?<img style="width: 290px; height: 260px;" src="(.*?)".*?</a>'
        items = re.findall(res_url,page,re.S)

        print '-------------------------Start-----------------------'
        contents = []
        for item in items:
            #print item[0], item[1], item[2], item[3], item[4]
            item = 'http://www.socwall.com/'+item
            print 'the real URL is :',item
            contents.append(item)
            #print contents
        print '--------------------------End------------------------'
        return contents

    def Insert(self,contents):
        db = MySQLdb.connect("localhost","root","","pythonsql" )
        cursor = db.cursor()
        num = 0
        for url in contents:
            sql = "INSERT INTO `info` (`id`, `url`, `tag`) VALUES (NULL, '" + url + "', 'TempTag');"
            try:
                cursor.execute(sql)
                db.commit()
                print 'No.%s URL INSERT SUCCESSFUL!'%num
                num=num+1
            except:
                # Rollback in case there is any error
                db.rollback()
                print 'SORRY,INSERT FAILED...'
            # 关闭数据库连接
        db.close()
        print 'All job is finished, please check your Database!'


pageNum = raw_input("Hello! Please input the Page Number :")
print 'The page number you have input is: ',pageNum
spider = Spider()
Pic_contents = spider.getContents(pageNum)
#print Pic_contents
spider.Insert(Pic_contents)

