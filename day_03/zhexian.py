import matplotlib.pyplot as plt
import numpy as np
# plt.plot()
# X:x坐标的点 列表
# Y：y坐标的点 列表
# color：颜色
# linestyle:线的样式
# linewidth:线宽
# maker:将点标注出来
# makersize:设置标注的大小
# makerfacecolor:标注的颜色
# alpha:（0~1）设置透明度


# 将-1~~1分成20份
x = np.linspace(-1, 1, 20)
y = 2*x+1
plt.plot(x, y, color='red', linestyle='--',
         linewidth=2, marker="*", markersize=10)
y0 = x**2
plt.plot(x, y0, color='blue', linestyle="-")
plt.show()
