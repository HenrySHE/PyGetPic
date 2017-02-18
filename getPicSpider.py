# -*- coding:utf-8 -*-
# Edit by Henry
# 2017-2-17 Fri

import urllib
import urllib2
import re


class Spider:
    def __init__(self):
        self.siteURL = 'http://www.socwall.com/wallpapers/page:2'
        #self.siteURL = 'http://www.socwall.com/'
        #self.siteURL = 'https://mm.taobao.com/json/request_top_list.htm?page=2'
    def getPage(self,pageNum):
        # url = self.siteURL + "/page=" + str(pageIndex)
        print pageNum
        url = self.siteURL
        print 'The url you input is: ', url
        #User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36
        HDs = {
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
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
        print 'Page content is: ',page
        #pattern = re.compile(r'src="(.*?)"', re.S|re.M)
        #pattern = re.compile('<img style="width: 290px; height: 260px;" src="/images/wallpapers/(.*?)">',re.S)
        #items = re.findall(pattern, page)

        #res_url = r'src="(.*?)"'
        res_url = r'<li class="wallpaper wallpaper.*?<img style="width: 290px; height: 260px;" src="(.*?)".*?</a>'
        items = re.findall(res_url,page,re.S)

        print '-------------------------Start-----------------------'
        for item in items:
            #print item[0], item[1], item[2], item[3], item[4]
            print item
        print '-------------------------End-----------------------'
            #print u'The image address is:' + item[0]


spider = Spider()
spider.getContents(1)
