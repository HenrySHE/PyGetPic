PyGetPic
====
Created by  **Henry SHE** :bowtie:

Python Getting :computer: &amp; Saving Pics :rice_scene:
## 暂定最终版（2017年4月22日）
1. 加入WordNet，允许用户在现有的tag的基础上去添加同义词Tag

Final Version:
Join WordNet, allowing users to add synonyms Tag based on the existing tag

----------------
## 更新版本（2017年4月20日）

### 更新功能
1. 允许用户输入页码，自动插入数据库+加Tag 
2. 允许用户查看/修改/删除 指定的Tag（根据用户输入Tag ID ）

Updated Feature:
1. Allow users to enter the page number, automatically insert the database + Tag
2. Allow users to view / modify / delete the specified Tag (based on user input Tag ID)

### 運行流程：
自動加Tag：首先用戶先輸入Page Number（即壁紙網站的頁碼），然後將對應頁碼下的圖片全部存入information的表格裏；
若是URL已經存在Database，Shell裏面告知操作者已經存在Database，若是還沒存在，會告訴操作者Tag已經自動添加進入數據庫。
查看、修改、刪除Tag，用戶輸入Tag ID，然後查看，刪除對應的Tag，或者修改Tag 裏面的內容。

Running process:
- Tag automatically: First, the user first enter the Page Number (page number of the wallpaper website), and then all the pictures under the page number stored in the information table;
- If the URL already exists Database, Shell which tells the operator already exists Database, if it does not exist, will tell the operator Tag has been automatically added to the database.
- View, modify, delete Tag, the user input Tag ID, and then view, delete the corresponding Tag, or modify the contents of the Tag.

----------------

## 交接JSP Project版本（2017年2月27日）

### 1.功能：
1. 適配之前的FYP Project；
2. 存入indexing表的image id是通過search來匹配實現，使得JSP project在搜索圖片的時候可以返回圖片結果；
3. 兩張表，在插入數據的時候（存圖片URL、加Tag）的時候，可以實現查重（提前查看數據庫是否已經存在已知Tag），避免搜索詞語的時候返重複的結果

1. Fit into the former FYP project
2  Using image id to match the searching process, making the JSP project in the search for pictures can return the picture results;
3. Add two tables, insert the data (save the image URL, add Tag), you can check (in advance to see if the database already exists known Tag), to avoid the search results when the return duplicate results.

### 2.運行截圖：

**搜索通過py文件存儲的tag的結果&返回的圖片**
> 搜索"pond"返回的結果，這兩張圖片都是通過爬蟲爬取的圖片，然後tag也是通過爬蟲添加的。(Retrieve the result returned by "pond", both of which are pictures crawled by the crawler, and the tag is also added by the crawler.)

![](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-27_1.png)

**Image id 測試**
> 因為存入搜索tag的時候是通過image id去match到information表格中的URL，所以我需要先獲取到image id。測試成功結果：(Because into the search tag by image id to match to the URL in the information table, so I need to get to the image id. Test successful results:)

![](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-27_3.png)

**存入數據庫成功截圖**

Saving data sucessfully screenshot:

![](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-27_4.png)

**Information & Indexing 查重複成功截圖**

![](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-27_information%E6%9F%A5%E9%87%8D%E6%88%90%E5%8A%9F%E6%88%AA%E5%9B%BE.png)

![](https://github.com/HenrySHE/PyGetPic/blob/master/ScreenShots/2017-2-27_tag%E6%A3%80%E9%AA%8C%E6%88%90%E5%8A%9F.png)


## 整合Face++圖片識別到project 版本（2017年2月21日）

### 1.主要的更新

1. 更改url獲取方式，改成直接獲取xxx.jpg的格式
2. 添加方法：`def get_whole_url(self,contents)`，用戶可以通過調用這個方法獲取完整的url
3. 添加方法：`def insert_info(self, contents)`,用戶可以將獲取的URL List存儲到'fyp'下面的'Information'的表格中。
4. 添加方法：`def print_fpp(),show_json(self,testType,r,single_url)`,用來將URL List發送到Face++分析Tag,然後存儲到'fyp'下'indexing'的表格里面
5. 上傳fyp表格（還未測試前的表格）

### 2.即將實現的功能

1. 通過分析Confidence去存儲positive feedback(初始的ClickTimes)


### 3.測試Face++ 文字識別模塊

今天測試了一下Face++ 的識別圖片中的文字模塊，決定棄用。原因如下：
* 精確度好像不太夠（~~可能是我測試的圖片的問題?~~）
* 我測試的第一張圖片是“3D Text"結果識別的結果是“3DT”
* 第二張測試的是寫著“TEXT”的圖片，全部大寫，但是識別結果是“EX”
* Picture Size:圖片的大小限定在800*800以內的png或者jpg文件，小了點。

### 4.測試成功的截圖

**For循環寫入Tag進入數據庫結果**


![](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-21_for_loop_Analyzing.png)

**将URL,文件名写入'Information'表**


![](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-21_%E6%95%B0%E6%8D%AE%E6%8F%92%E5%85%A5%E6%88%90%E5%8A%9F%E4%BB%A3%E7%A0%81.png)

**将URL,Tag写入'Indexing'表**


![](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-21_%E5%86%99%E5%85%A5%E6%95%B0%E6%8D%AE%E5%BA%93%E6%88%90%E5%8A%9F.png)

## 测试Face++成功（2017年2月20日）
**测试功能**
- 输入一个图片URL，可以通过Face++得出近似的object或者Scene

*代码因为涉及到api key所以暂时不放上来，等整合到程序里面开始使用，我会更改掉key然后push上来*


**測試的圖片：**

![測試圖片](http://s.visitbeijing.com.cn/uploadfile/2015/1127/20151127051010253.jpg)

**運行的結果:**

![Results](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/run_fpp_results.png)

## 版本更新（2017年2月19日）
**更新功能：**
- 讓用戶輸入Page Num
- 把獲取的URL補充成完整的URL
- 寫入測試的本地Database

**測試成功截圖：**

![Running Code](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-19_RunCode.png)

**數據庫寫入截圖：**

![Running Code](https://raw.githubusercontent.com/HenrySHE/PyGetPic/master/ScreenShots/2017-2-19_DB.png)

## 暫時測試成功的demo版本(2017年2月17日)
**功能：**
- 訪問圖片網站

- 獲取網站主頁.jpg的文件名
