#程序正常运行需要在同文件夹下加入一个“data.csv”文件，内容请参考链接： 城市代码
#需要用到csv文件 不会搞，先注释
# import sys
# import re
# import requests
# import webbrowser
# from PIL import Image
# from requests.exceptions import RequestException
# import csv
# data={}
# with open("data.csv",'r',encoding='ISO-8859-1') as f:
#     rawinfos=list(csv.reader(f))
#     for i in rawinfos:
#         data[i[0]]=i[1]
# def get_one_page(url,headers):
#     try:
#         response=requests.get(url,headers=headers)
#         if response.status_code==200:
#             response.encoding='utf-8'
#             return response.text
#         return None
#     except RequestException:
#         return None
# headers={'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/604.4.7 (KHTML, like Gecko) Version/11.0.2 Safari/604.4.7'}
# try:
#     address=data[sys.argv[1]]
# except:
#     sys.exit("\033[31m无该城市！\033[0m")
# html=get_one_page('http://www.weather.com.cn/weather1d/'+address+'.shtml',headers)
# if not html:
#     print("城市代码有误！")
#     exit(1)
# ADDRESS=re.findall('<title>(.*?)</title>',html)
# aim=re.findall('<input type="hidden" id="hidden_title" value="(.*?)月(.*?)日(.*?)时(.*?) (.*?)  (.*?)  (.*?)"',html,re.S)
# airdata=re.findall('<li class="li6 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>',html,re.S)
# print(ADDRESS[0][1:5])
# print("当前日期：%s月%s日,%s"%(aim[0][0],aim[0][1],aim[0][4]))
# print("更新时间：%s:00"%aim[0][2])
# print("当前天气：%s"%aim[0][5])
# print("今日温度：%s"%aim[0][6])
# print("空气质量："+airdata[0][0]+","+airdata[0][2])
# ask_ok=input("是否深入查看（Y/N）：")
# if ask_ok=='Y' or ask_ok=='y':
#     lightdata=re.findall('<li class="li1 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>',html,re.S)
#     colddata=re.findall('<li class="li2 hot">\n(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>',html,re.S)
#     weardata=re.findall('<li class="li3 hot" id="chuanyi">\n(.*?)<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>',html,re.S)
#     washdata=re.findall('<li class="li4 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>',html,re.S)
#     bloodata=re.findall('<li class="li5 hot">\n<i></i>\n<span>(.*?)</span>\n<em>(.*?)</em>\n<p>(.*?)</p>\n</li>',html,re.S)
#     detail = re.findall('hour3data={"1d":(.*?),"23d"', html, re.S)
#     detail = re.findall('"(.*?)"', detail[0], re.S)
#     print("--"*40)
#     print('详细数据：')
#     print("%-10s\t%-10s\t%-10s\t%-10s\t%-10s"%("时间","状态","温度","风向","风力"))
#     for each in detail:
#         each=each.split(',')
#         print("%-10s\t%-10s\t%-10s\t%-10s\t%-10s"%(each[0],each[2],each[3],each[4],each[5]))
#     print("--"*40)
#     print("%s:\t%s\t%s"%(lightdata[0][1],lightdata[0][0],lightdata[0][2]))
#     print("%s:\t%s"%(colddata[0][1],colddata[0][2]))
#     print("%s:\t%s\t%s"%(washdata[0][1],washdata[0][0],washdata[0][2]))
#     print("血糖指数:\t%s,%s"%(bloodata[0][0],bloodata[0][2]))
#     print("%s:\t%s\t%s"%(weardata[0][2],weardata[0][1],weardata[0][3]))
#     print("--"*40)
#     flag=input("是否查看详细穿衣建议（Y/N）：")
#     if flag=='Y' or flag=='y':
#         webbrowser.open("http://www.weather.com.cn/forecast/ct.shtml?areaid="+address)
# print("数据来源：中央气象台")


