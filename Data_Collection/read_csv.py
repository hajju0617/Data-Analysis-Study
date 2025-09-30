import pandas as pd
import os

os.chdir('C:/Data-Analysis/Data_Collection/data')

df = pd.read_csv('data.csv', encoding='utf-8', sep=',', header=0,
                 index_col=None, skiprows=None, nrows=None)

'''
header : 열 이름으로 사용할 행 번호를 지정.
index_col : 인덱스로 사용할 열 번호 or 열 이름 지정.
skiprows : 파일의 상위 n개의 행을 건너뛰고 읽기.
nrows : 읽어 올 행의 개수를 제한.
'''

print(df)