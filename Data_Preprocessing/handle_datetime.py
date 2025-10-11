import pandas as pd

date_str = ['2025-07-01', '2025-08-01', '2025-09-01']   # 문자열
df_date = pd.DataFrame({'date_str':date_str})
print('df_date = \n', df_date)

# datetime 타입으로 변환.
df_date['date'] = pd.to_datetime(df_date['date_str'])   # date_str : 문자열, date : datetime 타입.
print('[datetime 타입으로 변환] df = \n', df_date)
print()
print('df_date.info() = \n', df_date.info())
print("*" * 30)

# 날짜 데이터 분리.
print('df_date["date"].dt.year = \n', df_date["date"].dt.year)
print()
print('df_date["date"].dt.month = \n', df_date["date"].dt.month)
print()
print('df_date["date"].dt.day = \n', df_date["date"].dt.day)
print()
print('df_date["date"].dt.day_name() = \n', df_date["date"].dt.day_name())
print("*" * 30)

# 날짜 데이터 포멧 변경.
df_date['date_formatted'] = df_date['date'].dt.strftime('%Y/%m/%d')
print('df_date = \n', df_date)
print()
df_date['date_ymd'] = df_date['date'].dt.strftime('%Y년 %m월 %d일')
df_date['date_dmy'] = df_date['date'].dt.strftime('%d-%m-%Y')
df_date['date_weekday'] = df_date['date'].dt.strftime('%A, %Y-%m-%d')
print('df_date = \n', df_date)