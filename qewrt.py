# def fizzbuzz(n):
#     r=''
#     if not n%3:
#         r+='fizz'
#     if not n%5:
#         r+='buzz'
#     return r or n
# print(fizzbuzz(8) )

# def fibi():
#     a,b=0,1
#     while True:
#         yield a
#         a,b=b,a+b
#
# a=fibi()
# for i in a:
#     print(i)
#     if i > 10:
#         break
# def f(a,b,c):
#
#
# a=[('acs',20,10),('acd',15,12),('acc',12,10)]
# a.sort(key=f(0,1,2))
# print(a)
# a=list(map(int,input().split(' ')))[:5]
# print(a)
# a=[]
# m,n=3,5
# for i in range(m):
#
#         a.append([i*j for j in range(n)])
# print(a)

# s='a+aa+aaa+aaaa'
# n=3
# new=s.replace('a',str(n))
# print(eval(new))

# import re
# s=[]
# items=[x for x in input().split(",")]
#
# for i in items:
#     if len(i)<6 or len(i)>12:
#         continue
#     elif not re.search('[0-9]',i):
#         continue
#     elif not re.search("[A-Z]",i):
#         continue
#     elif not re.search("[a-z]",i):
#         continue
#     elif not re.search('[$#@]',i):
#         continue
#     s.append(i)
#
# print(s)

# from operator import itemgetter
# x=[('Ahn', '20', '90'), ('Ony', '17', '91'), ('Jny', '17', '93'), ('Ahn', '20', '85'), ('Tom', '19', '80')]
# print(sorted(x,key=itemgetter(0,1,2)))

# import os,string
# if not os.path.exists('D:\heavy'):
#  os.makedirs('D:\heavy')
# for char in string.ascii_uppercase:
#     with open ("D:\heavy\{}.txt".format(char),'w') as f:
#         f.write('')
# c=0
# while(c<2):
#     print("courn",c)
#     c+=1
# else:
#     print('loop')
# x=list(range(0,-5,-1))
# print(x)
# for i in x:
#     print(i)
# x=9
# (exec("if x: print(x)"))
# print(eval('5+9'))
# try:
#     a=int(input())
#     b=int(input())
#     print(a/b)
# except ZeroDivisionError:
#     print('cant devide')
#
# else:
#     print("else block")
a=10
b=15
print((a,b)[a<b])
print({True:a,False:b}[a<b])
print((lambda:a,lambda:b)[a>b]())
