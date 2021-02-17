import pandas as pd

defensivos = pd.read_csv("Defensivos.csv")
#print(defensivos)
defensivos=defensivos.dropna() # Eliminamos Nulos
print(list(defensivos.columns)) #Lista de Columnas para ver los Nombres
defensivos['DuelosGanados'] = defensivos['DuelosGanados'].str.rstrip('%').astype('float') #Transformamos los percentages
defensivos['DuelosAereosGanados'] = defensivos['DuelosAereosGanados'].str.rstrip('%').astype('float')
defensivos['BarridasGanadas'] = defensivos['BarridasGanadas'].str.rstrip('%').astype('float')
print(defensivos.head())


distribucion = pd.read_csv("Distribucion.csv")
distribucion.dropna() # Eliminamos Nulos
print(distribucion.describe())
distribucion['PasesAcertados'] = distribucion['PasesAcertados'].str.rstrip('%').astype('float')
distribucion['CambiosDeJuegoExitosos'] = distribucion['CambiosDeJuegoExitosos'].str.rstrip('%').astype('float')
print(distribucion.head())

ofensivos = pd.read_csv("Ataque.csv")
ofensivos.dropna()
print(ofensivos.describe())
ofensivos['Tiros a puerta'] = ofensivos['Tiros a puerta'].str.rstrip('%').astype('float')
print(ofensivos.head())
# print(ofensivos.describe())
#print(ofensivos)