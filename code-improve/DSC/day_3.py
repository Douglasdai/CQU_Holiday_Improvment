#迭代器与生成器
# list = [ 1,2,3,4]
# it = iter(list)
# for i in range(4):
#     print(next(it))

# import sys
# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         sys.exit()

#创造迭代器
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         x = self.a
#         self.a +=1 
#         return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# for i in range(5):
#     print(next(myiter))

#StopIteration
# class MyNumbers:
#     def __iter__(self):
#         self.a = 1
#         return self

#     def __next__(self):
#         if self.a <= 20:
#             x = self.a
#             self.a +=1 
#             return x
#         else:
#             raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#     print(x)

#生成器
#yield 函数
#生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点
#理解生成器就是一个迭代器
#调用一个生成器函数，返回的是一个迭代器对象   
#import sys
# def fibonacci(n):
#     a,b,counter=1,1,0
#     while True:
#         if (counter >n):
#             return
#         yield a 
#         a,b = b,a+b
#         counter  +=1
# f = fibonacci(10)
# while True:
#     try:
#         print(next(f),end=' ')
#     except StopIteration:
#         sys.exit()


#函数 
#def 函数名（参数列表）:
#    函数体

# def hello():
#     print("hello world ")

# hello()
# import math

# def area(r,h):
#     print("the circle is :",r*r*h*3.14)
# # area(2,3)

# def printme(str):
#     print(str)
#     return

# printme('调用用户自定义函数')
# printme('再次调用')

#mutable immutable
#string tuples numbers 不可更改
#list dict 是可以修改的对象
#不可变实例
# def ChangeInt(a):
#     a =10 
# b= 2
# ChangeInt(b)
# print(b)
# #可变实例
# def changeme(mylist):
#     '传入修改列表'
#     mylist.append((1,2,3,4))
#     print('the list is  ',mylist)
#     return

'调用函数'
# mylist = [10,20,30]
# changeme(mylist)
# print('function besides is :',mylist)

#参数
#必需参数  不加参数会报错
#关键字参数
# def printme(str):
#     print(str)
#     return

# printme (str = 'runoob teaching ')


#函数参数使用不需要指定顺序
# def printinfo(name ,age ):
#     print('name :',name)
#     print('age：' ,age)
#     return

# printinfo(age= 20 ,name = 'dsc')

#默认参数
# def printinfo(name ,age = 25):
#     print('name :',name)
#     print('age：' ,age)
#     return

# printinfo(age= 20 ,name = 'dsc')
# print('---------------')
# printinfo(name = 'runoob')

#不定长参数
#基本语法和框架
# def functionname([formal_args,] *var_args_tuple ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]

# def printinfo(arg1, *vartuple):
#     print("output: ")
#     print(arg1)
#     print(vartuple)
#     return
# printinfo(70,60,50)
 
# def printinfo(arg1,*vartuple):
#     print('output :')
#     print(arg1)
#     print(vartuple)
#     for i in vartuple:
#         print(i)
#     return

# #调用函数
# printinfo(10)
# printinfo(70,60,50)


#两个**
#格式
#def functionname([formal_args,] **var_args_dict ):
#    "函数_文档字符串"
#    function_suite
#    return [expression]
#字典形式导入

# def printinfo(arg1,**vardict):
#     print("output : ")
#     print(arg1)
#     print(vardict)

# printinfo(1,a=2,b=4)

#声明函数时，*可单独出现， 但是*后的参数必须使用关键字传入
# def f(a,b,*,c):
#     return a+b+c

# d = f(1,2,c= 3)
# print(d)

#匿名函数
#结构
# lambda [arg1 [,arg2,.....argn]]:expression

# sum = lambda arg1,arg2: arg1+arg2

# print('the sum is:',sum(10,20))
# print('the sum is :',sum(20,20))


#return
# def sum(a,b):
#     total = a+b
#     print('in the sum ,the total is :',total)
#     return total

# print(sum(10,20))

#强制位置参数
# def f(a,b,/,c,d,*,e,f):
#     print(a,b,c,d,e,f)

# f(10,20,30,40,e = 50,f= 60)

#数据结构
# a = [66.23,333,333,1,1234.5]
# print(a.count(333),a.count(66.23),a.count('x'))
# a.insert(2,-1)
# a.append(333)
# print(a)
# a.index(333)
# print(a)
# a.remove(333)
# print(a)
# a.reverse()
# print(a)
# a.sort()
# print(a)

#类似 insert, remove 或 sort 
#等修改列表的方法没有返回值


