from scipy.optimize import curve_fit
import numpy as np
import pandas as pd

housing_data = pd.read_csv('./california_housing_test.csv')

# 선형관계를 모델링하는 함수 정의.
def linear_model(x, a, b):
    return a * x + b

x_data = housing_data['median_income']
y_data = housing_data['median_house_value']

params, covariance = curve_fit(linear_model, x_data, y_data)
print(f'Optimized parameters = {params}')   # params에 linear_model에 최적화된 파라미터인 기울기와 절편을 구할 수 있음.