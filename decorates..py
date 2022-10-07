# l = [1,2,3,4,5]
# def func(a):
#     for i in (a):
#         yield i ** 2
# print(list(func(l)))
########### tuple#####
# items = ["flipcart",2021,"gmail",1.2,[1,2,3],2+3j,True]
# def func (a):
#     for item in a :
#         if isinstance(item,(int,float,complex)):
#             yield item
# print(tuple(func(items)))
###########strings#########
# names = ["bob","steve","alex","maya","john"]
# def func(a):
#     for item in a:
#         if len(item)%2!=0:
#             yield item[::-1]
# print(list(func(names)))
##############numeric value###############
# items = ["flipcart",2021,"gmail",1.2,[1,2,3],2+3j,True]
# def func(a):
#     for item in a:
#         if isinstance(item,(float,bool,complex,int)):
#             yield str (item)[::-1]
#         else:
#             yield item
# print(list(func(items)))
# # ##########33decimalpoint###############
# import math
# PI = math.pi
# print(PI)
# # def func(num):
# #     for i in range(num):
# #         yield round(PI,i)
# # print(list(func(6)))
# #######expression#########3
# res=(round(PI,i) for i in range(6))
# print(list(res))
###############
# def func(*args):
#         if len(args)>5:
#             yield f"{len(args)}is greater than 5"
#         else:
#             yield f"{len(args)}is less than 5"
# print(list(func(1,2,3,4,5,)))


# def func(string,num):
#     if num==0:
#         for value, ele in enumerate(string):
#             if value %2!=0:
#                 yield ele
#     if num == 1:
#         for value, ele in enumerate(string):
#             if value % 2 == 0:
#                 yield ele
# print(list(func("TRACXN",0)))
# print(list(func("TRACXN",1)))
# n
# def func(a):
#     n1=0
#     n2=1
#     for i in range(a):
#         yield n1
#         n1,n2=n2,n1+n2
# print(list(func(10)))
#
#
#
#
#
#
#
#
#
#
#
#
#
# def func(num):
#     n1=0
#     n2=1
#     for i in range(num):
#         yield n1
#         n1,n2=n2,n1+n2
# print(list(func(10)))
#
#
# def func (num):
#     n1=0
#     n2=1
#     l=[]
#     for vale in range(10):
#         l.append(n1)
#         n1,n2=n2,n1+n2
#         if num in l:
#             yield "it is fibionic"
#
#     else:
#         yield "it is not a fibionic"
# print(list(func(10)))
#
#
# names = ['laura','steve','bill','james','greig','scott','alex','ive']
# def func (a):
#     for name in names:
#         if name[0].lower() in "aeiou":
#             yield name
#
# # print(list(func(names)))
# d = {"walmart":7, "gmail": 5, "google": 6, "flipcart": 8}
# # print(sorted(d))
# print(sorted(d.items(),key=lambda a:a[-1],reverse=True ))

# l = [19,28,23,34,56]
# print(sorted(l,reverse=True))
# d = {"b":1,"c":2,"a":3}
# print(sorted(d,reverse=True))
