import matplotlib.pyplot as plt
import numpy as np
# 导入3D包
from mpl_toolkits.mplot3d import Axes3D
fig = plt.figure()
# 将2D坐标轴转换成3D坐标轴
ax = Axes3D(fig)
# 从-4~4每隔0.25产生一个数据
x = np.arange(-4, 4, 0.25)
y = np.arange(-4, 4, 0.25)
# 做网格
X, Y = np.meshgrid(x, y)
r = np.sqrt(X**2+Y**2)
# 计算高度
Z = np.sin(r)
# rstride =
# cstride =
ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap='hot')

ax.set_zlim(-2, 2)
# 制作投影
# zdir表示要做哪一个轴的投影
ax.contourf(X, Y, Z, zdir='z', offset=-2, cmap='rainbow')
plt.show()
