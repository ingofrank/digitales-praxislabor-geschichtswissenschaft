import pandas as pd

df_yu = pd.read_csv(
'VZ_YU1948-1981_numbers.csv', decimal=',', thousands='.')

print(df_yu.head())

df_yu_molten = df_yu.melt(
id_vars=['ethnicity'], var_name=['year'], value_name='value')

print(df_yu_molten.head())

df_yu_molten.to_csv(
'VZ_YU1948-1981_numbers_molten.csv', index=False) 
