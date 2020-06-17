import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm # Colormaps

x = np.linspace(0., 10., 200)
y1 = np.sin(2. * np. pi * x/4)
y2 = np.sin(2. * np. pi * x /8)
ylim = -1., 1


fig = plt.figure()
ax1 = fig.add_subplot(1, 2, 1) # LEFT PLOT
plt.plot(x, y1, "r-", label = "$y_1$")
plt.grid()
plt.ylim(*ylim)
plt.legend(loc = "best")
yticks = ax1.get_yticks()
plt.yticks(yticks, ["${0:.2f}$".format(t) for t in yticks] )


ax2 = fig.add_subplot(1, 2, 2) # RIGHT PLOT
plt.plot(x, y2, "b-", label = "$y_2$")
plt.grid()
plt.ylim(*ylim)
plt.legend(loc = "best")
yticks = ax2.get_yticks()
plt.yticks(yticks, ["" for t in yticks] )
ax2.invert_xaxis() # Inverts the x axis

plt.show()

