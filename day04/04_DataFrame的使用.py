import pandas as pd
import numpy as np
# DataFrame是一个二维数据
# 二维数据具有行和列
# DataFrame具有两个索引：行索引(index)，列索引(columns)
# 创建默认索引的DataFrame
d = pd.DataFrame([[1, 2, 3], [4, 5, 6, ], [7, 8, 9]])
print(d)
# 创建自定义索引的DataFrame
d = pd.DataFrame([[1, 2, 3], [4, 5, 6, ], [7, 8, 9]],
                 index=['a', 'b', 'c', ],
                 columns=['A', 'B', 'C']
                 )
print(d)
# numpy创建
d = pd.DataFrame(
    # 将0~9重新排列为2行5列
    np.arange(10).reshape(2, 5)
)
print(d)
print('&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&&')
# 字典的二维数据
# 字典的第二纬度，如果是列表和字典的话，必须等长
# 如果是Series对象的话，不要求等长，其余值用NaN(not a number)代替
di = {
    'name': pd.Series(['a', 'b', 'c']),
    'age': pd.Series([15, 34, 26, 56])
}
d = pd.DataFrame(di)
print(d)
