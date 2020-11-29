import pandas as pd

s = pd.Series([3, 2, 4, 6, 4])

# 修改
s[0] = 10
print(s)
print('->->->->->->->->->->\n\n->->->->->->->')
# 添加元素
s[5] = 1212121
print(s)
print('->->->->->->->->->->\n\n->->->->->->->')

# 删除元素
# inplace=False
# 当inplace为False的时候，删除元素不操作原来的Series
# 而是产生一个新的结果
# a=s.drop(5)
# print(a)

# inplace为True则修改原Series
s.drop(5, inplace=True)
print(s)