#列表当堆栈使用
# stack = [3,4,5]
# stack.append(6)
# stack.append(7)
# print(stack)
# stack.pop()
# print(stack)
#列表队列使用
# from collections import deque
# queue = deque(['Eric','John','Michal'])
# queue.append('Terry')
# queue.append("Graham")
# print(queue)
# queue.popleft()
# print(queue)
# queue.popleft()
# print(queue)


#列表推导式  非常有用
# vec = [2,4,6]
# vec = [3*x for x in vec]
# print(vec)
# vec = [[x,x**2] for x in vec]
# print(vec)

# freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
# freshfruit = [weapon.strip() for weapon in freshfruit]
# print(freshfruit)
# vec = [3*x for x in vec if x>3]
# print(vec)
# vec = [3*x for x in vec if x<2]
# print(vec)
# vec1 = [2,4,6]
# vec2 = [4,3,-9]
# vec1 = [x*y for x in vec1 for y in vec2]
# vec1 = [x+y for x in vec1 for y in vec2]
# vec1 = [vec1[i]*vec2[i] for i in range(len(vec1))]
# print(vec1)

#嵌套
# [str(round(355/113),i)for i in range(1,6)]

#断言 assert
#矩阵转置
# matrix = [[1, 2, 3, 4],[5, 6, 7, 8],[9, 10, 11, 12],]
# matrix = [[row[i] for row in matrix] for i in range(4)]
# print(matrix)


#del 语句
#for 表达式

#上课内容
# max =2 
# num =0
# for max in range(1,max+1):
#     num+=max
#     print(num)
# for i in range(0,5):
#     j =0 
#     while j <4 :
#         print('i is %d,and j is %d'%(i,j))
#         j+=1

#遍历技巧
# knights = {'gallahad': 'the pure', 'robin': 'the brave'}
# for k, v in knights.items():
#     print(k,v)

# for i,v in enumerate(['tic','tac','toe']):
#     print(i,v)

# questions = ['name','quest','favorite color']
# answers = ['lancelot','the holy grail','blue']
# for q,a in zip(questions,answers):
#     print('what is your {0}? it is {1}'.format(q,a))

# #反向遍历
# for i in reversed(range(1,10,2)):
#     print(i)

# #顺序遍历
# basket = ['apple','orange','apple','pear','orange','banana']
# for f in sorted(set(basket)):#转到集合意思为删除重复元素
#     print(f)

#模块
# import sys
# print('命令行参数如下：')
# for i in sys.argv:
#     print(i)

# print('\n\nPython path is :',sys.path,'\n')
#fibo 模块的内容
# def fib(n):
#     a,b=0,1
#     while b<n:
#         a,b=b,a+b
#         print(b)

# def fib1(n):
#     a,b=0,1
#     result = []
#     while b <n:
#         result.append(b)
#         a,b=b,a+b
#     return result

# import fibo
# fibo.fib(1000)
# c = fibo.fib1(1000)
# print(c)

# if __name__=='__mian__':
#     print('progress is running ')
# else:
#     print('I am from another ')
# import sys
# print(dir(sys))
# print(repr(1/7))
# for x in range(1,11):
#     print(repr(x).rjust(2),repr(x*x).rjust(3),end=' ')
#     print(repr(x*x*x).rjust(4))

# for x in range(1,11):
#     print('{0:2d}{1:4d}{2:5d}'.format(x,x*x,x*x*x))

# print('{0} 和 {1}'.format('Google', 'Runoob'))
# print('{1} 和 {0}'.format('Google', 'Runoob'))
# print('{name}网址： {site}'.format(name='菜鸟教程', site='www.runoob.com'))

# import math 
# print('常量PI的值为:{}。'.format(math.pi))

# print('常量PI的值为:{!a}。'.format(math.pi))
# import math 
# table = {'Google':1,'Runoob':2,'Taobao':3}
# for name,number in table.items():
#     print('{0:10} ==> {1:10d}'.format(name,number))

# import math
# print('pi is %5.3f'%math.pi)
# f = open("/tmp/foo.txt", "w")

# f.write( "Python 是一个非常好的语言。\n是的，的确非常好!!\n" )

# # 关闭打开的文件
# f.close()
# import pickle
# data1 = {'a': [1, 2.0, 3, 4+6j],
#          'b': ('string', u'Unicode string'),
#          'c': None}

# selfref_list = [1, 2, 3]
# selfref_list.append(selfref_list)

# output = open('data.pkl', 'wb')
# # Pickle dictionary using protocol 0.
# pickle.dump(data1, output)

