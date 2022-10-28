a=[10,2,3,4,5]
# a1=[]
# for i in a:
#     b=1
#     for j in a:
#         if i==j:
#             pass
#         else:
#             b=b*j
#
#     a1.append(b)
# print(a1)
# f,s=a[0],a[0]
# for i in (a):
#     if f<i:
#         s=f
#         f=i
#     elif s<i and i!=f:
#         s=i
#
#
# print(f,s)

# s= input("enter the value:")
# n=len(s)
# c=[0]*(n+1)
# c[0],c[1]=1,1
# # print(c)
# for i in range(2,n+1):
#     if s[i-1]>'0':
#         c[i]=c[i-1]
#     if ( s[i-2]=='1' or(s[i-2]=='2' and s[i-1]<'7')):
#         c[i]+=c[i-2]

# print(c[n])
# print(c)
# def name(f):
#     def making(s):
#         f(s)
#         return ( s.upper())
#     return making
# @name
# def usual(n):
#     return (n)
#
# print(usual('sardar'))
