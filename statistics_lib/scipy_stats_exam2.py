from scipy import stats
import pandas as pd

'''
데이터타입
    pandas.describe() : 숫자 + 문자 모두 가능
    scipy.stats.describe() : 숫자형만 가능
출력형태		
    pandas.describe() : 표(DataFrame)
    scipy.stats.describe() : 튜플 형태 (통계요약 결과 객체)
'''

df = pd.read_csv('C:/Data-Analysis-Study/data-manager/data/student_scores.csv')
print(df)
print(df.describe())
print('======================')

desc = stats.describe(df[['math', 'english', 'science', 'korean', 'average']])
print(desc)