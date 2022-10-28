# l=[3,3,3,3,3,3,3,3,3,1]
# arr_1=l[0:3]
# arr_2=l[3:6]
# arr_3=l[6:]
# print(sum(arr_1))
# print(sum(arr_2))
# print(sum(arr_3))
# if sum(arr_1)!=sum(arr_2)  and sum(arr_1)!=sum(arr_3) :
#     print("arr_1","is diff")
# elif sum(arr_2)!=sum(arr_1) and sum(arr_2)!=sum(arr_3):
#     print("arr_2","is diff")
#
# else:
# #     print("arr 3 is diff")
# def rec_max(l):
#    if len(l)==1:
#       return l[0]
#    else:
#       m=rec_max(l[1:])
#       return m if m<l[0] else l[0]
# print(rec_max([2,4,5,22,1]))


def sort_cards(cards,query):
    position=0
    while position<len(cards):
        if cards[position] == query:
            return position
        position+=1
    return -1
# print(sort_cards([1,2,3,4,5],3))
test_cases=[]

tests={'input':{'cards':[1,2,3,4,5],
                'query':3},
       'output':2}
print(sort_cards(**tests['input']) == tests['output'])


# s='python'
# n=len(s)
# for  i in range(1,n*2):
#     if i<=n:
#      print(s[:i])
#
#     else:
#         print(s[:n-i])




















