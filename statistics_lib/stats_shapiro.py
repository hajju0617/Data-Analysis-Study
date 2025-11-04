from scipy import stats
import pandas as pd

df = pd.read_csv('./california_housing_test.csv')

# 가격 중앙값(median_house_value)을 구성하는 1700개 데이터에서 500개 추출하여 이들이 정규분포를 따르는지 확인.
shapiro_test = stats.shapiro(df['median_house_value'].sample(500))
print(f'Shapiro-Wilk Test Statistic : {shapiro_test.statistic}, p-value : {shapiro_test.pvalue}')

# t-검정 (주택 가격 중앙값의 평균이 20,000달러인가?)
t_test_result = stats.ttest_1samp(df['median_house_value'].sample(500), 200000)     # 평균 계산은 어디서? -> stats.ttest_1samp() 함수 내부.
print(f't-Statistic : {t_test_result.statistic}, p-value : {t_test_result.pvalue}')