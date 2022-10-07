# count = 0###count the numbers call##
# def outer(func):
#     def wrapper(*args,**kwargs):
#         global count
#         print("fun name")
#         count +=1
#         func(*args,**kwargs)
#     return wrapper
# @ outer
# def add(a,b):
#       print(a+b)
# add(1,2)
# add(4,5)
# @outer
# def sub(a,b):
#       print(a-b)
# sub(4,6)
# print(count)
#######creating a dictionary####
import time
""" 
d ={}
def outer (func):
    def wrapper (*args,**kwargs):
        print(f"{func.__name__}function")
        if func.__name__ not in d:
            d[func.__name__]=1
        else:
            d[func.__name__]+1
            func(*args,**kwargs)
    return wrapper
@outer
def add(a,b):
    print(a+b)
add(1,2)
add(4,5)
@outer
def sub(a,b):
  print(a-b)
sub(4,6)
print(d)
"""
# ######returns the postive value######
# d
# def sub(a,b):
#     return a-b
# print(sub(4,6))ef outer(func):
#     def wrapper(*args,**kwargs):
#         print(f"executing{func.__name__}function")
#         res =func(*args,**kwargs)
#         return abs(res)
#     return wrapper
# @outer
# def add(a,b):
#     return a+b
# print(add(1,2))
# @outer
# def outer (fun):
#     def wrapper (*args,**kwargs):
#         print(f"executing{func.__name__}function"))
#         for i in range(3):
#             func(*args,*kwargs)
#     return wrapper()
# @outer
# def add(a,b):
#     print(a+b)
# add(4,5)
# def outer(func):
#     def wrapper (*args,**kwargs):
#         time.sleep(4)
#         func(*args,**kwargs)
#     return wrapper
# @outer
# def demo():
#     print("hello")
# demo()
# count =0
# def outer(func):
#     def wrapper (*args,**kwargs):
#         global count
#         print(f"executing {func.__name__}function")
#         count+=1
#         func(*args,**kwargs)
#         return wrapper
#     @outer
#     def add(a,b):
#         print(a+b)
#         add(1,2)
#         add(4,5)
#
#     @outer
#     def sub(a,b):
#      print(a-b)
#     sub(3,4)
#     sub(6,5)
#
# @outer
# def mul(a,b):
#     print(a*b)
#     mul(3,4)
#     mul(4,5)
#
# from time import sleep
# def parameter(n):
#     def outer(func):
#         def wrapper(*args,**kwargs):
#             sleep(n)
#             func(*args,**kwargs)
#         return wrapper
#     return outer
#
# @parameter(2)
# def add(a,b):
#     print(a+b)
# add(1,2)
# add(4,5)
#
# @parameter(3)
# def sub(a,b):
#     print(a-b)
# sub(50,5 )
# def display(fun):
#     def inner(*args,**kwargs):
#         print("the sum is")
#         fun(*args,**kwargs)
#     return wrapper
# @display(add)
# def add(a,b):
#     print(a+b)
#     add(5,6)


# def sms(func):
#     def inner(*args,**kwargs):
#         print("hello everyone")
#         return  func(*args,**kwargs)
#     return inner
# @ sms
# def add(a,b):
#     return  a+b
#
# print(add(2,3))
















