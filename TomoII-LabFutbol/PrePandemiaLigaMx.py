import pandas as pd

disparosApuertaApertura = pd.read_html("https://mexico.as.com/resultados/futbol/mexico_apertura/2019/ranking/equipos/disparos-a-puerta/")
disparosApuertaClausura = pd.read_html("https://mexico.as.com/resultados/futbol/mexico_clausura/2020/ranking/equipos/disparos-a-puerta/")
dfdisparosAPuertaApertura = pd.DataFrame(disparosApuertaApertura[0])
dfdisparosAPuertaClausura = pd.DataFrame(disparosApuertaClausura[0])

golesApertura = pd.read_html("https://mexico.as.com/resultados/futbol/mexico_apertura/2019/ranking/equipos/goles/")
dfgolesApertura = pd.DataFrame(golesApertura[0])
golesClausura = pd.read_html("https://mexico.as.com/resultados/futbol/mexico_clausura/2020/ranking/equipos/goles/")
dfgolesClausura = pd.DataFrame(golesApertura[0])

#Componemos datos
dfgolesApertura['Equipo'] = dfgolesApertura['Equipo'].str.rstrip(' México')
dfgolesApertura['Total'] = dfgolesApertura['Total'].str.rstrip('Goles').astype('int')
dfgolesApertura = dfgolesApertura.drop(['Pos.'], axis = 1)
dfgolesApertura = dfgolesApertura.rename(columns={'Total':'Goles'})
dfgolesClausura['Equipo'] = dfgolesClausura['Equipo'].str.rstrip(' México')
dfgolesClausura['Total'] = dfgolesClausura['Total'].astype('int')
dfgolesClausura = dfgolesClausura.drop(['Pos.'], axis = 1)
dfgolesClausura = dfgolesClausura.rename(columns={'Total':'Goles'})

dfdisparosAPuertaApertura['Equipo'] = dfdisparosAPuertaApertura['Equipo'].str.rstrip(' México')
dfdisparosAPuertaClausura['Equipo'] = dfdisparosAPuertaClausura['Equipo'].str.rstrip(' México')
dfdisparosAPuertaApertura['Total'] = dfdisparosAPuertaApertura['Total'].str.rstrip('Disparos a puerta').astype('int')
dfdisparosAPuertaClausura['Total'] = dfdisparosAPuertaClausura['Total'].str.rstrip('Disparos a puerta').astype('int')
dfdisparosAPuertaApertura = dfdisparosAPuertaApertura.drop(['Pos.'], axis = 1)
dfdisparosAPuertaClausura = dfdisparosAPuertaClausura.drop(['Pos.'], axis = 1)

#Unimos el año futbolistico
dfdisparosAPuerta = pd.concat([dfdisparosAPuertaApertura, dfdisparosAPuertaClausura]).groupby(['Equipo']).sum().reset_index()
dfdisparosAPuerta = dfdisparosAPuerta.rename(columns = {'Total':'DisparosAPuerta'})
dfgoles = pd.concat([dfgolesApertura, dfgolesClausura]).groupby(['Equipo']).sum().reset_index()

#Inner Join dataframes
final = dfgoles.set_index('Equipo').join(dfdisparosAPuerta.set_index('Equipo'))

#InnerJoin de dataframes
print(final)