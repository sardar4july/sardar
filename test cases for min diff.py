import sys
def min_array(arr,n):
    arr.sort()
    min_diff=sys.maxsize
    l=[]
    for i in range(1,n):
        arr1=arr[:n-i]
        arr2=arr[n-i:]
        f_arr1=sum(arr1)
        s_arr2=sum(arr2)
        diff=abs(f_arr1-s_arr2)
        l.append([arr1,arr2,diff])
        if diff<min_diff:
            min_diff=diff
            final_arr1=arr1
            final_arr2=arr2

    return min_diff,final_arr1,final_arr2,l
lst=[5,6,3,34,67,900,600]
n=len(lst)
lst2=sorted(lst)
print('min',min_array(lst2,n))
a=min_array(lst,n)
print("a",a[3])
b=a[3]
print('b[0]',b[0])
b.sort(key=lambda x:x[2])
print('soretd b',b)
if a[0]==b[0][2]:
    print("yes")
else:
    print("no")
