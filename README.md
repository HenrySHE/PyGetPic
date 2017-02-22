PyGetPic
====
Created by  **Henry SHE** :bowtie:

Python Getting :computer: &amp; Saving Pics :rice_scene:

## 整合Face++图片识别到project 版本（2017年2月21日）

### 1.主要的更新

1. 更改url获取方式，改成直接获取xxx.jpg的格式
2. 添加方法：`def get_whole_url(self,contents)`，用户可以通过调用这个方法获取完整的url
3. 添加方法：`def insert_info(self, contents)`,用户可以将获取的URL List存储到'fyp'下面的'Information'的表格中。
4. 添加方法：`def print_fpp(),show_json(self,testType,r,single_url)`,用来将URL List发送到Face++分析Tag,然后存储到'fyp'下'indexing'的表格里面
5. 上传fyp表格（还未测试前的表格）

### 2.即将实现的功能

1. 通过分析Confidence去存储positive feedback(初始的ClickTimes)


### 3.测试Face++ 文字识别模块

今天测试了一下Face++ 的识别图片中的文字模块，决定弃用。原因如下：
* 精确度好像不太够（~~可能是我测试的图片的问题?~~）
	* 我测试的第一张图片是“3D Text"结果识别的结果是“3DT”
	* 第二张测试的是写着“TEXT”的图片，全部大写，但是识别结果是“EX”
* Picture Size:图片的大小限定在800*800以内的png或者jpg文件，小了点。

### 4.测试成功的截图

**For循环写入Tag进入数据库结果**


![](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-21_for_loop_Analyzing.png)

**将URL,文件名写入'Information'表**


![](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-21_%E6%95%B0%E6%8D%AE%E6%8F%92%E5%85%A5%E6%88%90%E5%8A%9F%E4%BB%A3%E7%A0%81.png)

**将URL,Tag写入'Indexing'表**


![](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-21_%E5%86%99%E5%85%A5%E6%95%B0%E6%8D%AE%E5%BA%93%E6%88%90%E5%8A%9F.png)

## 测试Face++成功（2017年2月20日）
**测试功能**
- 输入一个图片URL，可以通过Face++得出近似的object或者Scene

*代码因为涉及到api key所以暂时不放上来，等整合到程序里面开始使用，我会更改掉key然后push上来*


**测试的图片：**

![测试图片](http://s.visitbeijing.com.cn/uploadfile/2015/1127/20151127051010253.jpg)

**运行的结果:**

![Results](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/run_fpp_results.png)

## 版本更新（2017年2月19日）
**更新功能：**
- 让用户输入Page Num
- 把获取的URL补充成完整的URL
- 写入测试的本地Database

**测试成功截图：**

![Running Code](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-19_RunCode.png)

**数据库写入截图：**

![Running Code](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-19_DB.png)

## 暂时测试成功的demo版本(2017年2月17日)
**功能：**
- 访问图片网站

- 获取网站主页.jpg的文件名
