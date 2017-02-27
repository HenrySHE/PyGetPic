# -*- coding:utf-8 -*-
# Edit by Henry


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
                  + url \
                  + "', '" \
                  + real_url + "');"
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
        i = 0
        string_url = ''
        while i <= (len(contents)-1):
            data = {
                'api_key':self.APIkey,
                'api_secret':self.APISecret,
                # http://s.visitbeijing.com.cn/uploadfile/2015/1127/20151127051010253.jpg
                # 'image_url':'http://www.tianqi.com/upload/article/15-06-10/XzKG_150610052612_1.jpg'
                # This URL is a picture of panda (with some text on it)
                # 'image_url':'http://s.visitbeijing.com.cn/uploadfile/2015/1127/20151127051010253.jpg'
                'image_url': contents[i]
            }
            r = requests.post(self.request_url,data)
            string_url = contents[i]

            print '\n','The receive content type is:',r.headers['content-type']
            # r.encoding
            # -----------This code is used to print the JSON file in text format
            print 'The whole JSON content is:',r.text,
            # testType = 'objects',
            # testType = 'scenes'
            self.show_json('objects',r,string_url)
            self.show_json('scenes',r,string_url)
            i += 1

    def show_json(self,testType,r,single_url):
        print 'From now on the single_url address is:', single_url

        id = (str)(self.get_image_id(single_url))
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
                print 'The No.%s key word is:' % (tamale + 1), r.json()[testType][tamale]["value"]
                print 'The No.%s key word confidence is' % (tamale + 1), r.json()[testType][tamale]["confidence"], '%', '\n'
                sql = "INSERT INTO `indexing` (`Tag_ID`, `Image_ID`, `Tag`, `ClickTimes`, `SuggestClickTimes`) VALUES (NULL, '"+ id +"', '" + r.json()[testType][tamale]["value"]  + "', '" + '6' + "', '0');"
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

    def get_image_id(self, single_url):
        db2 = MySQLdb.connect("localhost", "root", "", "fyp")
        cursor = db2.cursor()
        # SELECT `id` FROM `information` WHERE `Image_FilePath` = 'http://www.socwall.com/images/wallpapers/73875-290x260.jpg'
        sql2 = "SELECT `id` FROM `information` WHERE `Image_FilePath` = '" + single_url + "'"
        image_id = ''
        results = 0
        try:
            cursor.execute(sql2)
            results = cursor.fetchone()[0]
        except:
            db2.rollback()
            print 'SORRY,can not match any image id...'
        db2.close()
        print 'The image id is:', results
        return results

# -----------------Test the whole process of printing out the results---------------
spider = Spider()
# pageNum = raw_input("Hello! Please input the Page Number :")
# print 'The page number you have input is: ', pageNum
#pic_contents = spider.getContents(pageNum)
#print pic_contents
# ----------------Test Successful FULL URL
# print spider.get_whole_url(pic_contents)
#whole_url = spider.get_whole_url(pic_contents)
#print whole_url

url_url = [r'http://www.socwall.com/images/wallpapers/73788-290x260.jpg',r'http://www.socwall.com/images/wallpapers/73784-290x260.jpg']
url_url = [r'http://www.socwall.com/images/wallpapers/73719-290x260.jpg',r'http://www.socwall.com/images/wallpapers/73718-290x260.jpg']
spider.print_fpp(url_url)

# testimageid = 'http://www.socwall.com/images/wallpapers/73788-290x260.jpg'
# print spider.get_image_id(testimageid)
# spider.insert_info(Pic_contents)


# --------------------------------Test face++ function-------------------------------
# spider = Spider()
# url = 'http://www.baidu.com'
# spider.print_fpp(url)

# ----------------------Test saving url into fyp, information able-------------------

