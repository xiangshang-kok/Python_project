import pandas as pd
import numpy as np

# None 和 np.nan
# Numpy缺失值
# numpy中，如果是None,进行计算会报错
# 如果是np.nan,进行计算结果是nan
b = np.array([2, 3, np.nan, 10, 12])
# print(b.sum())
# pandas缺失值
# 进行计算的时候可以计算出结果
b = pd.Series([2, 3, np.nan, 10, 12])
# print(b.sum())
c = pd.DataFrame([[1, 2, np.nan], [4, 3, 6], [np.nan, 7, 1]])

# 判断缺失值
# isnull() :是空返回True      notnull():不是空返回True

# 删除缺失值:
# dropna()
# 删除所有具有空值的行
a = c.dropna()
print(a)
# 删除所有具有空值的列
a = c.dropna(axis=1)
print(a)
# 填充缺失值
# fillna
# 填充默认值、向前填充、向后填充
a = c.fillna(0)
print(a)
a = c.fillna(method='ffill')  # ffill forward fill
print(a)
a = c.fillna(method='bfill')  # bfill back fill
print(a)
a = c.fillna(method='bfill', axis=1)
print(a)

data = pd.DataFrame(np.random.randn(1000, 4))
print(data)
# 把每一列的数据控制在-3和3之间

# 以第一列为例子  data[0]
# 查找所有列 >3或<-3的值
# np.sign(data)如果是正数返回1，负数返回-1
data[np.abs(data) > 3] = np.sign(data)*3
print(data[np.abs(data) > 3])
print(data.describe())
