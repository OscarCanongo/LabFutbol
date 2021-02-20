import pandas as pd
file = "/Users/benny/Documents/LabFutbol/Laterales.csv"
df = pd.read_csv(file)
# print(df.head())
print(df.dtypes)
df_T = df.T
print(df.dtypes)

print(df.head())
df_T.to_csv("pivotTabla.csv")