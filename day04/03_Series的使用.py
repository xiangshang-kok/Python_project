import pandas as pd

class1 = pd.Series(
    [65, 48, 23, 45, 7],
    index=['black', 'pink', 'purple', 'orange', 'green']
)

print(class1)
# 获取所有的值，结果是一个numpy.ndarray类型
print(class1.values)
print(type(class1.values))
# 获取所有的索引，结果是一个index对象 <class 'pandas.core.indexes.base.Index'>
print(class1.index)  # 不可直接进行计算
print(type(class1.index))
print(class1.index.values)  # numpy.ndarray类型，可以直接进行计算
print("######################################################")
# 获取值
# 1，根据索引获取值
#   索引，序号
# 查询单个值
print(class1['black'], class1[0])
# 查询多个值
print(class1[[0, 3]])
print(class1[['black', 'orange']])
# 2，根据条件反查索引
