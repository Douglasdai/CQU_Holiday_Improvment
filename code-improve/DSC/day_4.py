#今天的代码基本都是抄的，爬虫相关完全不会，先借鉴别人代码，而后自己写
#正则表达式
# var str = "http://www.runoob.com:80/html/html-tutorial.html";
# var patt1 = /(\w+):\/\/([^/:]+)(:\d*)?([^# ]*)/;
# arr = str.match(patt1);
# for (var i = 0; i < arr.length ; i++) {
#     document.write(arr[i]);
#     document.write("<br>");
# }te(str1.match(patt1));
#爬虫
#request用法
# import urllib.parse
# import urllib.request
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())

#爬取某城市几天的 天气情况
from bs4 import BeautifulSoup
from bs4 import UnicodeDammit  # BS 内置库，猜测文档编码
import urllib.request

input_file = open("D:\\city.txt","r",encoding= "utf-8")
infile_content =input_file.readlines()
    #定义空列表储存临时数据，将同一组数据存储在同一列表中
list_temp = []
for each in infile_content:
    list_temp.append(each.split())
    # print(list_temp)
    #print(len(list_temp))
print(list_temp)
# print(len(dict_temp))
input_file.close()

# url = 'http://www.weather.com.cn/weather/101010100.shtml'
# try:
#     headers = {'User-Agent':'Mozilla/5.0(Windows;U;Windows NT 6.0 x64;en-US;rv:1.9pre)Gecko/20191008 Minefield/3.0.2pre'}  
#     req = urllib.request.Request(url,headers = headers)
#     data = urllib.request.urlopen(req)
#     data = data.read()
#     dammint = UnicodeDammit(data,['utf-8','gbk']) #鉴别编码，做一个包装-markup
#     data = dammint.unicode_markup
#     soup = BeautifulSoup(data,'lxml')
#     lis = soup.select("ul[class='t clearfix'] li") # 找到ul下的所有li
#     fp = open ("D:\CQU_work_hard\CQU_Holiday_Improvment\code-improve\DSC\exz.txt", "a", encoding="utf-8")
#     for li in lis:
#         try:
#             data = li.select('h1')[0].text  # h1的第一个元素的text文本
#             weather = li.select("p[class='wea']")[0].text
#             temp = li.findAll('span')[0].text + '/' + li.findAll('i')[0].text
#             print(data,weather,temp)
#             fp.write(data)
#             fp.write(weather)
#             fp.write(temp)
#             fp.write('\n')
#         except Exception as err:
#                 print(err)
# except Exception as err:
#     print(err)
# fp.close()


#输入数据函数
# def input_dict(infile):
#     input_file = open(infile,"r",encoding= "utf-8")
#     infile_content  =input_file.readlines()
#     #定义空列表储存临时数据，将同一组数据存储在同一列表中
#     list_temp = []
#     for each in infile_content:
#         list_temp.append(each.split())
#         # print(list_temp)
#         #print(len(list_temp))
#     dict_temp = dict(list_temp)
#     # print(dict_temp)
#     # print(len(dict_temp))
#     input_file.close()

# if __name__ == "__main__":
#     input_dict("D:\\city.txt")


#目前不知道怎么 进行数据库的处理
#爬取几个城市的天气情况
# from bs4 import BeautifulSoup
# from bs4 import UnicodeDammit
# import urllib.request
import sqlite3

class WeatherDB:  # 包含对数据库的操作
    def openDB(self):
        self.con = sqlite3.connect('weathers.db')
        self.cursor = self.con.cursor()
        try:
            self.cursor.execute('create table weathers (wCity varchar(16),wDate varchar(16),wWeather varchar(64),wTemp varchar(32),constraint pk_weather primary key(wCity,wDate))')
            # 爬取城市的天气预报数据储存到数据库weather.db中
        except:  # 第一次创建表格是成功的；第二次创建就会清空表格
            self.cursor.execute('delete from weathers')
    def closeDB(self):
        self.con.commit()
        self.con.close()

    def insert(self,city,date,weather,temp):
        try:
            self.cursor.execute('insert into weather (wCity,wDate,wTemp)values(?,?,?,?)',(city,date,weather,temp))
        except Exception as err:
            print(err)
    def show(self):
        self.cursor.execute('select * from weathers')
        rows = self.cursor.fetchall()
        print('%-16s%-16s%-32s%-16s'%('city','date','weather','temp'))
        for row in rows:
            print('%-16s%-16s%-32s%-16s'%(row[0],row[1],row[2],row[3]))

class WeatherForecast:  # 调用url,request函数访问网站
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US;rv:1.9pre)Gecko/2019100821 Minefield/3.0.2pre'}  # 创建头，伪装成服务器/浏览器访问远程的web服务器
        self.cityCode = {'北京':'101010100','上海':'101020100','广州':'101280101','深圳':'101280601','新竹':'101340103'} # 查找的城市
    def forecastCity(self,city):
        if city not in self.cityCode.keys():
            print(city+'code cannot be found')
            return

        url = 'http://www.weather.com.cn/weather/'+self.cityCode[city]+'.shtml'  # 创建成url
        try:
            req = urllib.request.Request(url,headers=self.headers) # 访问地址
            data = urllib.request.urlopen(req)
            data = data.read()
            dammit = UnicodeDammit(data,['utf-8'],'gbk')
            data = dammit.unicode_markup
            soup = BeautifulSoup(data,'lxml')
            lis = soup.select("ul[class='t clearfix'] li")  # 找到每一个天气数据
            for li in lis:
                try:
                    date = li.select('h1')[0].text
                    weather = li.select('p[class="wea"]')[0].text
                    temp = li.select('p[class="tem"] span')[0].text+'/'+li.select('p[class="tem"] i')[0].text
                    print(city,date,weather,temp)
                    self.db.insert(city,date,weather,temp) # 插入到数据库的记录
                except Exception as err:
                    print(err)
        except Exception as err:
            print(err)

    def process(self,cities):
        self.db = WeatherDB()
        self.db.openDB()
        for city in cities:
            self.forecastCity(city)  # 循环每一个城市
        self.db.closeDB()