# # Pickle the list using the highest protocol available.
# pickle.dump(selfref_list, output, -1)
# output.close()

#错误与异常
# def divide(x, y):
#         try:
#             result = x / y
#         except ZeroDivisionError:
#             print("division by zero!")
#         else:
#             print("result is", result)
#         finally:
#             print("executing finally clause")
# divide(2,1)
# divide(2,0)
# divide('2','1')

#python 面向对象
# class myclass:
#     i =12345
#     def f(self):
#         return 'hello world'

# x=myclass()
# print('myclass  i is : ',x.i)
# print('myclass f is :',x.f())

#类方法
# class people:
#     name = ' '
#     age =0
#     __weight = 0
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age =a
#         self.__weight= w
#     def speak(self):
#         print('%s say that : i am %d yeas old' %(self.name,self.age))

# class student(people):
#     grade = ' '
#     def __init__(self,n,a,w,g):
#         people.__init__(self,n,a,w)
#         self.grade = g
#     def speak(self):
#         print('%s say that : i am %d yeas old and grade %d' %(self.name,self.age,self.grade))

# s= student('xiaoming ',10,50,4)
# s.speak()


# 多继承
# class people:
#     #定义基本属性
#     name = ''
#     age = 0
#     #定义私有属性,私有属性在类外部无法直接进行访问
#     __weight = 0
#     #定义构造方法
#     def __init__(self,n,a,w):
#         self.name = n
#         self.age = a
#         self.__weight = w
#     def speak(self):
#         print("%s 说: 我 %d 岁。" %(self.name,self.age))
 
# #单继承示例
# class student(people):
#     grade = ''
#     def __init__(self,n,a,w,g):
#         #调用父类的构函
#         people.__init__(self,n,a,w)
#         self.grade = g
#     #覆写父类的方法
#     def speak(self):
#         print("%s 说: 我 %d 岁了，我在读 %d 年级"%(self.name,self.age,self.grade))
 
# #另一个类，多重继承之前的准备
# class speaker():
#     topic = ''
#     name = ''
#     def __init__(self,n,t):
#         self.name = n
#         self.topic = t
#     def speak(self):
#         print("我叫 %s，我是一个演说家，我演讲的主题是 %s"%(self.name,self.topic))
 
# #多重继承
# class sample(speaker,student):
#     a =''
#     def __init__(self,n,a,w,g,t):
#         student.__init__(self,n,a,w,g)
#         speaker.__init__(self,n,t)
 
# test = sample("Tim",25,80,4,"Python")
# test.speak()   #方法名同，默认调用的是在括号中排前地父类的方法

#私有变量
# class JustCounter:
#     __secretCount = 0  # 私有变量
#     publicCount = 0    # 公开变量
 
#     def count(self):
#         self.__secretCount += 1
#         self.publicCount += 1
#         print (self.__secretCount)
 
# counter = JustCounter()
# counter.count()
# counter.count()
# print (counter.publicCount)
# from dataclasses import dataclass
# class Vector:
#     def __init__(self,a,b):
#         self.a = a
#         self.b = b
#     def __str__(self):
    
#         return 'Vector (%d,%d)'%(self.a,self.b)
    
#     def __add__(self,other):
#         return Vector(self.a+other.a,self.b+other.b)
# c = Vector(9,10)
# d = Vector(-1,2)
# print(c+d)

#作用域
#L –> E –> G –>gt

#global 和 nonlocal关键字
#全局变量
# num =1 
# def fun1():
#     global num
#     print(num)
#     num =123
#     print(num)

# fun1()
# print(num)
#nonlocal
# def outer():
#     num =10 
#     def inner():
#         nonlocal num
#         num =100 
#         print(num)
#     inner()
#     print(num)
# outer()

# a = 10
# def test(a):
#     a +=1
#     print(a)
# test(a)

# import random
# print(random.choice(['apple', 'pear', 'banana']))


#测试模块  目前不不知道是干啥得


#实例 字符串是否为数字
# def is_number(s):
#     try:
#         float(s)
#         return True
#     except ValueError:
#         pass
#     try:
#        import unicodedata
#        unicodedata.numeric(s)
#        return True
#     except (TypeError,ValueError):
#         pass
#     return False
# print(is_number('foo'))


#python 金字塔
# num=int(input())
# for i in range(1,num+1):
#     print(' '*(num-i)+'+'*(2*i-1))
# import urllib.parse
# import urllib.request
# data = bytes(urllib.parse.urlencode({'word': 'hello'}), encoding='utf8')
# response = urllib.request.urlopen('http://httpbin.org/post', data=data)
# print(response.read())