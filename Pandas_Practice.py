import pandas as pd
# d={1:['a','b','c'],
#    2:['e','f','g'],
#    3:['x','y','z']}
# df=pd.DataFrame(d)
# print(df)
df1 = ({'rating': [90, 85, 82, 88, 94, 90, 76, 75],
                   'points': [25, 20, 14, 16, 27, 20, 12, 15]}
                  )
df2 = pd.DataFrame({'assists': [5, 7, 7, 8, 5, 7],
                   'rebounds': [11, 8, 10, 6, 6, 9]},
                   index=list('acdgmn'))
# s=pd.merge(df1,df2,left_index=True, right_index=True)
# s=pd.concat([df1, df2],axis=1)
# print(s)
# s=pd.DataFrame.from_dict(df1,orient='index')
# print(s)
# print(df2['assists'].count())
print(df2.iloc[0:3,0:2])
