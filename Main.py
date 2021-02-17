import pandas as pd

#Manejo de dataset defensivo
defensivos = pd.read_csv("Defensivos.csv")
#print(defensivos)
defensivos=defensivos.dropna() # Eliminamos Nulos
#print(list(defensivos.columns)) #Lista de Columnas para ver los Nombres
defensivos['DuelosGanados'] = defensivos['DuelosGanados'].str.rstrip('%').astype('float') #Transformamos los percentages
defensivos['DuelosAereosGanados'] = defensivos['DuelosAereosGanados'].str.rstrip('%').astype('float')
defensivos['BarridasGanadas'] = defensivos['BarridasGanadas'].str.rstrip('%').astype('float')
#print(defensivos.head())

#Estadisticas defensivas
x = defensivos.describe()
intercepcionesPartido = x['IntercepcionesPorPartido']['75%']
duelosGanados = x['DuelosGanados']['75%']
duelosAereosGanados = x['DuelosAereosGanados']['75%']
bloqueosPartido = x['Bloqueos/Partido']['75%']
despejesPartido = x['Despejes/Partido']['75%']
barridasGanadas = x['BarridasGanadas']['75%']

#Llenamos una lista con los mejores jugadores defensivos
intercepcionesList = (defensivos.loc[defensivos['IntercepcionesPorPartido'] > intercepcionesPartido])
duelosList = (defensivos.loc[defensivos['DuelosGanados'] > duelosGanados])
duelosAereosList = (defensivos.loc[defensivos['DuelosAereosGanados'] > duelosAereosGanados])
bloqueosList = (defensivos.loc[defensivos['Bloqueos/Partido'] > bloqueosPartido])
despejesList = (defensivos.loc[defensivos['Despejes/Partido'] > despejesPartido])
barridasList = (defensivos.loc[defensivos['BarridasGanadas'] > barridasGanadas])

#Obtenemos a los mejores Laterales defensivos
mejoresDefensivos = pd.concat([intercepcionesList, duelosList, duelosAereosList, bloqueosList, despejesList, barridasList])
#print(mejoresDefensivos.groupby(['Nombre']).sum())

#Manejo de Dataset Distribucion
distribucion = pd.read_csv("Distribucion.csv")
distribucion.dropna() # Eliminamos Nulos
distribucion['PasesAcertados'] = distribucion['PasesAcertados'].str.rstrip('%').astype('float')
distribucion['CambiosDeJuegoExitosos'] = distribucion['CambiosDeJuegoExitosos'].str.rstrip('%').astype('float')

#Estadisticas distribucion
y = distribucion.describe()
asistencias = y['Asistencias']['75%']
pasesAcertados = y['PasesAcertados']['75%']
toquesPartido = y['ToquesPorPartido']['75%']
cambiosJuegoExitosos = y['CambiosDeJuegoExitosos']['75%']
#print(distribucion.head())

#Llenamos una lista con los mejores jugadores en cuestion de distribucion
asistenciasList = (distribucion.loc[distribucion['Asistencias'] > asistencias])
pasesList = (distribucion.loc[distribucion['PasesAcertados'] > pasesAcertados])
toquesList = (distribucion.loc[distribucion['ToquesPorPartido'] > toquesPartido])
cambiosList = (distribucion.loc[distribucion['CambiosDeJuegoExitosos'] > cambiosJuegoExitosos])

#Obtenemos a los mejores Laterales en distribucion
mejoresDistribucion = pd.concat([asistenciasList, pasesList, toquesList, cambiosList])
#print(mejoresDistribucion.groupby(['Nombre']).sum())

#Manejo de Dataset Ofensivo
ofensivos = pd.read_csv("Ataque.csv")
ofensivos.dropna()
ofensivos['Tiros a puerta'] = ofensivos['Tiros a puerta'].str.rstrip('%').astype('float')
#print(ofensivos.head())
# print(ofensivos.describe())
#print(ofensivos)

#Estadisticas Ofensivas
z = ofensivos.describe()
goles = z['Goles']['75%']
tirosPuerta = z['Tiros a puerta']['75%']
regatesExitosos = z['Regates exitosos ']['75%']

#Llenamos una lista con los mejores jugadores en cuestion de ataque
golesList = (ofensivos.loc[ofensivos['Goles'] > goles])
tirosList = (ofensivos.loc[ofensivos['Tiros a puerta'] > tirosPuerta])
regatesList = (ofensivos.loc[ofensivos['Regates exitosos '] > regatesExitosos])

#Obtenemos a los mejores Laterales en distribucion
mejoresOfensivos = pd.concat([golesList, tirosList, regatesList])
#print(mejoresOfensivos.groupby(['Nombre']).sum())

mejoresLaterales = pd.concat([mejoresDefensivos, mejoresDistribucion, mejoresOfensivos])
print(mejoresLaterales)