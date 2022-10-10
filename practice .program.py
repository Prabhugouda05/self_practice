# s = "hello word"
# for item in range(len(s)):
#     print(s[item],end=" ") ###traversing through string

# g = "hi hero"
# for char in range(len(g)):
#     print(g[char],end="")
# h = {10,20,38,46}##### by set
# for num in h:
#     print(num,end=" ,")
# ##### by dict####
# d = {"a":10,"b":20,"c":30}
# # for key in d:
# #     print(key,end=",")
# for key in d:
#     print(d.get(key),end=",")
d = {"a":12,"b":13,"c":14}
# for item in d:
#     print(item,end=",")###only key
# for key in d:
#         print(d[key])###only value


######reversed string#####
s = "hello word"
# for char in range(len(s)-1,-1,-1):
#     print(str(char),end=",")
# for item in s[::-1]:
#     print(item,end=",")
#
# for char in reversed(s):
#     print(char,end=",")
# for char in enumerate(s):
#     print(char,end=",")
# for char in enumerate(s):
#     print(char[0],end=",")
# for char in enumerate(s):
#     print(char[0],char[1],end=",")


#
# s = "hello world"
# vowel = 0
# const = 0
# space = 0
# for char in s:
#     if char in "aeiouAEIOU":
#         vowel += 1
#     elif char == " ":
#         space += 1
#     else:
#         const += 1
#
# print("vowel ", vowel)
# print("consonents ", const)
# print("space ", space)

# import turtle
# import colorsys
# t = turtle.Turtle()
# s = turtle.Screen()
# s.bgcolor("black")
# t.speed(0)
# n=36
# h=0
# for i in range(460):
#     c=colorsys.hsv_to_rgb(h,1,0.9)
#     n+=1/n
#     t.color(c)
#     t.left(145)
#     for j in range(5):
#         t.forward(300)
#         t.left(150)


# from turtle import *
# color("red")
# begin_fill()
# pensize(3)
# left(50)
# forward(133)
# circle(50,200)
# right(140)
# circle(50,200)
# forward(133)
# end_fill()