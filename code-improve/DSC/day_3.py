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

freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
freshfruit = [weapon.strip() for weapon in freshfruit]
print(freshfruit)