ws = WeatherForecast()
ws.process(['北京','上海','广州','深圳','新竹'])
print('completed')

#获取cookie
# import http.cookiejar,urllib.request
# filename ='cookie.txt'
# cookie = http.cookiejar.MozillaCookieJar(filename)
# # cookie = http.cookiejar.CookieJar()
# handler = urllib.request.HTTPCookieProcessor(cookie)
# opener = urllib.request.build_opener(handler)
# response = opener.open('http://www.baidu.com')
# for item in cookie:
#     print(item.name+ ' ='+item.value)

# cookie.save(ignore_discard = True,ignore_expires = True)
#用user -agent 伪装
# from urllib import request,parse
# url = 'http://httpbin.org/post'
# headers = {
#     #伪装一个火狐浏览器
#     'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)',"host":'httpbin.org'
# }
# dict = {
#     'name':'Germey'
# }
# data = bytes(parse.urlencode(dict),encoding='utf8')
# req = request.Request(url=url,data=data,headers=headers,method='POST')
# response = request.urlopen(req)
# print(response.read().decode('utf-8'))


#网上案例 - 爬取豆瓣250电影
# import re

# import requests
# from bs4 import BeautifulSoup

# def get_content(url,):
#     try:
#         User_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebkit/537.36(KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
#         response = requests.get(url, headers = {'Users-Agent':User_agent})
#         response.raise_for_status()
#         response.encoding = response.apparent_encoding
#     except Exception as e:
#         print (" 爬取错误")
#     else:
        
# import re
# import requests
# from bs4 import BeautifulSoup

# def get_content(url,):
#     try:
#         user_agent = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.109 Safari/537.36"
#         response = requests.get(url,  headers={'User-Agent': user_agent})
#         response.raise_for_status()   # 如果返回的状态码不是200， 则抛出异常;
#         response.encoding = response.apparent_encoding  # 判断网页的编码格式， 便于respons.text知道如何解码;
#     except Exception as e:
#         print("爬取错误")
#     else:

#         print(response.url)
#         print("爬取成功!")
#         return  response.content

# def parser_content(htmlContent):
#     # 实例化soup对象， 便于处理；
#     soup = BeautifulSoup(htmlContent, 'html.parser')
#     #  1). 电影信息存储在ol标签里面的li标签:
#     #  <ol class="grid_view">
#     olObj = soup.find_all('ol', class_='grid_view')[0]

#     #  2). 获取每个电影的详细信息, 存储在li标签;
#     details = olObj.find_all('li')


#     for detail in details:
#         # #  3). 获取电影名称;
#         movieName = detail.find('span', class_='title').get_text()

#         # 4). 电影评分：
#         movieScore = detail.find('span', class_='rating_num').get_text()

#         # 5). 评价人数***************
#         # 必须要转换类型为字符串
#         movieCommentNum = str(detail.find(text=re.compile('\d+人评价')))
#         # 6). 电影短评
#         movieCommentObj = detail.find('span', class_='inq')
#         if movieCommentObj:
#             movieComment = movieCommentObj.get_text()
#         else:
#             movieComment = "无短评"

#         movieInfo.append((movieName, movieScore, movieCommentNum, movieComment))

# import openpyxl


# def create_to_excel(wbname, data, sheetname='Sheet1', ):
#     """
#     将制定的信息保存到新建的excel表格中;

#     :param wbname:
#     :param data: 往excel中存储的数据;
#     :param sheetname:
#     :return:
#     """

#     print("正在创建excel表格%s......" % (wbname))

#     # wb = openpyxl.load_workbook(wbname)
#     #  如果文件不存在， 自己实例化一个WorkBook的对象;
#     wb = openpyxl.Workbook()
#     # 获取当前活动工作表的对象
#     sheet = wb.active
#     # 修改工作表的名称
#     sheet.title = sheetname
#     # 将数据data写入excel表格中;
#     print("正在写入数据........")
#     for row, item in enumerate(data):  # data发现有4行数据， item里面有三列数据;
#         print(item)
#         for column, cellValue in enumerate(item):

#             # cell = sheet.cell(row=row + 1, column=column + 1, value=cellValue)
#             cell = sheet.cell(row=row+1, column=column + 1)
#             cell.value = cellValue

#     wb.save(wbname)
#     print("保存工作薄%s成功......." % (wbname))


# if __name__ == '__main__':
#     doubanTopPage = 10
#     perPage = 25
#     # [(), (), ()]
#     movieInfo = []
#     # 1, 2, 3 ,4, 5
#     for page in range(1, doubanTopPage+1):
#         # start的值= (当前页-1)*每页显示的数量(25)
#         url = "https://movie.douban.com/top250?start=%s" %((page-1)*perPage)
#         content = get_content(url)
#         parser_content(content)


## create_to_excel('D:\CQU_work_hard\CQU_Holiday_Improvment\code-improve\DSC\hello.xlsx', movieInfo, sheetname="豆瓣电影信息")