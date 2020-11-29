import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
ts = pd.Series(np.random.randn(1000),
               index=pd.date_range('1/1/2020', periods=1000)
               )

ts = ts.cumsum()   # 累加
plt.rcParams['font.family'] = ['SimHei']
plt.rcParams['axes.unicode_minus'] = False
# matplotlib画图
#plt.plot(ts.index, ts.values)
# pandas画图
# kindle:bar pie....
ts.plot()

plt.show()
