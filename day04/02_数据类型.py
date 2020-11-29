'''
Pandas的一维数据类型Series
Series是一种类似于一维数组的对象，数据+索引组成，如果没有指定索引，
Series会自动的添加数字索引，功能类似于Pyhton的字典，
但是会做到很多python原生做不到的事情
'''
import pandas as pd

# 列表转化
li = [4, 2, 3, 6, 5, 'hello', 8, 4, 6]
# 无指定索引，系统添加的索引从0开始
# 如果数据类型不同，那么值的数据类型是Object
a = pd.Series(li)
print(a)
# 自己指定索引数量要对应
b = pd.Series(li, index=['a', 'b', 'c', 'e', 'f', 'g', 'h', 'i', 'j'])
print(b)
# 字典创建Series
d = {
    'name': '小龙人',
    'age': '18',
    'gender': 'unknown'
}
x = pd.Series(d)
print(x)
