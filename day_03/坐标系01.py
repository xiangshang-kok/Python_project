import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(-3, 3, 50)
y = 2*x+1
plt.plot(x, y, color='red')
y0 = x**2
plt.plot(x, y0, color='blue')
# 获取到坐标轴
# plt.gca()---->get current axis
ax = plt.gca()
# 坐标脊
# ax.spines[]
# top left right bottom
# 隐藏坐标脊
# 第一种
ax.spines['top'].set_visible(False)
# 第二种方式：
ax.spines['right'].set_color(None)
# 绑定坐标脊
# 将x坐标轴与bottom坐标脊绑定
ax.xaxis.set_ticks_position('bottom')
# 将y坐标轴与left坐标脊绑定
ax.yaxis.set_ticks_position('left')

# 更改坐标脊位置
#ax.spines['bottom'].set_position(('date', 0))
ax.spines['bottom'].set_position(('data', 0))
plt.show()
