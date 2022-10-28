import requests
# print(requests.__version__)
# # print(dir(requests))
# print(requests.__author__)
# res=requests.get('https://google.com/')
# print(res.status_code)
# res=requests.get('https://amazon.com/')
# print(res.status_code)
# res=requests.get('https://www.google.com/')
# print(res.text)
# print(res.content)
# print(res.raw)
# print(res.encoding)
# r = requests.get('https://api.github.com/events')
# print(r.raw)
# resp=r.headers
# print(resp)
# print('timeout=0.001')
# try :
#     r = requests.get('https://api.github.com/events')
#     print(r.text)
# except requests.exceptions.RequestException as e:
#     print(e)
#
# print('time out=1.0')
#
# try:
#     r=requests.get('https://api.github.com/events')
#     print(r.status_code)
# except requests.exceptions.RequestException as e:
#       print(e)
# import math
# l=[1,2,3,4,5]
# x=math.prod(l)
# new=[x//i for i in l ]
# print(new)
l=[5,1,1,5]
d=[[0 for i in range(2)]for j in range(5)]
# print(d)
d[0][0]=0
d[0][1]=l[0]
for i in range(1,len(l)):
    d[i][1]=d[i-1][0]+l[i]
    d[i][0]=max(d[i-1][1],d[i-1][0])

print((d))