# import requests
# from bs4 import BeautifulSoup

# # 浏览器代{过}{滤}理
# headers = {
#     "user-agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.87 Safari/537.36"
# }


# # 获取该url地址下的源码
# def get_url(url):
#     data = requests.get(url, headers=headers).content.decode("utf-8")
#     # 使用html5lib 容错率较高
#     soup = BeautifulSoup(data, "html5lib")
#     return soup


# # 通过网页源码匹配该地区的七天天气的html源码
# def gain_data(soup):
#     hanmls = soup.find("div", class_="hanml")
#     # 匹配到存放所有天数温度的div标签下的数据
#     conmidtabs = hanmls.find_all("div", class_="conMidtab")
#     return conmidtabs


# # 通过网页源码匹配是哪七天
# def gain_day():
#     url = "http://www.weather.com.cn/textFC/hb.shtml"
#     soup = get_url(url)
#     day = []
#     days = list(soup.find("ul", class_="day_tabs").stripped_strings)
#     for Current in days:
#         day.append(Current)
#     return day


# # 获取每天的数据
# def gain_table(conmidtab):
#     tabs = conmidtab.find_all("table")
#     # 用来存放遍历的数据
#     y = {}
#     # 遍历当天该地区的所有城市
#     for tab in tabs:
#         # 因为前两个是表头 所以从第三个获取每个省的城市的名字和温度
#         trs = tab.find_all("tr")[2:]
#         for tr in trs:
#             # 提取城市name
#             citys = list(tr.find("td", width="83").stripped_strings)[0]
#             # 提取城市min_tmparetrue
#             tmps = list(tr.find("td", width="86").stripped_strings)[0]
#             # 把城市名作为key，温度作为value
#             y[citys] = int(tmps)
#             # 把字典y中的数据存放到该数组中
#     return y


# # 把数据到本地
# def write_file(regions, lis1_index):
#     lis1 = ["华北", "东北", "华东", "华中", "华南", "西北", "西南", "港澳台"]
#     with open("D:\CQU_work_hard\CQU_Holiday_Improvment\code-improve\DSC\weather1.txt", "a", encoding="utf-8") as fp:
#         # 把日期写到最前面
#         fp.write(("地区：" + lis1[lis1_index] + "\n"))
#         # 遍历regions，keys为当前日期，values是当前地区的所有市的名字和最低气温
#         for keys, values in regions.items():
#             fp.write((keys + "\n"))
#             # 遍历values，key为城市名称，value为该城市的最低温度
#             for key, value in values.items():
#                 fp.write((key + ":" + str(value) + "\t"))
#             fp.write("\n\n")


# if __name__ == '__main__':
#     # 用来存放该地区七天的温度
#     current_temperature = []
#     partitions = ["hb", "db", "hd", "hz", "hn", "xb", "xn", "gat"]
#     prefix = "http://www.weather.com.cn/textFC/"
#     # 获取七天的日期 days是个列表
#     days = gain_day()
#     # 用来存放该地区每天的温度
#     regions = {}
#     # 用来作为write_file函数里的lis1的下标
#     lis1_index = 0
#     # 遍历 所有的地区 华北，华东等等
#     for partition in partitions:
#         url = prefix + partition + ".shtml"
#         # 调用get_url获取源码
#         soup = get_url(url)
#         # 调用gain_data 获取到七天天气的源码
#         conmidtabs = gain_data(soup)
#         # 作为days数组的下标
#         day_index = 0
#         # 把七天的数据依次传递 获取每天的数据
#         for conmidtab in conmidtabs:
#             data = gain_table(conmidtab)
#             # 日期为key 当前地区的所有城市和最低温度为value
#             regions[days[day_index]] = data
#             day_index += 1

#         # 调用写入的函数把 regions 里的数据写到本地
#         write_file(regions, lis1_index)
#         # 每更换一个地区下标加1
#         lis1_index += 1