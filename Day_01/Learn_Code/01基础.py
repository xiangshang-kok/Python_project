import copy
print("123")
a = 2
b = 3
# print语句可以输出多个数据，用，隔开
# 中间的分隔符可以用sep=分割这样的
# 属性进行操作，sep必须在最后
print(a, b, sep=",")
name = "001"
print("%s%d" % (name, a))
# ID可以查看一个变量的内存地址，相同的数内存地址相同
print(id(a), id(b))

# 常见的数据类型
# 整数
print(bin(90))
print(oct(90))
print(hex(90))
# 字符串-单引号双引号都可以
# 布尔值 0是假  1是真

# python运算符
'''
算术运算符 
+ - * /(结果是小数) % **(次方)  //(结果是整数)  
比较运算符 print(1<a<3)
逻辑运算符 or and not
赋值运算符 += -=

分支语句
if 条件：
    语句
循环语句
while 循环条件：
    循环体
break  continue
for 循环

for 变量 in 集合元素：


for i in range(a):
range(a)
range(a,b)
range(a,b,c)a 起始，b 结尾 c 步长

列表
    []中可以写任意多个值
    添加元素
    list.append()
    extend(子列表)
    +   list+list (不改变原来列表)
    获取元素
    list[索引]
    插入元素
    insert(下标，元素)
    删除元素
    pop()：末尾弹出元素
    remove(元素):移除指定元素
    del list[下标]
    del 列表：删除整个列表并释放内存空间
    del 列表[a:b]
for i in list:
    print(i)
for i in range(list.__len__):
    print(list[i])
max(列表)&min(列表)
sum(列表)
列表.index(元素)  该元素在列表中的位置

集合  {}
    特点：无序不重复
#空集合 d=set()
添加元素  集合.add(元素)
移除元素  集合.remove(元素)
清空集合  集合.clear()
判断一个元素在不在集合中   元素 in 集合
计算集合元素个数 len(集合)   集合.__len__()

元组:()
    有序可重复  
    元组的元素一旦定义不能修改
    元组变为列表  list(元组)
    列表变为元组  tuple(列表)

字典
key 和 value组合而成
无序  key不能重复  value 可以重复
字典的底层数据结构---->哈希表
dic = {1:'one',2:'two',3:'three',4:'four',5:'five'}
取元素
字段[key] 结果是value
添加或者修改值   dic[6]='six'  dic[1]='six'  
删除  del 字典[key]  del字典
遍历字典
    for i in dir:
        print(dic[k])
    for k,v in dir:
        print(k,v)




'''
s = {'apple', 'banana', 'cherry', 'orange', 'apple'}
print(s)


# 元组创建
y = (1, 2, 3)
y1 = 1, 2, 3
y2 = (1)
y3 = 1,

l1 = [1, 3, 2, [1, 5, 6]]
# 深拷贝 和 浅拷贝
# 浅拷贝
# 列表嵌套列表， 二级列表只复制地址值


# 深拷贝
# 列表嵌套列表， 二级列表重新开辟地址进行复制
l2 = copy.deepcopy(l1)
'''函数定义
def 函数名(参数列表):
    代码
参数列表：
    1.必须参数
        调用函数时必须传入的函数
    2.关键字参数

    3.默认参数
        默认参数必须在最后
    4.可变参数
        可变参的传值必须是键值对的传值
'''


def add1(name='TOm', sex='male'):
    print(name, sex)


def change(**kw):
    print(kw)


change(name='TOm', sex='01')
