# pandas可以存取多种类型的文件
# 文本类  csv json excel pkl hdf5,webAPI HTML

# 读取CSV
# Comma-Separated Values
# 纯文本的形式来存储表格样式数据的文件
# 数据与数据之间用，隔开
# 读取
import pandas as pd
data = pd.read_csv(
    './day04/resources/ceshi.csv',
    encoding='gbk'
)
print(data)
print('->->->->->->->->->\n\n->->->->->->->->')
# 读取
data1 = pd.read_csv('./day04/resources/foo.csv',
                    # 列索引
                    # header=1,  # 列索引的默认行数
                    # header=None,  # 不将第一行作为列索引，会产生默认索引
                    # 添加列索引和header=0配合使用
                    # names=['x', '姓名', '性别', '年龄', '身高',
                    #       '体重', '地址', '分数']  # 添加列索引
                    # 行索引
                    # index_col=None,#不将第一列作为行索引
                    # index_col='name',  # 指定一列作为行索引
                    # index_col=['name', 'age']  # 自定义多列作为行索引
                    # 读取指定的行和列
                    # usecols=[0, 4, 3],  # 读取指定列，默认索引
                    # usecols=['name', 'age'],  # 读取指定的列，自定义索引
                    # nrows=3,  # 读取的行数，前几行
                    # skiprows=2,  # 从表格的第几行开始计算
                    # skiprows=[2, 4],  # 要跳过的行数
                    # skipfooter=2,  # 从末尾计算忽略多少行
                    # engine='python',# c更快，python功能更多

                    # 替换空值
                    na_values=['male'],  # 将所有带有male的字符替换为空值
                    keep_default_na=False,  # 默认True，系统自带的空值和自定义的空值，False只会使用自定义的空值
                    encoding='utf-8'


                    )
print(data1)
print('->->->->->->->->->\n\n->->->->->->->->')

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

# 写入CSV
a.to_csv(
    './day04/resources/foo1.csv',
    index=False,  # 不存储行索引
    header=False,  # 不存储列索引
    columns=['name', 'sex', 'add'],  # 只保存指定的列

)
