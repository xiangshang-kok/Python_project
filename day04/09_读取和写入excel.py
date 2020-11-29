import pandas as pd
# 读取excel
# 默认读取第一张表
e = pd.read_excel('./day04/resources/output.xlsx')
print(e)
# 可以读取到指定的表格 sheet_name=None读取文件中的所有的表
e = pd.read_excel('./day04/resources/output.xlsx', sheet_name='Sheet1')
print(e)
# 可以选择指定的表
print(e['abc'])
# 其他的属性和读取CSV中的属性是一致的
