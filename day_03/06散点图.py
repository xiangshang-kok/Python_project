# 单组数据，查看数据的分布情况
# 多组数据，数据之间的关系
import matplotlib.pyplot as plt
import numpy as np
# x = [1, 2, 3, 4, 5, 6]
# y = [2, 3, 8, 6, 2, 9, ]
# plt.scatter(x, y,
#             marker='*',  # 点的样式
#             # s=1000,  # 点的大小
#             s=[50, 26, 1000, 56, 89, 96],
#             color='red'
#             )
# normal :指定正态分布
# randint:随机整数
# random: 0~1随机小数
# rand:0~1均匀分布
# randn:标准正态分布
x = np.random.normal(0, 1, 1024)
y = np.random.normal(0, 1, 1024)
t = np.arctan2(y, x)
plt.scatter(x, y, s=75, c=t, alpha=0.5)  # cmap=rainbow,Dark2
plt.xlim(-1.5, 1.5)
plt.ylim(-1.5, 1.5)
plt.show()
