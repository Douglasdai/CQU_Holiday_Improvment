# import pandas as pd
# import numpy as np
# import matplotlib
# df = pd.DataFrame(np.random.randn(10,4),index=pd.date_range('2020/12/18',periods=10), columns=list('ABCD'))


#简单折线图
# df.plot()
# import matplotlib.pyplot as plot
# import numpy as np
# # 着线图数据
# line = [1,2,6,8,9,15,23,29,35]

# # 指定线条粗细
# plot.plot(line,linewidth=2)
# # 设置标题
# plot.title("zszxz line ",fontsize=12)
# # 设置x轴
# plot.xlabel("x",fontsize=12)
# # 设置y轴
# plot.ylabel("y",fontsize=12)
# # 显示
# plot.show()


#齐全折线图
# import matplotlib.pyplot as plot 
# import numpy as np
# #数据
# line1=[1,2,6,8,9]
# line2=[2,4,12,16,18]

# #指定线条粗细
# plot.plot(line1,line2,linewidth = 2)
# #标题
# plot.title("example",fontsize =12)
# #设置x轴
# plot.xlabel("x",fontsize = 12)
# #y
# plot.ylabel("y",fontsize = 12)
# #显示
# plot.show()

#简单散点图
# import matplotlib.pyplot as plot
# import numpy as np
# x=[1,3,5,7,9]
# y=[2,4,6,8,10]
# #散点
# plot.scatter(x,y)

# plot.title("ex2",fontsize = 12)

# plot.xlabel("x",fontsize =12)
# plot.ylabel("y",fontsize =12)
# plot.show()

#计算型散点图
# import matplotlib.pyplot as plot
# import numpy as np 
# x_val = list(range(1,50))
# y_val = [x**2 for x in x_val]
# #折线
# # plot.plot(x_val,y_val,linewidth= 2)
# plot.xlabel("x",fontsize =12)
# plot.ylabel("y",fontsize =12)
# #散点
# # plot.scatter(x_val,y_val,color = 'black')

# plot.show()


#随即散点
# import matplotlib.pyplot as plot
# import numpy as np 
# n=500 
# x= np.random.normal(0,1,n)
# y= np.random.normal(0,1,n)

# plot.scatter(x,y,color = 'green',alpha = 0.7,marker='*')
# #设置网格线
# plot.grid(True)
# plot.show()

# import matplotlib.pyplot as plot
# import numpy as np
import tkinter
import tkinter.messagebox
import matplotlib.pyplot as plot 
import numpy as np
import urllib
#异常处理，选择处理
def searchfile2(file,c):
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
    plot.title(out_form[0]+'\n'+\
        out_form[0]+' '+out_form[1]+' '+out_form[2]+' 最高气温为：'+\
        out_form[3]+'最低气温为：'+out_form[4],fontsize = 12)
    plot.xlabel('date',fontsize = 12)
    plot.ylabel('temp',fontsize= 12)
    plot.show()


#界面(有待优化)
root = tkinter.Tk()
root.title("天气查询")
root.geometry('750x500')
# root.tf.Font(size =40 )
w = tkinter.Label(root,text = "天气查询",)
w.pack()
input_city = tkinter.Entry(width= 50)
input_city.pack()
def getuser():
    c = input_city.get()
    searchfile2("D:\\CQU_work_hard\\CQU_Holiday_Improvment\\code-improve\\DSC\\exz.txt",c)
# searchfile2("D:\\CQU_work_hard\\CQU_Holiday_Improvment\\code-improve\\DSC\\exz.txt",c)
b = tkinter.Button(root,text = '确认',command = getuser)
b.pack()
root.mainloop()


