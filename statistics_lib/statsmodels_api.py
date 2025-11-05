import statsmodels.api as sm
import pandas as pd

housing_data = pd.read_csv('./california_housing_test.csv')

X = housing_data['median_income']       # 독립 변수.
y = housing_data['median_house_value']  # 종속 변수.

X = sm.add_constant(X)                  # 상수항 추가.

# 선형회귀 모델 피팅.
model = sm.OLS(y, X).fit()
print(model.summary())
print('=================================')

# median_income(중간 소득)이 2.5, 4.5, 6.5인 세 단지에 대한 중위 소득 주택 가격을 예측.
new_data = pd.DataFrame({'const': 1, 'median_income': [2.5, 4.5, 6.5]})
predictions = model.predict(new_data)
print(predictions)