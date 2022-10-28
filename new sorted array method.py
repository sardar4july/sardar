import sys
import itertools as it
final_arr1,final_arr2=0,0
def min_array(arr):
    arr.sort()
    # min_diff=sys.maxsize

    n = len(arr)
    if n % 2 == 0:
        d1 = n // 2
        d2 = n // 2

    else:
        d1 = (n // 2)
        d2 = (n // 2) + 1
    l = []
    '''make all combinations within two lists by lengths d1,d2 respectively '''
    x = (list(it.combinations(arr, d1)))
    y = (list(it.combinations(arr, d2)))
    # print(x, y)
    values = 0
    min_diff = max(arr)
    '''iterate over each element in both lists and compare the the difference of sum of individual with
     minimum difference make sure to avoid duplicates (by using sets)  '''
    for i in range(len(x)):
        for j in range(len(y)):
            # l.append([x[i],y[j],abs(sum(x[i]) - sum(y[j]))])
            if set(arr) - set(x[i]) == set(y[j]) and abs(sum(x[i]) - sum(y[j])) != 0:
                l.append([x[i], y[j], abs(sum(x[i]) - sum(y[j]))])
                if abs(sum(x[i]) - sum(y[j])) < min_diff :
                    min_diff = abs(sum(x[i]) - sum(y[j]))
                    # l.append([x[i], x[j], min_diff])
                    values = (x[i], y[j])


            final_arr1=x[i]
            final_arr2=y[j]
    print("values,min diff", values, min_diff)

    return min_diff,final_arr1,final_arr2,l

lst=[5,9,3,11,34,34,56]
# n=len(lst)
# lst2=sorted(lst)
# print('min',min_array(lst2))
a=min_array(lst)
# print("a",a[3])
b=a[3]
# print('b[0]',b[0])
b.sort(key=lambda x:x[2])
# print('soretd b',b)
def testing(arr1,arr2):

    if a[0]==b[0][2]:
        print("yes")
    else:
        print("no")

testing(final_arr1,final_arr2)