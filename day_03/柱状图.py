import matplotlib.pyplot as plt
import numpy as np
x = np.array([1, 2, 3, 4, 5])
math = [98, 65, 78, 100, 3]
english = [78, 85, 98, 36, 45]
plt.bar(x, math, color='red', alpha=0.5, width=0.2)
plt.bar(x+0.2, english, color='blue', alpha=0.5, width=0.2)
plt.xticks(np.arange(5)+1.1, x, fontsize=16)
plt.show()
