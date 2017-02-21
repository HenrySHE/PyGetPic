# -*- coding:utf-8 -*-
# Edit by Henry
# First Edited 2017-2-17 Fri
# Second Edited 2017-2-19 Sun
# Third Edited 2017-2-21 Tue

import urllib2
import re
import MySQLdb
import requests


class Spider:
    def __init__(self):
        self.siteURL = 'http://www.socwall.com/wallpapers/page:'
        self.request_url = 'https://api-cn.faceplusplus.com/imagepp/beta/detectsceneandobject'
        self.APIkey = ''
        self.APISecret = ''

    def getPage(self, pageNum):
        # url = self.siteURL + "/page=" + str(pageIndex)
        url = self.siteURL + pageNum
        print 'pageNum:', pageNum
        print 'The url you input is: ', url
        # Act as a browser
        hds = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
        }
        request = urllib2.Request(url, headers=hds)
        # response = urllib2.urlopen(request)
        # return response.read().decode('gbk')
        try:
            response = urllib2.urlopen(request)
        except urllib2.URLError, e:
            # Get the reason and exit
            print e.code
            print e.reason
            exit()
        return response.read().decode('gbk')
        # return response.read()

    def getContents(self, pageNum):
        page = self.getPage(pageNum)
        # print 'Page content is: ',page
        # pattern = re.compile(r'src="(.*?)"', re.S|re.M)
        # pattern = re.compile('<img style="width: 290px; height: 260px;" src="/images/wallpapers/(.*?)">',re.S)
        # items = re.findall(pattern, page)
        # res_url = r'src="(.*?)"'
        res_url = r'<li class="wallpaper wallpaper.*?' \
                  r'<img style="width: 290px; height: 260px;" src="/images/wallpapers/(.*?)".*?</a>'
        items = re.findall(res_url, page, re.S)

        print '-------------------------Start-----------------------'
        contents = []
        for item in items:
            # print item[0], item[1], item[2], item[3], item[4]
            print 'The short url is: ', item
            contents.append(item)
            # print contents
        print '--------------------------End------------------------'
        return contents

    # This function is used to get the whole result lists
    def get_whole_url(self,contents):
        result_list = []
        for url in contents:
            real_url = 'http://www.socwall.com/images/wallpapers/' + url
            print 'Getting the Whole URL list:',real_url
            result_list.append(real_url)
        return result_list

    def insert_info(self, contents):
        db = MySQLdb.connect("localhost", "root", "", "fyp")
        cursor = db.cursor()
        num = 0
        print '===============Connecting Database==================='
        for url in contents:
            # INSERT INTO `information` (`id`, `Image_FileName`, `Image_FilePath`) VALUES (NULL, 'http://s.visitbeijing.com.cn/uploadfile/2015/1127/20151127051010253.jpg', '20151127051010253.jpg');
            # sql = "INSERT INTO `info` (`id`, `url`, `tag`) VALUES (NULL, '" + url + "', 'TempTag');"
            # /images/wallpapers/73875-290x260.jpg
            real_url = 'http://www.socwall.com/images/wallpapers/' + url
            print 'The real_url is : ',real_url
            sql = "INSERT INTO `information` " \
                  "(`id`, `Image_FileName`, `Image_FilePath`) VALUES (NULL, '" \
                  + real_url \
                  + "', '" \
                  + url + "');"
            try:
                cursor.execute(sql)
                db.commit()
                print 'No.%s URL INSERT SUCCESSFUL!' % num
                num = num + 1
            except:
                # Rollback in case there is any error
                db.rollback()
                print 'SORRY,INSERT FAILED...'
                # 关闭数据库连接
        db.close()
        print '===============Database Closed==================='
        print 'All job is finished, please check your Database!'


    def print_fpp(self,contents):
        #print 'Analyzing the url:',contents
        temp = 0
        while temp <= (len(contents)-1):
            data = {
                'api_key':self.APIkey,
                'api_secret':self.APISecret,
                # http://s.visitbeijing.com.cn/uploadfile/2015/1127/20151127051010253.jpg
                # 'image_url':'http://www.tianqi.com/upload/article/15-06-10/XzKG_150610052612_1.jpg'
                # This URL is a picture of panda (with some text on it)
                # 'image_url':'http://s.visitbeijing.com.cn/uploadfile/2015/1127/20151127051010253.jpg'
                'image_url': contents[temp]
            }
            r = requests.post(self.request_url,data)
            print '\n','The receive content type is:',r.headers['content-type']
            # r.encoding
            # -----------This code is used to print the JSON file in text format
            print 'The whole JSON content is:',r.text,
            # testType = 'objects',
            # testType = 'scenes'
            self.show_json('objects',r,contents[temp])
            self.show_json('scenes',r,contents[temp])
            temp = temp + 1

    def show_json(self,testType,r,single_url):
        print 'From now on the single_url address is:', single_url
        print '\n==================  Test %s Start=====================' % testType
        # -----------This is used to show all the JSON in Dictionary type
        # print r.json()
        # print r.json()["time_used"].encode('utf-8')
        print 'List length is :', len(r.json()[testType])
        length = len(r.json()[testType])
        db = MySQLdb.connect("localhost", "root", "", "fyp")
        cursor = db.cursor()
        if length > 0:
            print 'It has some %s in this picture!' % testType, '\n'
            temp_length = length - 1
            tamale = 0
            while (tamale <= temp_length):
                # INSERT INTO `indexing` (`Tag_ID`, `Image_ID`, `Tag`, `ClickTimes`, `SuggestClickTimes`) VALUES (NULL, 'http://s.visitbeijing.com.cn/uploadfile/2015/1127/20151127051010253.jpg', 'panda', '5', '5');
                print 'The No.%s key word is:' % tamale, r.json()[testType][tamale]["value"]
                print 'The No.%s key word confidence is' % tamale, r.json()[testType][tamale]["confidence"], '%', '\n'
                sql = "INSERT INTO `indexing` (`Tag_ID`, `Image_ID`, `Tag`, `ClickTimes`, `SuggestClickTimes`) VALUES (NULL, '"+ single_url +"', '" + r.json()[testType][tamale]["value"]  + "', '" + '6' + "', '0');"
                try:
                    cursor.execute(sql)
                    db.commit()
                    print 'TAG %s INSERT SUCCESSFUL!'%r.json()[testType][tamale]["value"]
                except:
                    # Rollback in case there is any error
                    db.rollback()
                    print 'SORRY,INSERT FAILED...'
                    # 关闭数据库连接
                tamale = tamale + 1
        else:
            print 'This picture might not belongs to %s type' % testType
        db.close()
        print '=====================End of Test %s========================' % testType


# -----------------Test the whole process of printing out the results---------------
pageNum = raw_input("Hello! Please input the Page Number :")
print 'The page number you have input is: ', pageNum
spider = Spider()
pic_contents = spider.getContents(pageNum)
#print pic_contents
# ----------------Test Successful FULL URL
# print spider.get_whole_url(pic_contents)
#whole_url = spider.get_whole_url(pic_contents)
#print whole_url
url_url = [r'http://www.socwall.com/images/wallpapers/73875-290x260.jpg',r'http://www.socwall.com/images/wallpapers/73874-290x260.jpg']
spider.print_fpp(url_url)

# spider.insert_info(Pic_contents)


# --------------------------------Test face++ function-------------------------------
# spider = Spider()
# url = 'http://www.baidu.com'
# spider.print_fpp(url)

# ----------------------Test saving url into fyp, information able-------------------

