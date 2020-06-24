# #number
# #type()显示数据类型
# a,b,c,d= 20 ,2.2,True, 4+3j
# print(type(a),type(b),type(c),type(d))
# #isinstance 可以判断
# a=111
# isinstance(a,int)
# #del 删除对象引用

# #"" '' 字符串表示，并且 \ 可以换行，不耽误任何东西
# str = 'Runoob'

# print (str)          # 输出字符串
# print (str[0:-1])    # 输出第一个到倒数第二个的所有字符
# print (str[0])       # 输出字符串第一个字符
# print (str[2:5])     # 输出从第三个开始到第五个的字符
# print (str[2:])      # 输出从第三个开始的后的所有字符
# print (str * 2)      # 输出字符串两次，也可以写成 print (2 * str)
# print (str + "TEST") # 连接字符串

# #列表
# list = ['abcd', 786, 2.23, 'runoob',70.2]
# tinylist = [123, 'runoob']

# print(list)     #打印列表list
# print(list[0])  #打印列表中0位置元素
# print(list[1:3])#打印list中1到3 位置的元素 即第二个至第四个
# print(list[2:]) #打印从第三个开始的元素
# print(tinylist*2)#打印两遍该列表   
# print(list + tinylist)#连接两个列表

# #反转字符串
# def reversWords(input):
#     #通过空格将字符串分隔，把各个单词分割成列表
#     inputWords = input.split(" ")
#     #第一个-1 ，表示最后一个元素
#     #第二个参数为空，表示移动到列表末尾
#     #第三个参数为步长，-1 表示逆向
#     inputWords = inputWords[-1::-1]
#     #重新组合字符串
#     output = ' '.join(inputWords)

#     return output

# if __name__=="__main__":
#     input = 'I like runoob'
#     rw = reversWords(input)
#     print(rw)

# #数值计算
# a=3
# b=5
# c=a+b
# print(c)
# print(a)
# print(b)

# #python中不可变数据为：number string tuple
# #可变数据为 ：list dictionary set



# #元组
# #元组（tuple）与列表类似，不同之处在于元组的元素不能修改
# #元组写在小括号 () 里，元素之间用逗号隔开。 如下
# tuple = ('abcd', 786, 2.23, 'runoob',70.2)
# tinytuple = (123,'runoob')

# print(tuple)
# print(tuple*2)
# print(tuple[0])
# print(tuple[2:])
# print(tuple[2:5])
# print(tuple+tinytuple)

# #集合
# #创建集合可以用() {}
# #创建空集合必须用（）， 因为{}是创建字典的
# sites = {'Google','Taobao','Runoob','Facebook','Zhihu','Baidu'}
# print(sites) #集合将删去重复的元素

# #成员测试
# if 'Runoob' in sites:
#     print('Runoob in sites')
# else:
#     print('Runoob is not in sites')

# #进行集合运算
# #不得不说 python 太强了
# a = set ('abjadslfje')
# b = set ('abjaxjitep')
# print(a)
# print(a-b)
# print(a&b)
# print(a|b)
# print(a^b)

# #字典
# #简介
# #列表是有序的对象集合，字典是无序的对象集合。两者之间的区别在于：
# #字典当中的元素是通过键来存取的，而不是通过偏移存取。
# # 字典是一种映射类型，字典用 { } 标识，
# # 它是一个无序的 键(key) : 值(value) 的集合。
# # 键(key)必须使用不可变类型。
# # 在同一个字典中，键(key)必须是唯一的

# dict = {}
# dict['one'] = "1- cainiao teaching "
# dict[2] = "2- cainiao methods"

# tinydict = {'name':'runoob','code':1,'site':'www.runoob.com'}

# print(dict['one'])  #输出键为'one'的值
# print(dict[2])      #输出键为2 的值
# print(tinylist)     #输出整个字典
# print(tinydict.keys())  #输出键
# print(tinydict.values())#输出值
# #字典类型也有一些内置的函数，例如clear()、keys()、values()等

# #python 数据类型转换
# # int(x [，base])      #将x转换为一个整数
# # float(x)            #将x转换到一个浮点数
# # complex(real [，imag])#创建一个复数
# # str(x)              #将对象 x 转换为字符串
# # repr(x)             #将对象 x 转换为表达式字符串
# # eval(str)           #用来计算在字符串中的有效Python表达式,并返回一个对象
# # tuple(s)            #将序列 s 转换为一个元组
# # list(s)             #将序列 s 转换为一个列表
# # set(s)              #转换为可变集合
# # dict(d)             #创建一个字典。d 必须是一个 (key, value)元组序列。
# # frozenset(s)        #转换为不可变集合
# # chr(x)              #将一个整数转换为一个字符
# # ord(x)              #将一个字符转换为它的整数
# # hex(x)              #将一个整数转换为一个十六进制字符串
# # oct(x)              #将一个整数转换为一个八进制字符串

# #位运算符
# a = 60 
# b = 13
# print(a)
# print(b)
# print(a&b)
# print(a|b)
# print(a^b)
# print(~a)

# a=10 
# b=20
# #逻辑运算符
# if (a and b):
#     print('all true')
# else:
#     print('a number is not true')
# if ( a or b ):
#    print ("2 - 变量 a 和 b 都为 true，或其中一个变量为 true")
# else:
#    print ("2 - 变量 a 和 b 都不为 true")
 
# # 修改变量 a 的值
# a = 0
# if ( a and b ):
#    print ("3 - 变量 a 和 b 都为 true")
# else:
#    print ("3 - 变量 a 和 b 有一个不为 true")
 
# if ( a or b ):
#    print ("4 - 变量 a 和 b 都为 true，或其中一个变量为 true")
# else:
#    print ("4 - 变量 a 和 b 都不为 true")
 
