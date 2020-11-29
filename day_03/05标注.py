import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 9, 100)
y = np.sin(x)
plt.plot(x, y)
x0 = 2
y0 = np.sin(x0)
# 画点
plt.scatter(x0, y0, s=80, color='blue')
plt.plot([x0, x0], [y0, 0], linewidth=3, linestyle='--')
#######################################################
# 文字
# annotate
plt.annotate('%.1f=sin(x)' % y0,  # 输出的文字
             xy=(x0, y0),  # 标注的位置
             xycoords='data',  # 标注的依据
             xytext=(+30, -30),  # 文本偏移量
             textcoords='offset points',  # 文本偏移位置参考系
             fontsize=16,  # 字号
             arrowprops=dict(arrowstyle='->',
                             connectionstyle='arc3, rad=0.3')
             )
ax = plt.gca()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_color(None)
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.spines['bottom'].set_position(('data', 0))
ax.spines['left'].set_position(('data', 0))
plt.show()
