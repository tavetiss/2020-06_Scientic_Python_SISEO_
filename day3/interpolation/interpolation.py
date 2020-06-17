import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import pandas as pd

# DATA1:
x1 = np.random.rand(20) * 4
y1 = np.cos(x1)

# DATA1:
x2 = np.random.rand(20) * 4
y2 = np.cos(x2)*1.1 + 0.1

# INTERPOLATION
x = np.linspace(0., 4., 100) # Interpolation grid
f1 = interpolate.interp1d(x1, y1, kind = "linear", bounds_error=False)
f2 = interpolate.interp1d(x2, y2, kind = "linear", bounds_error=False)

# NEW DATASET
df = pd.DataFrame(index = x)
df["y1"] = f1(x)
df["y2"] = f2(x)
df.to_excel("data.xls")


plt.figure()
plt.plot(x1, y1, "or", label = "data1")
plt.plot(x2, y2, "bs", label = "data2")
plt.plot(x, f1(x), "r+-", label = "interp1")
plt.plot(x, f2(x), "b+-", label = "interp2")
plt.grid()
plt.legend(loc = "best")
plt.show()

