import matplotlib.pyplot as plt
import numpy as np
from matplotlib import cm # Colormaps

def func(x,y):
    """
    A mapping
    """
    r = (x**2 + y**2)**.5
    return np.exp(-r/5) * (np.sin(x/2) + np.cos(2+y)*2)
     
x = np.linspace(-5., 5., 100)
y = np.linspace(-5., 5., 100)
X, Y = np.meshgrid(x,y)
Z = func(X, Y)
Z = np.where(Z<-1., np.nan, Z)
# CROSS SECTION
s = np.linspace(-5, 5., 200) # POSITION ON THE SECTION
theta = -45. # ANGLE OF THE CROSS SECTION [°]
xc = np.cos(np.radians(theta)) * s
yc = np.sin(np.radians(theta)) * s



fig = plt.figure()
ax = fig.add_subplot(1, 2, 1) # LEFT PLOT
plt.title("Mapping")
plt.contour(X, Y, Z, 20, colors = "black")
plt.contourf(X, Y, Z, 20, cmap = cm.copper)
cbar = plt.colorbar(orientation = "horizontal")
cbar.set_label("Altitude, $z$ [m]")
plt.xlabel("Position, $x$ [m]")
plt.ylabel("Position, $y$ [m]")
#plt.grid()
plt.plot(xc, yc, "r-", label = "cross section")
plt.legend()

ax = fig.add_subplot(1, 2, 2)
 

plt.show()


"""
fig = plt.figure()
plt.plot(np.random.rand(10))
plt.grid()
plt.savefig("plot.pdf")
plt.close("all") # Close all figures that are not shown
"""