# if not( a and b ):
#    print ("5 - 变量 a 和 b 都为 false，或其中一个变量为 false")
# else:
#    print ("5 - 变量 a 和 b 都为 true")

# #成员运算符 in  not in
# a = 10
# b = 20
# list = [1, 2, 3, 4, 5 ]
# now =list
# if ( a in now ):
#    print ("1 - 变量 a 在给定的列表中 list 中")
# else:
#    print ("1 - 变量 a 不在给定的列表中 list 中")
 
# if ( b not in now ):
#    print ("2 - 变量 b 不在给定的列表中 list 中")
# else:
#    print ("2 - 变量 b 在给定的列表中 list 中")
 
# # 修改变量 a 的值
# a = 2
# if ( a in now ):
#    print ("3 - 变量 a 在给定的列表中 list 中")
# else:
#    print ("3 - 变量 a 不在给定的列表中 list 中")

# a = 20
# b = 20
# # id() 函数用于获取对象内存地址
# if ( a is b ):
#    print ("1 - a 和 b 有相同的标识")
# else:
#    print ("1 - a 和 b 没有相同的标识")
 
# if ( id(a) == id(b) ):
#    print ("2 - a 和 b 有相同的标识")
# else:
#    print ("2 - a 和 b 没有相同的标识")
 
# # 修改变量 b 的值
# b = 30
# if ( a is b ):
#    print ("3 - a 和 b 有相同的标识")
# else:
#    print ("3 - a 和 b 没有相同的标识")
 
# if ( a is not b ):
#    print ("4 - a 和 b 没有相同的标识")
# else:
#    print ("4 - a 和 b 有相同的标识")

# #字符串更新
# var1 = 'hello world!'
# print(var1[:6]+'runoob')

# #\n 换行 \v 纵向制表符
# #\t 横向制表符 \r 回车
# #\f 换页    \oyy 8进制 \xyy 16进制

# #字符串格式化
# print("我叫 %s 今年 %d 岁",'ming',10)

# para_str = """这是一个多行字符串的实例
# 多行字符串可以使用制表符
# TAB ( \t )。
# 也可以使用换行符 [ \n ]。
# """
# print (para_str)


# #f-string 
# name = ' runoob'
# f'hello{name}'
# f'{1+2}'
# print(f'hello{name}')
# print(f'{1+2}')

#在Python3中，所有的字符串都是Unicode字符串

#列表可拼接，可嵌套
#Python 的元组与列表类似，不同之处在于元组的元素不能修改。
# 元组使用小括号，列表使用方括号。
# 元组创建很简单，只需要在括号中添加元素，并使用逗号隔开即可。
# 字典值可以是任何的 python 对象，既可以是标准的对象，也可以是用户定义的，但键不行。
# 两个重要的点需要记住：
# 不允许同一个键出现两次。创建时如果同一个键被赋值两次，后一个值会被记住，如下实例：
# 键必须不可变，所以可以用数字，字符串或元组充当，而用列表就不行

#集合  无序不重合 会自动删除重复元素
# basket =('ahdsf','ok','what','none')
# if 'ok' not in basket:
#    print('it really good')
# else:
#    print('nothing happend')

# #集合之间可运算   
# a = set('abracadabra')
# b = set('alacazam')

#添加 元素
# a.add('what')
# b.update([4,6])
# a.remove('a')
# b.discard('ay')
# print(a,b)
# a.pop()  #随机删除一个元素
# print(a)
# a.clear()
# print(a)

#斐波那契数列
# a,b=0,1
# while b<10:
#    print(b)
#    a,b=b,a+b

#end 关键字
# a,b=0,1
# while b<1000:
#    print(b,end=' ')
#    a,b=b,a+b

#狗年龄判断

# c = int(input("please input your dog year"))

# if c==1:
#    print('the dog is 14 years old')
# if c==2:
#    print('the dog is 22 years old')
# if c>2:
#    print("the dog is %s years old" %str(22+(c-2)*5))


#1-100 sum
#while 

# i=1
# sum = 0
# while i<= 100:
#    sum +=i
#    i+=1
# print(sum)
# dict = {['Name']: 'Runoob', 'Age': 7}
# print ("dict['Name']: ", dict['Name'])

# count = 0
# while count < 5:
#    print(count,'<5')
#    count +=1
# else:
#    print(count,'>= 5')

# languanges = ['C','C++','Perl','Python']
# for x in languanges:
#    print(x)

#break 语句
# sites = ['baidu','google','runoob','taobao']
# for site in sites:
#    if site == 'runoob':
#       print('runoob yes')
#       break
#    else:
#       print('nothing happend and no for ')
# print('complete for ')

# for i in range(5):
#    print(i,end = ' ')

# for i in range(0,10,3):
#    print(i,end = ' ')

# for i in range(5,9):
#    print(i,end = ' ')

# for i in range(-10,-100,-3):
#    print(i,end=' ')

# a = ['Google','Baidu','Runoob','Taobao','QQ']
# for i in range(len(a)):
#    print(i,a[i])

# a=list(range(5))
# print(a)

# n = 5
# while n>0: 
#    n-=1
#    if n==2:
#       continue
#    print(n)
# print('循环结束')

# for letter in 'runoob':
#    if letter == 'b':
#       break
#    print('till now the character is :',letter)

# var = 10 
# while var >0:
#    print('till now the uncertain is :',var)
#    var -=1
#    if var ==5:
#       break
# print('byebye!')

# else  循环
import math
for n in range(2,10):
   for x in range(2,n):
      if n%x == 0:
         print(n,'==',x,'*',n//x)
         break
   else:
      print(n,'none zhi number')

#pass 语句
#pass 不做任何事情，一般用做占位语句，如下实例
