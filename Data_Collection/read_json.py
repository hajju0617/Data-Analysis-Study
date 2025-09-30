import pandas as pd
import json
import os

os.chdir('C:/Data-Analysis/Data_Collection/data')

# 내장함수와 json 라이브러리를 이용해서 읽고 출력.
with open('data.json', 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)
    # json.load() : JSON 데이터 읽어옴.
print(data)

# pasdas를 이용해서 DataFrame으로 읽어서 출력.
df = pd.read_json('data.json', orient='records', encoding='utf-8', lines=False)
'''
orient : JSON 데이터가 어떤 형식으로 저장되어 있는지 알려주는 옵션.
lines : JSON 데이터(파일)이 여러 줄인지 여부를 지정.
'''
print(df)