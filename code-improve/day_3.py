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
# import sys
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
