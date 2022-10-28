# n=13
# for i in range(2,n):
#     if n%i!=0 and i*i>n :
#         print('prime')
#         break
#
#     if n%i == 0:
#         print('not a prime')
#         break

# l=['a','x','b','x','c','x','d','x']
# l[1::2]=[]
#
# print(l)
# lis=eval(input(""))
# print((lis))
# t=1,23,3
# print(type(t))
#
# l=[-1,16,17,3,4,3,2,5,11,15 ]
# l1=l[0]
# l2=0
# for i in range(len(l)-1):
#
#
# #     for j in range(len(l)):
# #         if l[j]-l[i] > l1:
# #             l1=l[j]-l[i]
# #             l2=(l[i],l[j])
# # print(l1,l2)
#
# import sys
# for line in sys.stdin:
#     if 'E' == line.rstrip():
#         break
#     print(f'message:{line}')
# # print('END')
# import sys
# from sys import stdin,argv
#
# my_input = stdin.read(1)
# input1 = sys.argv[1]
# print(input1)
# my_input2 = stdin.readline()
# total = int(my_input2)
# print("my_input = {}".format(my_input))
# print("my_input2 = {}".format(my_input2))
# print("total = {}".format(total))
# s='python'
# w=''
# for i in range(len(s)-1):
#     w +=(s[i]+'_')
#
# print(w+s[-1])
# marks={}
# d={'z':{'m':90,'s':40,'e':65},
#    'b':{'m':60,'s':50,'e':55},
#    'c':{'m':90,'s':60,'e':39}}
# marks=max(d.items(),key=lambda x,y:sum(y))

# marks={}
# d = {'Manjeet': {'Maths': 1, 'English': 0, 'Physics': 2, 'Chemistry': 3},
#              'Akash': {'Maths': 0, 'English': 0, 'Physics': 3, 'Chemistry': 2},
#              'Nikhil': {'Maths': 4, 'English': 2, 'Physics': 2, 'Chemistry': 3},
#              'Akshat': {'Maths': 1, 'English': 0, 'Physics': 2, 'Chemistry': 0}}
# for k,v in d.items():
#    max=0
#    for m in v.values():
#       if m>max:
#          max=m
#    marks[k]=max
# print(marks)
#
# l=[7,1,5,4,3,2]
# min_v=l[0]
# for i in range(len(l)):
#     if min_v >l[i]:
#         min_v=l[i]
#     else:
#         pass
# print(min_v)
# maxprofit=0
# for j in range(len(l)):
#     if maxprofit<(l[j]-min_v):
#         maxprofit=(min_v-l[j])
# print(maxprofit)

expression1="{{[}]}"
open_tup = tuple('({[')
close_tup = tuple(')}]')
map = dict(zip(open_tup, close_tup))
queue = []
def expes(expression):
    for i in expression:
        if i in open_tup:
            queue.append(map[i])
        elif i in close_tup:
            if not queue or i != queue.pop():
                return ("Unbalanced")
    if not queue:
        return ("Balanced")
    else:
       return ( "Unbalanced")
print(expes(expression1))
# l=[7,3,4,6,1]
# mx=0
# values=0
# mn=l[0]
# for i in range(len(l)):
#     for j in range(i+1,len(l)):
#         if mx>(l[i]-l[j]):
#             mx=(l[i]-l[j])
#             values=(l[i],l[j])
#
# print("Buy at {} and sell at {} then you Max profit will be {}".format(values[0],values[1],abs(mx)))
# l=[[10,20,30],[40,50,60],[70,80,90]]
# l1=[[],[],[]]
#
# for a,b,c in l:
#     l1[0].append(a)
#     l1[1].append(b)
#     l1[2].append(c)
#
# print(l1)
# lst=[0,500,23,450,33,1,90,101,300]
# f_m,s_m=0,0
# for i in lst:
#     if i>f_m:
#        s_m,f_m=f_m,i
#
#     elif i>s_m and s_m!=f_m:
#         s_m=i
#
# print(f_m,s_m)


s = "Have a great day"
# t = s.split(" ")
# print(" ".join([i[::-1] for i in t]))
