# -*- coding:utf-8 -*-
# Edit by Henry

import urllib2
import re
import MySQLdb
import requests
import time
from nltk.corpus import wordnet


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
        contents = []
        for item in items:
            # print item[0], item[1], item[2], item[3], item[4]
            # print 'The short url is: ', item
            contents.append(item)
            # print contents
        return contents

    # This function is used to get the whole result lists
    def get_whole_url(self,contents):
        result_list = []
        print 'The image url are:'
        for url in contents:
            real_url = 'http://www.socwall.com/images/wallpapers/' + url
            # print 'Getting the Whole URL list:',real_url
            print real_url
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
            # print 'The real_url is : ',real_url
            sql = "INSERT INTO `information` " \
                  "(`id`, `Image_FileName`, `Image_FilePath`) VALUES (NULL, '" \
                  + url \
                  + "', '" \
                  + real_url + "');"
            # --------------Test if the record exist-------------------
            sql2 = "SELECT `id` FROM `information` WHERE `Image_FilePath` = '" + real_url + "'"
            try:
                cursor.execute(sql2)
                row_count = cursor.rowcount
                # print 'The row count is :', row_count
                if row_count == 0:
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
                else:
                    print 'Images already exist, no need to insert.'
                    continue
            except:
                # Rollback in case there is any error
                db.rollback()
                print 'SORRY,INSERT FAILED...'
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

            # print '\n','The receive content type is:',r.headers['content-type']
            # r.encoding
            # -----------This code is used to print the JSON file in text format

            # print 'The whole JSON content is:',r.text,
            print "========================================================="
            print 'From now on the single_url address is:', string_url
            print 'And the image id is:', (str)(self.get_image_id(string_url))
            self.show_json('objects',r,string_url)
            self.show_json('scenes',r,string_url)
            i += 1
        print "========================================================="

    def show_json(self, testType, r, single_url):
        # print 'From now on the single_url address is:', single_url
        id = (str)(self.get_image_id(single_url))
        print '\n-----[Start of Testing %s]------' % testType
        # -----------This is used to show all the JSON in Dictionary type
        # print r.json()
        # print r.json()["time_used"].encode('utf-8')
        # print 'List length is :', len(r.json()[testType])
        length = len(r.json()[testType])
        db = MySQLdb.connect("localhost", "root", "", "fyp")
        cursor = db.cursor()
        if length > 0:
            # print '<---It has some %s in this picture!' % testType
            temp_length = length - 1
            tamale = 0
            while (tamale <= temp_length):
                # INSERT INTO `indexing` (`Tag_ID`, `Image_ID`, `Tag`, `ClickTimes`, `SuggestClickTimes`) VALUES (NULL, 'http://s.visitbeijing.com.cn/uploadfile/2015/1127/20151127051010253.jpg', 'panda', '5', '5');
                print 'The No.%s key word is:' % (tamale + 1), r.json()[testType][tamale]["value"]
                syns = wordnet.synsets((tamale + 1), r.json()[testType][tamale]["value"])
                print 'The Explanation of this word is :'%syns[0].definition()
                print 'The No.%s key word confidence is' % (tamale + 1), r.json()[testType][tamale][
                    "confidence"], '%'
                sql = "INSERT INTO `indexing` (`Tag_ID`, `Image_ID`, `Tag`, `ClickTimes`, `SuggestClickTimes`) VALUES (NULL, '" + id + "', '" + \
                      r.json()[testType][tamale]["value"] + "', '" + '6' + "', '0');"
                sql2 = "SELECT `Tag_ID` FROM `indexing` WHERE `Image_ID` = '" + id + "' AND `Tag` = '" + \
                       r.json()[testType][tamale]["value"] + "'"
                try:
                    cursor.execute(sql2)
                    row_count = cursor.rowcount
                    if row_count == 0:
                        try:
                            cursor.execute(sql)
                            db.commit()
                            print '>>>TAG <<<%s>>> INSERT SUCCESSFUL!' % r.json()[testType][tamale]["value"]
                            tamale = tamale + 1
                        except:
                            # Rollback in case there is any error
                            db.rollback()
                            print 'SORRY,INSERT FAILED...'
                            # 关闭数据库连接
                    else:
                        print ">>>This tag has already exist in the database!"
                        tamale = tamale + 1
                        continue
                except:
                    # Rollback in case there is any error
                    db.rollback()
                    print "SORRY,CONNECTION FAILED..."

        else:
            print 'This picture might not belongs to %s type' % testType
        db.close()
        print '-----[End of Testing %s]------\n' % testType

    def calc_confidence(self,value):
        # temp = temp_val[testType][tamale]["confidence"]
        # click_times = self.calc_confidence(int(float(temp)))
        # print 'Click Times is:____________________>>>>>',click_times
        # str(click_times)
        if value >= 50:
            click_times = 5 + int(value/5)
        elif value < 20:
            click_times = 5 + int(value/10)
        else:
            click_times = 5 + int(value/8)
        return click_times


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
        # print 'The image id is:', results
        return results

    def operate_tag(self,choice,tag_id):
        db = MySQLdb.connect("localhost", "root", "", "fyp")
        cursor = db.cursor()
        # 1. Viewing Tag through tag id
        if choice == '1':
            sql = "SELECT * FROM `indexing` WHERE `Tag_ID` =" + tag_id
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    Tag_ID = row[0]
                    Image_ID = row[1]
                    Tag = row[2]
                    ClickTimes = row[3]
                    SuggestClickTimes = row[4]
                    print "-----Tag_ID = %d, Image_ID = %s, Tag = %s, ClickTimes = %d, SuggestClickTimes = %d" % \
                          (Tag_ID, Image_ID, Tag, ClickTimes, SuggestClickTimes)
            except:
                print "-----Error: unable to get data"
            db.close()
        elif choice == '2':
            sql = "DELETE FROM `indexing` WHERE `indexing`.`Tag_ID` ="+tag_id
            try:
                cursor.execute(sql)
                db.commit()
                print '-----The tag was deleted'
            except:
                db.rollback()
                print '-----Sorry delete failed.'
            db.close()
        elif choice == '3':
            new_tag = raw_input('-----Please input new tag:')
            sql = "UPDATE `indexing` SET `Tag` = '" + new_tag + "' WHERE `indexing`.`Tag_ID` =" + tag_id
            try:
                cursor.execute(sql)
                db.commit()
                print '-----The tag was Updated'
            except:
                db.rollback()
                print '-----Sorry update failed.'
            db.close()
        elif choice == '4':
            # sql = "SELECT `Tag` FROM `indexing` WHERE `Tag_ID` =" + tag_id
            sql = "SELECT * FROM `indexing` WHERE `Tag_ID` =" + tag_id
            try:
                cursor.execute(sql)
                results = cursor.fetchall()
                for row in results:
                    tid = row[0]
                    iid = row[1]
                    tag = row[2]

                # print tag
                syns = wordnet.synsets(tag)
                print '-----The <<tag>> is:',tag
                print '-----The <<image id>> is:',iid
                print '-----The <<definition>> is:',syns[0].definition()
                print '==================='
                i = 0
                while (i < len(syns)):
                    print 'No.', i + 1, ': ',syns[i].lemmas()[0].name()
                    i = i + 1
                print '==================='
                j = int(raw_input('-----Please input a tag you want to add(0 return to menu):'))
                if j == 0:
                    return
                else:
                    sql2 = "INSERT INTO `indexing` (`Tag_ID`, `Image_ID`, `Tag`, `ClickTimes`, `SuggestClickTimes`) " \
                           "VALUES (NULL, '"  + iid + "', '" + syns[j-1].lemmas()[0].name() + "', '6', '0');"
                    try:
                        cursor.execute(sql2)
                        db.commit()
                        print '-----Data has been inserted.'
                    except:
                        db.rollback()
                    db.close()
            except:
                print "-----Error: unable to get data"
                db.close()
        else:
            db.close()
            print '-----Wrong input! Please input correct answer'


    def main(self):
        print '----------------------------------'
        print 'Welcome! What did you want to do?'
        print '----------------------------------'
        print '1. Crawling Picture from the Wall paper website.'
        print '2. Add Synonyms/View/Edit/Delete Tag from the database.'
        print '0. Exit'
        choice = raw_input("Please input your choice:")
        if choice == '1':
            print 'Your Choice is 1'
            pageNum = raw_input("Please input the Page Number :")
            print 'The page number you have input is: ', pageNum
            print '-------------------------Start-----------------------'
            pic_contents = self.getContents(pageNum)
            self.insert_info(pic_contents)
            # print pic_contents
            whole_url = self.get_whole_url(pic_contents)
            print 'Biding them into a list: ',whole_url
            # test_url = [r'http://www.socwall.com/images/wallpapers/75178-290x260.jpg'
            #     ,r'http://www.socwall.com/images/wallpapers/75177-290x260.jpg']
            self.print_fpp(whole_url)
            print '--------------------------End------------------------'
            self.main()
        elif choice == '2':
            print 'Your Choice is 2'
            print '-----Please choose operations:'
            print '-----1.Viewing Tag through tag id'
            print '-----2.Deleting Tag through tag id'
            print '-----3.Editing Tag through tag id'
            print '-----4.Add Synonyms Tags Through tag id'
            choice2 = raw_input('-----Your choice is:')
            tag_id = raw_input('-----Please input tag id:')
            self.operate_tag(choice2,tag_id)
            print '-----Returning to Main Menu...'
            time.sleep(3)
            self.main()

        elif choice == '0':
            exit()
        else:
            print 'Wrong Input! Please try again.'
            return self.main()


