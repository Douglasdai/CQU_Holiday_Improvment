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
    # print(len(list_temp))
dict_temp= dict(list_temp)
input_file.close()

class WeatherForecast:  # 调用url,request函数访问网站
    def __init__(self):
        self.headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US;rv:1.9pre)Gecko/2019100821 Minefield/3.0.2pre'}  # 创建头，伪装成服务器/浏览器访问远程的web服务器
        self.cityCode = dict_temp # 查找的城市
    def forecastCity(self,city):
        if city not in self.cityCode.keys():
            print(city+'code cannot be found')
            return

        url = 'http://www.weather.com.cn/weather/'+self.cityCode[city]+'.shtml'  # 创建成url
        fp = open ("D:\CQU_work_hard\CQU_Holiday_Improvment\code-improve\DSC\exz.txt", "a", encoding="utf-8")
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
                   data = li.select('h1')[0].text  # h1的第一个元素的text文本
                   weather = li.select("p[class='wea']")[0].text
                   temp = li.findAll('span')[0].text + '/' + li.findAll('i')[0].text
                   print(city,data)
                   fp.write(city)
                   fp.write(' ')
                   fp.write(data)
                   fp.write(weather)
                   fp.write(temp)
                   fp.write('\n')
                    # 插入到数据库的记录
                except Exception as err:
                    print(err)
            
        except Exception as err:
            print(err)



ws = WeatherForecast()
for i in dict_temp.keys():
    ws.forecastCity(i)
print('completed')