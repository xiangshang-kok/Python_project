import pandas as pd
import numpy as np

value = [
    ['李华', 'male', 18, 150, 90, '北京故宫', 60],
    ['金花', 'female', 80, 155, 60, '东京汴梁', 58],
    ['西门', 'male', 14, 175, 30, '东京故宫', 60],
    ['武大', 'male', 18, 150, 100, '窗外', 12],
    ['武紧', 'male', 80, 180, 90, '老虎洞', 80],
]
a = pd.DataFrame(value, index=[1, 2, 3, 4, 5],
                 columns=['name', 'sex', 'age',
                          'height', 'weight', 'add', 'score']
                 )
print(a)
# 1.常规属性
# 获取每一列数据的数据类型
print(a.dtypes)  # DataFrame
# 获取行索引
print(a.index.values)
print('&&&&&&&&&&&&&&&&&')
# 获取列索引.values获取索引值
print(a.columns.values)
print('%%%%%%%%%%%%%%%%%%%%%%')
print('>>>>>>>>>>>>>>>>>>>>>>>>')
# 2、整体数据情况
# 整体信息
print(a.info())
print('%%%%%%%%%%%%%%%%%%%%%%')
# 整体统计指标
print(a.describe())
# 获取前3行
print(a.head(3))
print('>>>>>>>>>>>>>>>>>>>>')
# 获取后3行
print(a.tail(3))
print('<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

# 3、获取数据————内容查询
# 列：
#   查询一列
print(a['add'])
print('->->->->->->->->->->->')
# 查询多列
print(a[['name', 'add']])
print('->->->->->->->->->->->')
# 查询多行--->不推荐
print(a[0:1])
print('&&&&&&&&&&&&&&&')
# pandas专属查询方式---->优化
# 查询行：
# loc:是根据索引来查找
# iloc：根据行号来查找
# 查单行
print(a.loc[1])
print('->->->->->->->->->->->')
print(a.iloc[0])

# 查单列
# [a:b,c:d]
# a行到b行
# c列到b列
print('->_______')
print(a.loc[:'address'])
print(a.iloc[:, 5])
print('$$$$$$$$$$$$$$$$$$$$$$$$$$$')
# 查多行
print(a.loc[[1, 3]])
# 查多列
print(a.loc[:, ['add', 'name']])
print('***********************\n\n\n\n*************')
# 4、过滤查询
print(a.loc[2])
print(a['score'] < 60)
print(a.loc[a['score'] < 60, ['name', 'add']])
print('***********************\n\n\n\n*************')
# 查询低于平均分的人，列出成绩和地址
print(a.loc[a['score'] < a.mean()['score'], ['name', 'add']])
print('***********************\n\n\n\n*************')
# isin函数
# 输出所有地址在add的人
add = ['老虎洞', '北京故宫']
x = a['add'].isin(add)
print(a.loc[x])
