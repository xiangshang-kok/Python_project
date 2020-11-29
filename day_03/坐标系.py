import matplotlib.pyplot as plt
import numpy as np
# 如果想一个脚本画多个窗口
# 就调用plt.figure(),在每一个画线前面添加该方法
# figsize=(8,5)设置窗口的大小


x = np.linspace(-3, 3, 50)
y = 2*x+1
#plt.figure(figsize=(8, 5))
plt.plot(x, y, color='red')
y0 = x**2
# plt.figure()
plt.plot(x, y0, color='blue')

# 更改坐标轴刻度的取值范围
# x:xlim
# y:ylim
plt.xlim((-3, 3))
plt.ylim((-2, 9))

# 设置坐标轴的说明文本
# X 轴的说明文本
# matplotlib本身不支持中文字体
# 因此要显示中文
# 第一种方式：
#   添加属性：fontproperties='字体'
# 第二种方式：
#   plt.rcParams['font.sans-serif']=['字体']
# 第一种方式的优先级最高

plt.rcParams['font.sans-serif'] = ['Kaiti']
#plt.xlabel('这是x', fontproperties='Kaiti')
plt.xlabel('这是x')
plt.ylabel('I am y')

# 添加大标题
plt.title('第一个Matplotlib的图表')
# 设置轴的小标
tick = [1, 2, 3, 4]
names = ['bad', 'good', 'best', 'worse']
plt.xticks(tick, names)
plt.show()
