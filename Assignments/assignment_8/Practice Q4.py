import statsmodels.formula.api as smf
import pandas as pd 
import matplotlib.pyplot as plt
import numpy as np
coeffs = np.polyfit(x,y,2)
plt.scatter(x,y)
plt.plot(x, np.polyval(coeffs,x))
plt.show()

 
x = np.linspace(0, 10, 20)
y = 3*x**2 + 2*x + 1 + np.random.randn(20)*10

x_fit = np.linspace(min(x), max(x), 100)
y_fit = np.polyval(coeffs, x_fit)
plt.plot(x_fit, y_fit)


# Fit quadratic model
coeffs = np.polyfit(x, y, 2)

# Scatter plot of data
plt.scatter(x, y, label="Data", color='blue')

# Correct line plot (smooth, ordered x-values)
x_fit = np.linspace(min(x), max(x), 100)
y_fit = np.polyval(coeffs, x_fit)
plt.plot(x_fit, y_fit, color='red', label="Quadratic Fit")

plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.title("Quadratic Fit Correction")
plt.show()

# Read CSV (replace filename with your actual file)
df_weather = pd.read_csv("delhi_weather_2017.csv", parse_dates=["time"])

# Plot both columns on the same axes
df_weather.plot(
    x="time",
    y=["temperature", "wind_speed"],
    title="Delhi Weather 2017: Temperature and Wind Speed"
)

df_conv = pd.read_csv("conversion_rates.csv", parse_dates=["time"])

# Compute percentage growth (non-dimensional)
df_conv["EUR_USD_growth"] = df_conv["EUR_USD"] / df_conv["EUR_USD"].iloc[0] * 100
df_conv["GBP_USD_growth"] = df_conv["GBP_USD"] / df_conv["GBP_USD"].iloc[0] * 100

# Plot both growth curves
df_conv.plot(
    x="time",
    y=["EUR_USD_growth", "GBP_USD_growth"],
    title="Percentage Growth of Conversion Rates (Base = 100%)"
)

df_conv["EUR_high"] = df_conv["EUR_USD"] > 1.1

# Display first few rows
df_conv.head()

plt.plot(df_conv["time"], df_conv["EUR_USD"], label="EUR/USD", color='blue')
plt.fill_between(
    df_conv["time"],
    df_conv["EUR_USD"],
    where=df_conv["EUR_high"],
    color='red',
    alpha=0.3,
    label="Above 1.1"
)

plt.xlabel("Time")
plt.ylabel("Conversion Rate")
plt.title("EUR/USD Conversion Rate Highlighted Above 1.1")
plt.legend()
plt.show()

time = np.linspace(0, 2*np.pi, 100)
df = pd.DataFrame({
    "time": time,
    "sin": np.sin(time),
    "cos": np.cos(time)
})

# Numerical derivative using diff()
df["d_sin_dt"] = df["sin"].diff() / df["time"].diff()

# Plot both
plt.plot(df["time"], df["cos"], label="cos(t)")
plt.plot(df["time"], df["d_sin_dt"], label="d(sin)/dt (approx.)", linestyle='--')
plt.xlabel("Time")
plt.legend()
plt.title("Comparison of cos(t) and d(sin)/dt")
plt.show()
# .diff() loses one value each time it computes a difference.

# This makes the first (and sometimes last) points undefined or noisy because there’s no previous point to compute a difference from.