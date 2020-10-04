import matplotlib.pyplot as plt 
import matplotlib.pyplot as pt 
import numpy as np 
import matplotlib.pyplot as py
import matplotlib.patches as patch

a = patch.Rectangle((20,-15), width=40, height=13, facecolor='white', edgecolor='grey')
b = patch.Rectangle((20,-2), width=40, height=13, facecolor='red', edgecolor='grey')
c = patch.Rectangle((-25,-13), width=5, height=22, facecolor='red')
d = patch.Rectangle((-26,-15), width=7, height=2, facecolor='red')
e = patch.Rectangle((-26,9), width=7, height=2, facecolor='red')
m,n = py.subplots()
n.add_patch(a)
n.add_patch(b)
n.add_patch(c)
n.add_patch(d)
n.add_patch(e)
py.axis('equal')
py.title('Indonesian',fontweight ="bold") 

t = np.arange(0,2*np.pi, 0.1) 
x = 16*np.sin(t)**3 
y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t) 
plt.plot(x,y) 
plt.show()
