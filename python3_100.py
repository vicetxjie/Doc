# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-
#
# '''
# 2018.07.25
# Python 练习100题
# http://www.runoob.com/python/python-100-examples.html
# '''
#
# '''
# 题目001：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# '''
# def tm001():
#
#     '''
#     [备注]：按题意直接写出来
#     '''
#     arr = []
#     for i in range(1,5):
#         for j in range(1,5):
#             for k in range(1,5):
#                 num = 100*i+10*j+k
#                 if i!=j and j!=k and i!=k and num not in arr : # 互不相同且无重复的三位数
#                     arr.append(num)
#     print(len(arr),arr)
#
# if __name__ == '__main__':
#     tm001()
#
#
#
# def tm001_1():
#     '''
#     [备注]：其实python自带排列组合模板，可以直接调用。
#     也知道这个写法，只是函数及不住，还是百度一下才能写出来。
#     如果这是面试题，能写出后一种当然好，不能的话还是老老实是的按照上面的思路来吧。
#     '''
#
#     import itertools
#     temp_arr = list(itertools.permutations([1,2,3,4],3)) # 排列 A_4^3 = (4)!/(4-3)! = (4*3*2*1)/1 = 24
#     arr = [100*t[0]+10*t[1]+t[2] for t in temp_arr]
#     print(len(arr),arr)
#
# if __name__ == '__main__':
#     tm001_1()
#
#
# '''
# 题目002：企业发放的奖金根据利润I的多少来提成：
# 低于或等于10万元时，奖金可提10%；
# 利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；
# 20万到40万之间时，高于20万元的部分，可提成5%；
# 40万到60万之间时高于40万元的部分，可提成3%；
# 60万到100万之间时，高于60万元的部分，可提成1.5%；
# 高于100万元时，超过100万元的部分按1%提成。
# 从键盘输入当月利润I，求应发放奖金总数？
# '''
#
# def tm002():
#     '''
#     程序分析：请利用数轴来分界，定位。
#     【备注】：这种处理数轴问题的写法，值的参考。比elif的写法，简洁方便的多。
#     '''
#
#     lirun = int(input('净利润： '))
#     dengji = [1000000,600000,400000,200000,100000,0]
#     bili = [0.01,0.015,0.03,0.05,0.075,0.1]
#     jiangjin = 0
#     for i in range(len(dengji)):
#         if lirun > dengji[i]:                      # 对于处于区间的部分
#             jiangjin+=(lirun-dengji[i])*bili[i]    # 计算并累加奖励
#             lirun=dengji[i]                        # 剩余部分
#     print(jiangjin)
#
# if __name__ == '__main__':
#     tm002()
#
#
#
# '''
# 题目003：一个整数，它加上100后是一个完全平方数，再加上168又是一个完全平方数，请问该数是多少？
# '''
#
# def tm003():
#     '''
#     [备注]：网站上是求了一下方程，没细看。
#     python又不是没有开方函数，直接按字面意思解了。
#     '''
#
#     import math
#     for i in range(1000):
#         x = math.sqrt(i+100)
#         y = math.sqrt(i+100+168)
#         if x%1==0 and y%1==0:
#             print(i)
#
# if __name__ == '__main__':
#     tm003()
#
#
#
# '''
# 题目004：输入某年某月某日，判断这一天是这一年的第几天？
# '''
#
# def tm004():
#
#     '''
#     【备注】：知道python有时间元组这一概念，这道题完全不需要计算。
#     时间元组包含9个属性
#     tm_year     年
#     tm_mon      月（1～12）
#     tm_mday     日（1～31）
#     tm_hour     时（0～23）
#     tm_min      分（0～59）
#     tm_sec      秒（0～61，60或61是闰秒）
#     tm_wday     星期（0～6，0是周一）
#     tm_yday     第几天（1～366）
#     tm_isdst    夏令时（平时用不到）
#     '''
#     import time
#     date = input('输入时间（例如2018-07-25）： ')
#     st = time.strptime(date, '%Y-%m-%d')     # 时间文本转化成时间元组
#     num = st.tm_yday
#     print(num)
#
# if __name__ == '__main__':
#     tm004()
#
#
#
# '''
# 题目005：输入三个整数x,y,z，请把这三个数由小到大输出。
# '''
#
# def tm005():
#     print('输入三个整数： ')
#     x = int(input('输入第一个整数： '))
#     y = int(input('输入第二个整数： '))
#     z = int(input('输入第三个整数： '))
#     l = [x,y,z]
#     arr = sorted(l)     # 你也可以使用list.sort()方法来排序，但list本身会被修改
#     print(arr)
#
# if __name__ == '__main__':
#     tm005()
#
# '''
# 题目006：斐波那契数列。
# '''
# import sys
# def tm006(n=10):
#     '''
#     程序分析：斐波那契数列，又称黄金分割数列，指的是这样一个数列：0、1、1、2、3、5、8、13、21、34、……。
#     【个人备注】：很多种解法，我是按照分割的方式，每次取列表后两项，然后相加。
#     '''
#
#     l = [0,1]
#     for i in range(n-len(l)):
#         arr = l[-2:]
#         l.append(arr[0]+arr[1])
#     print(l)
#
# if __name__ == '__main__':
#     tm006(int(sys.argv[1]))
#
#
# '''
# 题目007：将一个列表的数据复制到另一个列表中。
# '''
#
# def tm007():
#     '''
#     【个人备注】：如果系统的看过python教程之类的应该都知道。
#     Python里面一切都是对象，list的复制需要用[:]的方式。
#     至于b=a只是相当于给a取了个别名而已，指向的是同一个列表，并没有实现复制。
#     '''
#
#     a = [1,2,3]
#     b = a[:]
#     '''题外话'''
#     a[0] = 0
#     print(id(a),id(b))      # 可以看到a,b的内存不一致，是复制
#     print(a,b)              # 修改a,b不变
#     a = [1,2,3]
#     b = a
#     a[0] = 0
#     print(id(a),id(b))      # 如果去掉[:],可以看到a,b的内存一致，并没有复制，指向的是同一个列表
#     print(a,b)              # 修改a，b也变
#
# if __name__ == '__main__':
#     tm007()
#
#
# '''
# 题目008：题目：输出 9*9 乘法口诀表。
# '''
#
# def tm008():
#     # 【个人备注】：已经忘了，百度了才想起来口诀表具体长什么样。
#     # 注意 %-7s 和 end='' 的用法，其他没什么。
#
#     for i in range(1,10):
#         for j in range(1,10):
#             if j<=i:
#                 string = '%d*%d=%d' % (j,i,j*i)
#                 print('%-7s' % string, end='')
#         print('')
#
# if __name__ == '__main__':
#     tm008()
#
#
# '''
# 题目009：暂停一秒输出。
# '''
#
# def tm009():
#     # time.sleep()
#
#     import time
#     a = time.time()
#     time.sleep(1)
#     b = time.time()
#     print(b-a)
#
# if __name__ == '__main__':
#     tm009()
#
#
# '''
# 题目010：暂停一秒输出，并格式化当前时间。
# '''
#
# def tm010():
#
#     import time
#     a = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     print(a)
#     time.sleep(1)
#     b = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
#     print(b)
#
# if __name__ == '__main__':
#     tm010()
#
#
# '''
# 题目011：古典问题：
# 有一对兔子，
# 从出生后第3个月起每个月都生一对兔子，
# 小兔子长到第三个月后每个月又生一对兔子。
# 假如兔子都不死。
# 问每个月的兔子总数为多少？
# '''
#
# def tm011():
#     # 其实这道题就是斐波那契数列的由来。
#     # 【个人备注】：理清思路是关键，理解成满两个月后，每月都能生兔子，就好办了。
#
#     m1 = 1      # 满月
#     m2 = 0      # 满两个月
#     mm = 0      # 可以月月生兔子了
#     for i in range(1,10):
#         # 过了一个月之后
#         mm = mm+m2          # 加入新增成年的兔子
#         m2 = m1             # 满月的变成满两个月
#         m1 = mm             # 这个月新出生兔子
#         print(i,mm,m1,m2,mm+m1+m2)   # 每个月有多少对兔子
#
# if __name__ == '__main__':
#     tm011()


