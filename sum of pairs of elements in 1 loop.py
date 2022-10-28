l=[2,3,4,-9,-7,0,-3,7,-2,9,9,9]
'doubles'
import time
sum=9
# start_time=time.time()
n=len(l)
for i in range(n-1):
    if ((-l[i])+sum) in l[i+1:]:
        # time.sleep(2)
        print((l[i],((-l[i]))+sum))
# end_time=time.time()
# print("duration:",end_time-start_time)
# sum=0
# l1=l.copy()
#
# n=len(l1)
# value=0
# for i in range(n):
#     for j in range(i+1,n):
#         if l[i]+l[j]==sum:
#             print((l[i],l[j]))

#
# import itertools as it
# 'triplet'
# l=[2,3,4,-9,-7,0,-3,7,-2,9]
# su=0
# n=len(l)
# for i in range(n):
#     for j in range(i+1,n):
#         for k in range(j+1,n):
#             if l[i]+l[j]+l[k]==su:
#                 print((l[i],l[j],l[k]))
# x=list(it.combinations(l,3))
# # for i in range(len(x)):
# #     if sum(x[i]) == 0:
# #         print(x[i])
#
#
# # import itertools as it
# # #
# l=[5,9,3,11,34,34,56]
# #
# # ''' Measure the length of given list and dived it into two parts d1 and d2'''
# #
# n=len(l)
# if n%2 ==0:
#     d1=n//2
#     d2=n//2
#
# else:
#     d1=(n//2)
#     d2=(n//2)+1
#
# '''make all combinations within two lists by lengths d1,d2 respectively '''
# x=(list(it.combinations(l,d1)))
# y=(list(it.combinations(l,d2)))
# print(x,y)
# values=0
# min_diff=max(l)
#
# '''iterate over each element in both lists and compare the the difference of sum of individual with
#  minimum difference make sure to avoid duplicates (by using sets)  '''
# for i in range(len(x)):
#     for j in range(len(y)):
#         if set(l) - set(x[i]) == set(y[j]):
#          if abs(sum(x[i])-sum(y[j]))<min_diff and abs(sum(x[i])-sum(y[j]))!=0 :
#             min_diff= abs(sum(x[i])-sum(y[j]))
#             values=(x[i],y[j])
# print(values,min_diff)
# #
# def check(l1,l2):
#     if sum(l1)-sum(l2)==min_diff:
#         print("True")
#     else:
#         print("false")
# check([5,9,3],[11,34,34,56])