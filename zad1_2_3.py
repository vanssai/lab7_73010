import pandas as pd

df = pd.read_csv('demografia.csv', decimal='.', na_values=['.', 'NA', 'n/a', 'NaN'])
df.columns = df.columns.str.strip()

if 'KRAJE' in df.columns:
    df.rename(columns={'KRAJE': 'KRAJ'}, inplace=True)
if 'KRAJ' in df.columns:
    df['KRAJ'] = df['KRAJ'].astype(str).str.strip()

print(df.head())

if '2022' in df.columns:
    print(df.loc[df['2022'].idxmax(), 'KRAJ'])

df_num = df.drop(columns=['KRAJ'], errors='ignore')
col_max = df_num.max().idxmax()
row_idx = df_num[col_max].idxmax()
print(df.loc[row_idx, 'KRAJ'], col_max)