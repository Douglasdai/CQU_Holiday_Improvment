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
root = tkinter.Tk()

def helloCallBack():
    tkinter.messagebox.showinfo('the 结果',"今天晴天")

input_city = tkinter.Entry(root,show="")
input_city.pack()
w = tkinter.Label(root,text = "please input your city")
w.pack()
b = tkinter.Button(root,text = '确认',command = helloCallBack)
b.pack()
root.mainloop()
