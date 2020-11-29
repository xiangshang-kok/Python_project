import matplotlib.pyplot as plt
# 第一种方式
# plt.subplot(行,列,位置)
# plt.subplot(2, 1, 1)

# plt.subplot(2, 3, 4)

# plt.subplot(2, 3, 5)

# plt.subplot(2, 3, 6)


# 第二种方式
import matplotlib.gridspec as gridspec
# ax1 = plt.subplot2grid((3, 3),  # 整个窗口分为几行几列
#                        (0, 0),  # 起始位置
#                        colspan=3,  # 占了多少列
#                        rowspan=1,  # 占了多少行
#                        )
# ax1.set_title

# 第三种方式
# 将整个窗口分为三行三列
# [:,:]
# ,前表示行，如果只有一个数字，表示占据这一行
# 如果有：表示一个区间如果0:2占据0行和第一行，包前，不包后
# ，后表示列，语法格式与行相同
gs = gridspec.GridSpec(3, 3)
plt.subplot(gs[0, :])
plt.subplot(gs[1, :2])
plt.subplot(gs[1:, 2:])


plt.show()
