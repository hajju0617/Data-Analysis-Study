import pandas as pd

data_a = {
    'A': ['A0', 'A1'],
    'B': ['B0', 'B1']
}
data_b = {
    'A': ['A2', 'A3'],
    'B': ['B2', 'B3']
}
df_1 = pd.DataFrame(data_a)
df_2 = pd.DataFrame(data_b)

result_concat = pd.concat([df_1, df_2], axis=0, ignore_index=True)
print(result_concat)
print('==========')
result_concat = pd.concat([df_1, df_2], axis=0, ignore_index=False)
print(result_concat)
print('==========')
result_concat = pd.concat([df_1, df_2], axis=1, ignore_index=True)
print(result_concat)
print('==========')
result_concat = pd.concat([df_1, df_2], axis=1, ignore_index=False)
print(result_concat)
print('==========')