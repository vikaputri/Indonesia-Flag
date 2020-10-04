import numpy as np
import matplotlib.pyplot as py
import matplotlib.patches as patch

a = patch.Rectangle((0,1), width=20, height=5, facecolor='white', edgecolor='grey')
b = patch.Rectangle((0,6), width=20, height=5, facecolor='red', edgecolor='grey')
m,n = py.subplots()
n.add_patch(a)
n.add_patch(b)

py.axis('equal')
py.show()
