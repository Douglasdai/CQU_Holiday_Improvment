# # 爬取所有城市几天的 天气情况
# from bs4 import BeautifulSoup
# from bs4 import UnicodeDammit  # BS 内置库，猜测文档编码
# import urllib.request

# input_file = open("D:\\city.txt","r",encoding= "utf-8")
# infile_content =input_file.readlines()
#     #定义空列表储存临时数据，将同一组数据存储在同一列表中
# list_temp = []
# for each in infile_content:
#     list_temp.append(each.split())
#     # print(list_temp)
#     # print(len(list_temp))
# dict_temp= dict(list_temp)
# input_file.close()

# class WeatherForecast:  # 调用url,request函数访问网站
#     def __init__(self):
#         self.headers = {'User-Agent':'Mozilla/5.0 (Windows; U; Windows NT 6.0 x64; en-US;rv:1.9pre)Gecko/2019100821 Minefield/3.0.2pre'}  # 创建头，伪装成服务器/浏览器访问远程的web服务器
#         self.cityCode = dict_temp # 查找的城市
#     def forecastCity(self,city):
#         if city not in self.cityCode.keys():
#             print(city+'code cannot be found')
#             return
#         url = 'http://www.weather.com.cn/weather/'+self.cityCode[city]+'.shtml'  # 创建成url
#         fp = open ("D:\\CQU_work_hard\\CQU_Holiday_Improvment\\code-improve\\DSC\\exz.txt", "a", encoding="utf-8")
#         try:
#             req = urllib.request.Request(url,headers=self.headers) # 访问地址
#             data = urllib.request.urlopen(req)
#             data = data.read()
#             dammit = UnicodeDammit(data,['utf-8'],'gbk')
#             data = dammit.unicode_markup
#             soup = BeautifulSoup(data,'lxml')
#             lis = soup.select("ul[class='t clearfix'] li")  # 找到每一个天气数据
#             fp.write('\n'+city+' ')            
#             for li in lis:                
#                 try:
#                    data = li.select('h1')[0].text  # h1的第一个元素的text文本
#                    weather = li.select("p[class='wea']")[0].text
#                    temp = li.findAll('span')[0].text + '/' + li.findAll('i')[0].text
#                    print(city,data)
#                    fp.write(data+' ')                   
#                    fp.write(weather+' ')                   
#                    fp.write(temp+' ')               
#                     # 插入到数据库的记录                 
#                 except Exception as err:
#                     print(err)            
#         except Exception as err:
#             print(err)

# # 数据处理
# def alter(file,old_str,new_str):
#     """
#     替换文件中的字符串
#     :param file:文件名
#     :param old_str:就字符串
#     :param new_str:新字符串
#     :return:
#     """
#     file_data = ""
#     with open(file, "r", encoding="utf-8") as f:
#         for line in f:
#             if old_str in line:
#                 line = line.replace(old_str,new_str)
#             file_data += line
#     with open(file,"w",encoding="utf-8") as f:
#         f.write(file_data)

# ws = WeatherForecast()
# for i in dict_temp.keys():
#     ws.forecastCity(i)
# print('completed')
# alter("D:\\CQU_work_hard\\CQU_Holiday_Improvment\\code-improve\\DSC\\exz.txt", "/", " ")
# alter("D:\\CQU_work_hard\\CQU_Holiday_Improvment\\code-improve\\DSC\\exz.txt", "℃ ", " ")

#交互查询并做图
import matplotlib.pyplot as plot 
import numpy as np
# #负号显示问题
plot.rcParams['axes.unicode_minus'] = False
# #中文显示问题
plot.rcParams['font.sans-serif'] = ['SimHei']
#第一天实时气温
# def searchfile(file):
#     data_file = open(file,"r",encoding= "utf-8")
#     data_content =data_file.readlines()
# #     #定义空列表储存临时数据，将同一组数据存储在同一列表中
#     data_temp = []
#     for each in data_content:
#         data_temp.append(each.split())

#     data_dict = dict()
#     n=1
#     while n <len(data_temp)-1:
#         data_dict[data_temp[n][0]]=data_temp[n]
#         n+=1

#     c = input("你要查询的城市： ")
#     out_form = data_dict[c]
#     print(out_form[0]+' '+out_form[1]+' '+out_form[2]+' 气温为：'+out_form[3])
#     x=[]
#     y1=[]
#     y2=[]

#     m=4
#     while m <len(out_form):
#         str1=out_form[m]+out_form[m+1]    
#         x.append(str1)
#         y1.append(int(out_form[m+2]))
#         y2.append(int(out_form[m+3]))
#         m+=4
#     plot.plot(x,y1,y2,linewidth= 2)
#     plot.title(out_form[0],fontsize = 12)
#     plot.xlabel('date',fontsize = 10)
#     plot.ylabel('temp',fontsize= 12)
#     plot.show()


#第一天有最低最高气温
def searchfile2(file):
    # #负号显示问题
    plot.rcParams['axes.unicode_minus'] = False
    # #中文显示问题
    plot.rcParams['font.sans-serif'] = ['SimHei']
    data_file = open(file,"r",encoding= "utf-8")
    data_content =data_file.readlines()
#     #定义空列表储存临时数据，将同一组数据存储在同一列表中
    data_temp = []
    for each in data_content:
        data_temp.append(each.split())

    data_dict = dict()
    n=1
    while n <len(data_temp)-1:
        data_dict[data_temp[n][0]]=data_temp[n]
        n+=1

    c = input("你要查询的城市： ")
    #异常处理
    out_form = data_dict[c]
    print(out_form[0]+' '+out_form[1]+' '+out_form[2]+' 最高气温为：'+out_form[3]+'最低气温为：'+out_form[4])
    x=[]
    y1=[]
    y2=[]

    m=1
    while m <len(out_form):
        str1=out_form[m]+out_form[m+1]    
        x.append(str1)
        y1.append(int(out_form[m+2]))
        y2.append(int(out_form[m+3]))
        m+=4
    plot.figure(figsize=(12,6))
    plot.plot(x,y1,'ro-',linewidth = 2)
    plot.plot(x,y2,'bo-',linewidth = 2)
    plot.title(out_form[0],fontsize = 12)
    plot.xlabel('date',fontsize = 12)
    plot.ylabel('temp',fontsize= 12)
    plot.show()
   
# searchfile2("D:\\CQU_work_hard\\CQU_Holiday_Improvment\\code-improve\\DSC\\exz.txt") 
   



# 作图
# # #函数
# # def printSheet():
# out_form = data_dict[c]
# print(out_form[0]+' '+out_form[1]+' '+out_form[2]+'气温为：'+out_form[3])
# x=[]
# y1=[]
# y2=[]
# m=4
# while m <len(out_form):
#     str1=out_form[m]+out_form[m+1]    
#     x.append(str1)
#     y1.append(int(out_form[m+2]))
#     y2.append(int(out_form[m+3]))
#     m+=4
# plot.plot(x,y1,y2,linewidth= 2)
# plot.title(out_form[0],fontsize = 12)
# plot.xlabel('date',fontsize = 10)
# plot.ylabel('temp',fontsize= 12)
# plot.show()








