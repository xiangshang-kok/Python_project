import matplotlib.pyplot as plt
import numpy as np
#
x = np.linspace(0, 66, 33)
y = np.linspace(0, 36, 18)
X, Y = np.meshgrid(x, y)

H = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 917, 1000, 958, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 0, 0, 1000, 982, 893, 542, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 1000, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 1000, 1000, 982, 900, 568, 507, 500, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 1000, 1000, 1000, 1000, 0, 0, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 1000, 982, 894, 516, 284, 440, 489, 500, 500, 500, 0],
     [0, 0, 0, 0, 0, 1000, 1000, 982, 964, 982, 1000, 0, 0, 0, 0, 0, 0, 0,
         0, 0, 0, 1000, 1000, 946, 556, 147, 97, 266, 479, 500, 500, 500, 0],
     [0, 0, 0, 0, 1000, 1000, 982, 911, 643, 893, 929, 946, 1000, 0, 0, 0, 0,
         0, 0, 0, 1000, 1000, 982, 893, 485, 95, 91, 416, 489, 500, 500, 0, 0],
     [0, 0, 0, 0, 1000, 982, 911, 589, 536, 554, 571, 607, 946, 1054, 1036, 1000, 1000,
         1000, 1000, 1000, 1000, 982, 911, 579, 431, 99, 200, 447, 500, 500, 0, 0, 0],
     [0, 2083, 2500, 1357, 1071, 964, 661, 589, 643, 750, 750, 768, 982, 1786, 1214, 1036,
         1000, 1000, 1000, 1000, 1000, 936, 569, 434, 212, 105, 133, 0, 0, 0, 0, 0, 0],
     [0, 0, 2917, 2607, 1429, 1268, 1232, 1214, 1357, 2429, 1964, 1893, 2482, 2554,
         1893, 1214, 1107, 1036, 1000, 982, 946, 839, 302, 92, 39, 8, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 2167, 2833, 2750, 2714, 2714, 2714, 2786, 2893, 2821, 2250, 2250, 2250,
         2143, 2000, 1786, 1107, 1000, 946, 611, 471, 156, 34, 16, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 2893, 3000, 3000, 3000, 3000, 3000, 2964, 2893, 2857, 2857, 2857,
         2750, 1964, 1143, 1000, 929, 529, 186, 103, 31, 18, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 2833, 2964, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000, 3000,
         2821, 1900, 1021, 914, 886, 486, 143, 89, 38, 32, 17, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 2833, 2893, 2964, 3000, 3000, 2964, 2893, 2857, 2857, 2857,
         2643, 1264, 521, 486, 843, 300, 171, 149, 110, 174, 46, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 2833, 2857, 2857, 2833, 0, 0, 2143, 2143, 1964,
         1150, 914, 886, 829, 500, 443, 440, 423, 355, 43, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2000, 2000, 1857, 1143,
         1000, 911, 393, 439, 457, 486, 450, 118, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2000, 2000, 1839, 1089, 929,
         819, 224, 134, 172, 400, 382, 118, 75, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1875, 1625, 0,
         0, 460, 96, 28, 10, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 31, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

# 填充颜色
plt.contourf(X, -Y, H, cmap='hot')

# 画等高线

lin = plt.contour(X, -Y, H, 4, color='black', linewidth=0.2)
# 显示等高值
plt.clabel(lin, inline=True, fontsize=12)
plt.show()
