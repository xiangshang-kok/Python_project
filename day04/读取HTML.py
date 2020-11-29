import pandas as pd
# HTML 有一个table标签，专门做表格的标签
# pandas读取html的时候就是在读取table标签内的信息
# table标签内有tr表示行，tr中有若干个td表示列
table = pd.read_html(
    'http://www.stats.gov.cn/tjsj/zxfb/202010/t20201030_1797711.html')
# 如果有多张表，用下标的方式进行选择
print(table[1])
t = table[1].iloc[3:]
t.to_csv('./day04/resources/foo1.csv', index=False, header=False)
