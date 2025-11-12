import statsmodels.formula.api as smf
import pandas as pd 
import matplotlib.pyplot as plt
coeffs = np.polyfit(x,y,2)
plt.scatter(x,y)
plt.plot(x, np.polyval(coeffs,x))
plt.show()