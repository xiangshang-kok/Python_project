import matplotlib.pyplot as plt
import numpy as np
x = [4, 6, 2, 8]
plt.pie(x, autopct='%.1f%%', labels=['a', 'b', 'c', 'd'],
        explode=[0, 0, 0, 0.1],
        shadow=True
        )

plt.show()
