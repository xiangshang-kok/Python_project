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
print('->->->->->->->->->\n\n->->->->->->->->')

# 修改列
a['sex'] = ['man', 'woman', 'man', 'man', 'man']
print(a)
print('->->->->->->->->->\n\n->->->->->->->->')

# 添加行，所有元素都是111
# 1.如果是一个数的话，所有的列都添加成这个数
# 2.如果是一个列表，那么列表的元素个数必须和列数相匹配
# 3.如果是一个Series对象，那么索引的名字必须和列索引的名字相同，
# 如果不相同传入的值就是NaN
a.loc[6] = 111
# 内容要对应完全
a.loc[7] = pd.Series(['娜扎', 'woman', '6', '90', '30', '陈塘关', 88],
                     index=['name', 'sex', 'age', 'height',
                            'weight', 'add', 'score']
                     )
print(a)
print('->->->->->->->->->\n\n->->->->->->->->')
# 添加列
a['phone'] = 123456
print(a)
print('->->->->->->->->->\n\n->->->->->->->->')

# 删除
a.drop(6, inplace=True)
print(a)
print('->->->->->->->->->\n\n->->->->->->->->')
# 默认是删除行，如果要删除列那么添加属性axis=1
a.drop('phone', axis=1, inplace=True)
print(a)
