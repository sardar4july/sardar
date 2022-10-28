# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
# if __name__ == '__main__':
    # print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# functions=[]
# for i in range(8):
#     def my_function():
#         return i
#     functions.append(my_function)
# results=[function() for function in functions]
# print(results)
# print(functions)

# def fact(n):
#
#     if n<0:
#         return ("please enter positive number")
#     elif n==1:
#         return 1
#     else:
#
#         return n*fact(n-1)
#
# print(fact(10))
#
# x=str(n1)
# c=0
# for i in x[::-1]:
#
#     if i !='0':
#         break
#     else:
#         c+=1
# print(c)

# def fact(x):
#
#     # x1=request.POST['y']
#     # x=int(x1)
#     if x<0:
#         return  ("please enter positive number")
#     elif x==1:
#         return 1
#     else:
#
#         n4= x*fact(x-1)
#         d = str(n4)
#         c = 0
#         for i in d[::-1]:
#
#             if i != '0':
#                 break
#             else:
#                 c += 1
#     return c
#
# print(fact(10))
# n=4
# res=1
# for i in range(1,n+1):
#     res=res*i
# print(res)
# n=5
# a,b=0,1
# for i in range(n):
#     print(a, end=' ')
#     a,b=b,a+b
# def fibinocii(n):
#     if n<=1:
#         return n
#     else:
#         return (fibinocii(n-2)+fibinocii(n-1))
#
# for i in range(n):
#     print(fibinocii(i) , end=' ')
# s='string'
# print(s[::-1])

# def rever_strng(s):
#     if len(s)==0:
#         return s
#     else:
#        return rever_strng(s[1:])+s[0]
#
# print(rever_strng(s))
# s='aaabbbccdddss'
# d=''
# c=1
# for i in range(len(s)-1):
#     if s[i]==s[i+1]:
#         c+=1
#     else:
#         d+=s[i]+str(c)
#         c=1
# d+=s[i+1]+str(c)
# print(d)

# for i in range(len(s)):
#     if s[i].isalpha() and s[i+1].isdigit():
#        s1+=s[i]*int(s[i+1])
#
# print(s1)
# s='a31b30c2d3s2'
# s1=''
#
# for i in range(len(s)):
#
#     if s[i].isalpha():
#         s1+=s[i]
#     elif s[i].isdigit():
#         b=""
#         for j in range(i,len(s)):
#             if s[j].isdigit():
#                 b+=s[j]
#             else:
#                 break
#         s1+=s1[-1]*(int(b)-1)
#
# print(s1)
# n=(input())
# sum=0
# for i in n:
#     sum +=int(i)**(len(n))
# if sum==int(n):
#     print("it is")
# else:print("not")
# n=7
# for i in range(2,n):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)
# for i in range(2,n):
#     if n%i==0:
#         print("it is not")
#         break
#     else:
#         print("yes its ")
#         break

