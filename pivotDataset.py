import pandas as pd
file = "/Users/benny/Documents/LabFutbol/Laterales.csv"
df = pd.read_csv(file)
print(df.head())

df = df.pivot_table(columns="Nombre")
print(df.head())

df.to_csv("pivotTabla.csv")