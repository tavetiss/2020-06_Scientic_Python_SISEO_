# A first simple example with Python
import numpy as np # Numpy: matrices and vectors in Python like in Matlab
from matplotlib import pyplot as plt # Matplotlib/Pyplot: library for plotting


a = 5 
b = "Hello"
l = [1,2,4, "Thing"] # A python List
l2 = [3,4,5]

# Numpy 
a = np.array(l2) # Array is like a list but easier for math and faster
a1 = np.linspace(0., 1., 11)
a2 = np.arange(10)
   

# Simple function in Python
d = 11

def func(x, b = 1., c = 1., d = 5.):
    """
    A mathematical function: y = exp(x / b) * cos(c * x) 
 
    Args:
        * x: a value
        * b: another value
        * c: ...
    """
    #d = 5 # Some test with local vs global variables
    y = np.exp( x / b) * np.cos(c * x) 
    #print("x=", x, "b=",b , "c=", c, "d=", d)
    return y


# Plot a function with matplotlib
x = np.linspace(0., 10., 1001)
y = func(x)

fig = plt.figure()
plt.plot(x, y)
plt.grid()
plt.xlabel("$x$ values")
plt.ylabel(r"$y=\exp(\frac{x}{b}) \times \cos(xc)$")
plt.show()




