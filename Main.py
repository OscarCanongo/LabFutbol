import pandas as pd

defensivos = pd.read_csv("Defensivos.csv")
#print(defensivos)
#defensivos.dropna
print(defensivos.describe())

distribucion = pd.read_csv("Distribucion.csv")
#distribucion.dropna
print(distribucion.describe())
#(distribucion)

ofensivos = pd.read_csv("Ataque.csv")
#ofensivos.dropna
print(ofensivos.describe())
#print(ofensivos)