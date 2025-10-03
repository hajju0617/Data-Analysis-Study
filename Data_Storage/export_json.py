import pandas as pd
import json
import os
os.chdir('C:/Data-Analysis/Data_Storage/data')

data = {
    "이름": "홍길동",
    "나이": 25,
    "거주지": "서울",
    "관심사": ["프로그래밍", "데이터 분석", "영화"]
}

# 내장 라이브러리 json을 이용.
with open('output.json', mode='w', encoding='utf-8') as json_file:
    json.dump(data, json_file, indent = 4, ensure_ascii = False)


# pandas의 DataFrame을 이용.
df = pd.DataFrame(data)
print(df)
df.to_json('output_df.json', orient='records', indent = 4, force_ascii=False)