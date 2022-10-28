# l = [1,[2,33,6,7,],[4,8,0]]
#
# print(l[0],l[1])
#
# def fun(m):
#     for i in m:
#         if i%2 == 0:
#             return i
#         else:
#             return "else",i
# print((fun([2,32,4,5,6,8,66])))
# l=[32,44,1,33,4,3,4]
# comb_list=[]
# max_diff=1
# values=0
# for i in range(len(l)):
#     comb_list.append([l[i]])
#     for j in range(i+1,len(l)):
#         comb_list.append([l[i],l[j]])
#         if l[j:] not in comb_list:
#          comb_list.append(l[j:])
# print(comb_list)
# for i in range(len(comb_list)):
#     for j in range(i+1,len(comb_list)):
#         if sum(comb_list[i])-sum(comb_list[j])>max_diff:
#             max_diff=sum(comb_list[i])-sum(comb_list[j])
#             values=(comb_list[i],comb_list[j])
# print(max_diff,values)

#
# #
# min_diff=50
# values=0
# for i in range(len(l)):
#     comb_list.append([l[i]])
#     for j in range(i+1,len(l)):
#         comb_list.append([l[i],l[j]])
#         if l[j:] not in comb_list:
#          comb_list.append(l[j:])
# # print(comb_list)
# for i in range(len(comb_list)):
#     for j in range(i+1,len(comb_list)):
#         if abs(sum(comb_list[i])-sum(comb_list[j]))<min_diff and abs(sum(comb_list[i])-sum(comb_list[j]))!=0:
#             min_diff=abs(sum(comb_list[i])-sum(comb_list[j]))
#             values=(comb_list[i],comb_list[j])
# print(min_diff,values)

# from itertools import combinations as com
# c=0
# d={}
# for i in range(26):
#     d[chr(97+i)]=i+1
#
# n,l=list(map(int,input().split(','))),0
# for i in com(d.keys(),):
#     s=0
#     for j in i:
#         s+=d[j]
#     if s==l:
#         c+=1
# print(c)



#
# import pandas as pd
#
# df=pd.read_csv("a.csv")
# df1=df.max()
# df1.to_csv('b .csv')
# print(df1)

# d={1:'a',2:'b',3:'c'}
# print(1 in d)

# l=[1,2,4,12,0,4]
# l1=l[0]
# for i in range(len(l)-1):
#
# pass
#
# print(l)

# def merge_sort(unsorted_list):
#    if len(unsorted_list) <= 1:
#       return unsorted_list
# # Find the middle point and devide it
#    middle = len(unsorted_list) // 2
#    left_list = unsorted_list[:middle]
#    right_list = unsorted_list[middle:]
#
#    left_list = merge_sort(left_list)
#    right_list = merge_sort(right_list)
#    return list(merge(left_list, right_list))
#
# # Merge the sorted halves
# def merge(left_half,right_half):
#    res = []
#    while len(left_half) != 0 and len(right_half) != 0:
#       if left_half[0] < right_half[0]:
#          res.append(left_half[0])
#          left_half.remove(left_half[0])
#       else:
#          res.append(right_half[0])
#          right_half.remove(right_half[0])
#    if len(left_half) == 0:
#       res = res + right_half
#    else:
#       res = res + left_half
#    return res
# unsorted_list = [64, 34, 25, 12, 22, 11, 90]
# print(merge_sort(unsorted_list))

# size=int(input('enter the number: '))
# lst=[]
# for i in range(size):
#     x=input("enter :")




#     if x.isnumeric():
#         lst.append(int(x))
#     else:
#         pass
# print(lst)
#
# print([i for i in range(lst[0],lst[-1]) if i  in lst])

