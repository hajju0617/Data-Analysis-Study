from scipy.signal import convolve
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_csv('./california_housing_test.csv')
median_house_value = df['median_house_value']

window_size = 5
window = np.ones(window_size) / window_size

smoothed_signal = convolve(median_house_value, window, mode='valid')

plt.figure(figsize=(10, 6))
plt.plot(median_house_value.index, median_house_value, label = 'Original')
plt.plot(np.arange(window_size - 1, len(median_house_value)), smoothed_signal, label = 'Smoothed', color = 'red')
plt.legend()
plt.show()
