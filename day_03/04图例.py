import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2*x+1
line1, = plt.plot(x, y, color='red')
y0 = x**2
line2, = plt.plot(x, y0, color='blue')
# 图例
# 第一种
#       plot中有一个属性叫做lable
#line2=plt.plot(x, y0, color='blue', label='2x+1')
# plt.legend()

# 第二种
# plot会返回该线条的对象   best自动选取数据少的区域加图例
# 如果需要这个对象进行图例操作，那么需要在在截取的变量后面加‘，’举例
# line,=plt.plot()


plt.legend(handles=[line1, line2], labels=['2x+1', 'x**2'], loc='best')
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_color(None)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.show()
