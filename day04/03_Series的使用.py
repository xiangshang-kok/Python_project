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
# 根据索引
# 查询单个值
print(class1['black'], class1[0])
# 查询多个值
print(class1[[0, 3]])
print(class1[['black', 'orange']])
# 切片
print(class1[1:4])  # 包前不包后，包含1不包括4
print(class1['pink':'orange'])  # 使用自定义的索引，包前又包后

# 2，根据条件反查索引
# 举例：查询所有值小于60的索引
# 普通方法
# for i in class1:
#     if i<60:
#         print(i)
# pandas方法
print('************************')
# x = [True, False, False, False, False]
# print(class1[x])
# print(class1 < 60)
print(class1[class1 < 60])
# 给每个学生加5分
# 没有改变源数据，而是生产了新的Series对象
aa = class1+5
print(class1+5)
print(aa)
# 计算总分
print(class1.sum())  # np.sum(class1)