# -----------------Test the whole process of printing out the results---------------
spider = Spider()
# pageNum = raw_input("Hello! Please input the Page Number :")
# print 'The page number you have input is: ', pageNum
#pic_contents = spider.getContents(pageNum)
#print pic_contents

# ----------------测试完整url(success)--------------
# print spider.get_whole_url(pic_contents)
#whole_url = spider.get_whole_url(pic_contents)
#print whole_url

#-----------------测试写入indexing Tag的时候是否能匹配到image id (success)-----------
# url_url = [r'http://www.socwall.com/images/wallpapers/73788-290x260.jpg',r'http://www.socwall.com/images/wallpapers/73784-290x260.jpg']
# url_url = [r'http://www.socwall.com/images/wallpapers/73719-290x260.jpg',r'http://www.socwall.com/images/wallpapers/73718-290x260.jpg']
# spider.print_fpp(url_url)

# testimageid = 'http://www.socwall.com/images/wallpapers/73788-290x260.jpg'
# print spider.get_image_id(testimageid)
# spider.insert_info(Pic_contents)

# --------------------------------Test face++ function-------------------------------
# spider = Spider()
# url = 'http://www.baidu.com'
# spider.print_fpp(url)
# ----------------------Test inserting duplicate data into 'information' table (success)-------------------
# dup_url = [r'73788-290x260.jpg']
# spider.insert_info(dup_url)

spider.main()


